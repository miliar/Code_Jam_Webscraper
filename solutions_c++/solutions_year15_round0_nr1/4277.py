//Author: Siddharth Saluja
//Quote: "LIVE FOR YOUR AIM"

#include<bits/stdc++.h>

/* Constants */
#define mod 1000000007
#define imax 2147483647
#define imin -2147483648
#define pi 3.14159265358979323846264338327950
#define eps 1E-9
/* constants end  */
//#define DEBUG

/* stl templates */
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define vi vector<int>
#define vs vector<string>
#define vvi vector<vector<int> >
#define vpii vector<pair<int,int> >
#define vl vector<long long>
#define vvl vector<vector<long long> >
#define vpll vector<pair<long,long> >
#define sz(x) (int)x.size()
#define ln(s) (int)s.length()
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define pii pair<int,int>
#define pll pair<long long,long long>
#define psi pair<string,int>
#define psl pair<string,long long >
#define aa first
#define bb second
/* stl templates end */

/* looping templates */
#define fori(s,e) for(i=s;i<=e;i++)
#define forj(s,e) for(j=s;j<=e;j++)
#define fork(s,e) for(k=s;k<=e;k++)
#define rep(i,s,e) for(int i=s;i<=e;i++)
/* looping templates end */

/* general templates */
#define mem(x,y) memset(x,y,sizeof(x));
#define ull unsigned long long
#define ll long long
#define s(a) scanf("%d",&a)
#define lls(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define p(a) printf("%d",a)
#define llp(a) printf("%lld",a)
#define sp(a) printf("%s",a)
#define cp(a) printf("%c",a)
#define nline printf("\n")
#define space printf(" ")
/* general templates end */


using namespace std;
ll int scan()
{
    ll int t=0;
    char c,ch;
    ch=getchar();
    if (ch=='-')
    {
        c=getchar();
    }
    else
    {
        c=ch;
    }
    while(c<'0' || c>'9')
    {
        c=getchar();
    }
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar();
    }
    if (ch=='-' )
    {
        return -t;
    }
    else
    {
        return t;
    }
}

int main()
{
#ifdef DEBUG
cout<<"Debugging\n";
#endif
freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
ios::sync_with_stdio(false);
ll int i,j,k,t,n,m,x,y;
string s;
cin>>t;
ll u=t;
while(t--)
{
    cin>>n;
    cin>>s;
    ll max_standing=0,ans=0;
    max_standing=s[0]-'0';
    for(i=1;i<=n;i++)
    {
        if(s[i]=='0')continue;

        if(max_standing<i)
        {
            ans+=(i-max_standing);
            max_standing=i;
            max_standing+=(s[i]-'0');
        }
        else
        {
            max_standing+=(s[i]-'0');
        }
    }
    cout<<"Case #"<<u-t<<": "<<ans<<"\n";
}

return 0;
}
