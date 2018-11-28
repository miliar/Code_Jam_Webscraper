#include <iostream>
#include <algorithm>
#include <cstring>
#include <utility>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
using namespace std;

#define for1(i,n) for(i=0;i<n;i++)
#define for2(i,n) for(i=1;i<=n;i++)
#define all(v) v.begin(),v.end()
#define set(a,b) memset(a,b,sizeof a)
#define cin3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define cin2(a,b) scanf("%d%d",&a,&b)
#define cin1(a) scanf("%d",&a)
#define pb push_back
#define mp make_pair
#define inf  1e8


int main()
{
    int i,j,k,l,loop;
    double r1,r2,r3,ans,cps,f,x,c;
    cin1(loop);
    for2(l,loop)
    {
        cin>>c>>f>>x;
        ans=0.0;
        cps=2.00;
        while(1)
        {
            r1=x/cps;
            r2=c/cps;
            r3=x/(cps+f);
            if(r1<=r2+r3)
            {
                ans+=r1;
                break;
            }
            else
            {
                ans+=r2;
                cps+=f;
            }
        }
        printf("Case #%d: %.7lf\n",l,ans);
    }
    return 0;
}
