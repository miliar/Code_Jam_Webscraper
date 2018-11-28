#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
using namespace std;
const int MAXN=1000+10;
char p[MAXN];
int main()
{
//   freopen("in","r",stdin);
//   freopen("out","w",stdout);
    int t,kcase=0;
    ios::sync_with_stdio(false);
    cin>>t;
    while(t--)
    {
        int s,sum=0;
        cin>>s>>p;
        int ans=0;
        for(int i=0; i<=s; i++)
        {
            if(p[i]>'0')
            {
               if(sum<i)
               {
                  ans+=i-sum;
                  sum=i;
               }
            }            sum+=p[i]-'0';
        }
        cout<<"Case #"<<++kcase<<": ";
        cout<<ans<<endl;
    }
    return 0;
}
