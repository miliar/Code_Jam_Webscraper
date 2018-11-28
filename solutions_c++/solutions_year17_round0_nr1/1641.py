#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(int)a;i<=(int)b;i++)
#define rip(i,a,b) for(int i=(int)a;i>=(int)b;i--)
#define ll long long
#define MOD 1000000007
#define N 200005
#define f first
#define s second
#define pb push_back
#define pii pair<int,int>
#define matrix vector<vector<ll>>
#define PI acos(-1)
#define INF 10000000
#define LSOne(S) (S & (-S))
int main() {
   freopen("/home/vikhyat/Desktop/in.txt","r",stdin);
   freopen("/home/vikhyat/Desktop/out.txt","w",stdout);
   // ios_base::sync_with_stdio(false);
//	cin.tie(0);
	//cout.tie(0);
    int t;
    cin>>t;
    rep(_,1,t)
    {
        string s;
        int k;
        cin>>s>>k;
        cout<<"Case #"<<_<<": ";
        int l=s.length(),ans=0;
        rep(i,0,l-k)
        {
            if(s[i]=='-')
            {
                rep(j,i,i+k-1)
                {
                    if(s[j]=='-')
                    s[j]='+';
                    else
                    s[j]='-';
                }
                ans++;
            }
        }
        int f=0;
        rep(i,0,l-1)
        {
            if(s[i]=='-')
            {
                f=1;
            }
        }
        if(f==1)
        cout<<"IMPOSSIBLE\n";
        else
        cout<<ans<<endl;
    }
    return 0;
}
