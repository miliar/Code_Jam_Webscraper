#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a)    for(int i = 0;i < a;i++)
#define REP(i,a,b)  for(int i = a;i < b;i++)

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    REP(a,1,t+1)
    {
        int n;
        string s;
        cin>>n>>s;
        int curs=0;
        int pre=0;
        int ar[1010];
        for(int i=0;i<=n;i++)
        {
            ar[i]=s[i]-'0';
        }
        for(int i=0;i<=n;i++)
        {
          if(ar[i]>0)
          {
            if(curs>=i)
            {
                curs+=ar[i];
            }
            else
            {
                int diff=(i-curs);
                pre+=diff;
                curs+=(ar[i]);
                curs+=diff;
            }
          }
        }
        cout<<"Case #"<<a<<": "<<pre<<"\n";
    }
    return 0;
}
