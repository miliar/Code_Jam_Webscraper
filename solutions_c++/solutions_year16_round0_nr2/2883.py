#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define mod 1000000007
#define reset(s,val) memset(s,val,sizeof(s))
#define eps 1e-9
#define pi acos(-1)
#define sqr(x) (x)*(x)
#define two(x) (1<<(x))

int t,n;
string s;

int main( ){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin>>t;
    For(cas,1,1+t)
    {
        cout<<"Case #"<<cas<<": ";
        cin>>s;
        n=s.size();
        int ans=0;
        while(1)
        {
            int id=-1;
            For(i,0,n) if(s[i]=='-') id=i;
            if(id==-1) break;
            if(s[0]=='+')
            {
                ans++;
                For(i,0,id+1)
                {
                    if(s[i]=='+') s[i]='-';
                    else break;
                }
            }
            ans++;
            For(i,0,id+1)
            {
                if(s[i]=='-') s[i]='+';
                else s[i]='-';
            }
            For(i,0,(id+1)/2) swap(s[i],s[id-i]);
        }
        cout<<ans<<endl;
    }
}
