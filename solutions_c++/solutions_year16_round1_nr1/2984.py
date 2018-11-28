#include<bits/stdc++.h>
#define ll long long int
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define INF 99999999
#define pii pair<int,int>
#define MAX 1005
int Set(int n,int pos) {return n | (1<<pos);}
int Reset(int n,int pos){return n & ~(1<<pos);}
int Check(int n,int pos){return n & (1<<pos);}
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,T=0,i;
    string s,ans;
    cin>>t;
    while(t--)
    {
        cin>>s;
        for(i=0,ans="";i<s.size();i++)
        {
            if(!i)
                ans+=s[i];
            else
            {
                if(s[i]>=ans[0])
                    ans=s[i]+ans;
                else
                    ans=ans+s[i];
            }
        }
        cout<<"Case #"<<++T<<": "<<ans<<endl;
    }
    return 0;
}
