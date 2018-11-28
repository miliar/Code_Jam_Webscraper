#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <cmath>
using namespace std;
typedef long long ll;
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
int warCnt(const vector<double> naomi, const vector<double> ken)
{
    int n=naomi.size(), win = 0;
    set<double> wt(ken.begin(), ken.end());
    FOR(i,0, n)
    {
        if (*wt.rbegin() < naomi[i])
            wt.erase(wt.begin());
        else
        {
            wt.erase(wt.lower_bound(naomi[i]));
            win++;
        }
    }
    return n-win;
}
bool fncomp (double lhs, double rhs) {return lhs>rhs;}

int DecWar(const vector<double> naomi, const vector<double> ken)
{
    int n=naomi.size(), win = 0;
    set<double> naomis(naomi.begin(), naomi.end());
    bool(*fn_pt)(double,double) = fncomp;
    std::set<double,bool(*)(double,double)> kens(ken.begin(),ken.end(), fn_pt);
//    std::set<double> kens(ken.begin(),ken.end());
  
    while(true)
    {
        if (naomis.size() == 0)
            break; 
        if (*naomis.begin() < *kens.rbegin())
        {
            naomis.erase(naomis.begin());
            kens.erase(kens.begin());
        }
        else
        {
            naomis.erase(naomis.begin());
            std::set<double>::iterator it= kens.begin();
            FOR(i,0, kens.size() -1)
                ++it;

            kens.erase(it);
            win++;
        }

    }
    return win;
}
int main()
{
	FILE* fin = freopen("D-large.in","rt",stdin);
	FILE* fout = freopen("D-large.out","wt",stdout);
    int t;
    std::cin>>t;

    FOR(zz, 0, t)
    {
        int n;
        scanf("%d",&n);
        vector<double> naomi, ken;
        FOR(i,0,n)
        {
            double t;
            scanf("%lf", &t);
            naomi.push_back(t);
        }
        FOR(i,0,n)
        {
            double t;
            scanf("%lf", &t);
            ken.push_back(t);
        }
        printf("Case #%d: %d %d\n", zz+1, DecWar(naomi, ken), warCnt(naomi, ken));
        
    }
    fclose(fout);
    fclose(fin);
    return 1;
}