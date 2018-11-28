#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;
#define EPS 1e-9

vector<double> N, K;

int war()
{
    int c;
    bool found;
    vector<double>::iterator it;
    vector<double> n = N;
    vector<double> k = K;
    sort(k.begin(),k.end());
    int ans = 0;
    for(c=0;c<n.size();c++)
    {
        found = false;
        for(it=k.begin();it!=k.end();it++) if((*it)>n[c])
        {
            k.erase(it);
            found = true;
            break;
        }
        if(!found)
        {
            k.erase(k.begin());
            ans++;
        }
    }
    return ans;
}

int deceitful()
{
    int c;
    bool found;
    vector<double>::iterator it;
    vector<double> n = N;
    vector<double> k = K;
    sort(n.begin(),n.end());
    sort(k.begin(),k.end());
    while(fabs(k[k.size()-1]-1.0)<EPS)
    {
        k.erase(k.begin()+(k.size()-1));
        n.erase(n.begin());
    }
    int ans = 0;
    for(c=0;c<n.size();c++)
    {
        if(n[c]>k[0])
        {
            k.erase(k.begin());
            ans++;
        }
        else
        {
            k.erase(k.begin()+(k.size()-1));
        }
    }
    return ans;
}

int main()
{
    int T,c,n;
    double temp;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++)
    {
        N.clear();
        K.clear();
        scanf("%d",&n);
        for(c=0;c<n;c++)
        {
            scanf("%lf",&temp);
            N.push_back(temp);
        }
        for(c=0;c<n;c++)
        {
            scanf("%lf",&temp);
            K.push_back(temp);
        }
        printf("Case #%d: %d %d\n",tc,deceitful(),war());
    }
    return 0;
}
