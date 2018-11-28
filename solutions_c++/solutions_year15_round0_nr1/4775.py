#include <vector>
#include <climits>
#include <stack>
#include <map>
#include <algorithm>
#include <list>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <queue>
#define ll long long
#define s1(a) scanf("%d",&a)
#define sc(a) scanf("%c",&a)
#define s1ll(a) scanf("%lld",&a)
#define s2(a,b) scanf("%d %d",&a,&b)
#define s2ll(a,b) scanf("%lld %lld",&a,&b)
#define s1d(a) scanf("%lf",&a)
#define s2d(a,b) scanf("%lf %lf",&a,&b)
#define p1(a) printf("%d\n",a)
#define pc(a) printf("%c\n",a)
#define p1ll(a) printf("%lld\n",a)
#define p1d(a) printf("%lf\n",a)
#define MAX 1000000
using namespace std;
int main()
{
    int t;
    s1(t);
    for(int ii=1;ii<=t;ii++)
    {
        int len;
        string str;
        cin>>len>>str;
        int ans=0;
        int sum=str[0]-48;
        for(int i=1;i<=len;i++)
        {
            if(i>sum)
            {
                int p = i-sum;
                ans=ans+(p);
                sum+=p;
            }
            sum+=str[i]-48;

        }
        //cout<<sum<<" "<<ans<<endl;
        printf("Case #%d: %d\n",ii,ans);
    }
}
