#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> read_blocks(int n)
{
    vector<int> blocks(n);
    for(auto &b : blocks)
    {
        double f;
        scanf("%lf", &f);
        b = static_cast<int>(100000*f);
    }
    
    sort(blocks.begin(), blocks.end());    
    return blocks;
}

int deceitful_war(const vector<int>& naomi, const vector<int>& ken)
{
    int resp = 0;
    auto bken = ken.begin();
    auto eken = ken.end();
    for(auto b : naomi)
    {
        if(b > *bken)
        {
            ++resp;
            ++bken;
        }
        else
        {
            --eken;
        }
    }
    
    return resp;
}

int war(const vector<int>& naomi, const vector<int>& ken)
{
    set<int> kset(ken.begin(), ken.end());
    int resp = 0;
    for(auto b : naomi)
    {
        auto it = kset.upper_bound(b);
        if(it == kset.end())
        {
            ++resp;
            kset.erase(kset.begin());
        }
        else
        {
            kset.erase(it);
        }
        
    }
    
    return resp;
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int lp=1;lp<=t;++lp)
    {
        int n;
        scanf("%d", &n);
        auto naomi = read_blocks(n);
        auto ken = read_blocks(n);
        
        auto dresp = deceitful_war(naomi, ken);
        auto wresp = war(naomi, ken);
        printf("Case #%d: %d %d\n", lp, dresp, wresp);
    }
    
    return 0;
}