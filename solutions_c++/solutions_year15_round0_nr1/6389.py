// codersan
#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define init(a,b) memset(a,b,sizeof(a));
#define pnl() printf("\n");
#define tr(container,it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define sortv(a) sort(a.begin(),a.end());
#define go()  int t; cin>>t; while(t--)
#define forl(i,a,b) for(int i=a;i<b;i++)
#define rofl(i,a,b) for(int i=a;i>b;i--)
#define LL long long int
#define mod 1000000007
using namespace std;
typedef vector<int> vi;
typedef pair<int , int> pii;
typedef vector<pii> vpii;
inline LL gcd(LL a, LL b){ LL temp; while(b>0)	{ temp= b; b=a%b; a=temp;}	return a;}
inline LL fast(LL a, LL b)
{
    LL prod=1;
    while(b)
    {
        if(b&1)prod=(prod*a);
        a=(a*a),b/=2;
    }
    return prod;
}
int main()
{
    #ifndef ONLINE_JUDGE
       freopen("C:\\Users\\codersan\\Desktop\\GCJ\\Ain.in", "r", stdin);
        freopen("C:\\Users\\codersan\\Desktop\\GCJ\\Aout.txt", "w", stdout);
    #endif
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        LL ans=0;
        int len,val;
        string s;
        cin>>len>>s;
        val=s[0]-'0';
        for(int i=1;i<s.length();i++)
        {
            if(val>=i)
               val=val+(s[i]-'0');
            else
                ans=ans+i-val,val=i+(s[i]-'0');
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }

return 0;
}
