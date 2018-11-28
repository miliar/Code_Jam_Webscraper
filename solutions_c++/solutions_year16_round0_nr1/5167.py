#include <bits/stdc++.h>
using namespace std;
/* YOU DO NOT TELL ME WHETHER MY SOLUTION IS RIGHT, SKYNET!!! */
#define forr(n) for (int i=0;i<n;i++)
#define pb push_back
#define len size()
#define mems(a,v) memset(a,v,(int)sizeof a)
#define all(v) v.begin(),v.end()
#define sz(v)  ((int)((v).size()))
#define rall(v) v.rbegin(),v.rend()
#define mp(x,y) make_pair(x,y)
#define fr first
#define se second
//#define p printf
#define sc scanf
#define V vector
#define nl cout<<"\n";
#define deb(s) cout<<"here"<<s<<endl;
#define PI (double)3.14159265358979323846264338
int X[]={1,0,-1,0},Y[]={0,1,0,-1};
string DIR="SENW";
#define MAX 1000000007
#define MOD 1000000009
#define md(x,y) ((x%y+y)%y)
#define oo (int)1e9
typedef pair<int,int> ii;
typedef unsigned long long ull;
typedef long long ll;
typedef int I;
ull summ(ull n){return ((n*n)+n)/2;}
ull gcd (ull a,ull b){ull c;while(a!=0){c=a;a=b%a;b=c;}return b;}
double dist(ll x, ll y ,ll xx,ll yy){return sqrt((x-xx)*(x-xx)+ (y-yy)*(y-yy));}
///Actual solution starts here////////////////////Sherbi7y///////////////////////////////
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    cout.tie(0);//Better safe than sorry?

    #ifndef ONLINE_JUDGE
        freopen("A-large.in","r",stdin);freopen("A2.out","w",stdout);
    #endif
    ll t,n,cn=1,acc,rr;
    cin>>t;
    set<int> ss;
    while(t--)
    {
        cout<<"Case #"<<cn++<<": ";
        cin>>n;
        //acc=n;
        ss.clear();
        acc=0;
        if(n==0) {cout<<"INSOMNIA\n";continue;}
        while(ss.size() < 10)
        {
            acc+=n;
            rr=acc;
            while(rr)
            {
                ss.insert(rr%10);
                rr/=10;
            }
        }
        cout<<acc<<"\n";
    }
    return 0;
}

/*
int Bullshit(int& l,int& r)
{
    int mid,cmp;
    while(l<r)
    {
        mid=(l+r+1)>>1;
        if(good(mid))
        {
            l=mid;
        }
        else 
        {
            r=mid-1;
        }
    }
    return mid;
}
*/
/*cin>>n>>m;
    for(int cn=1;n||m;cn++)
    {
        forr(n)cin>>arr[i];
        mems(brr,1);
        int maxx=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(brr[i][j]&& arr[i][j]=='@'){
                    maxx+=good(i,j,arr[i][j]);
                }
            }
        }
        cout<<maxx<<"\n";
        cin>>n>>m;
    }*/

/*ULL combi(ULL n,ULL k)
{
    ULL ans=1;
    k=k>n-k?n-k:k;
    int j=1;
    for(;j<=k;j++,n--)
    {
        if(n%j==0)
        {
            ans*=n/j;
        }else
        if(ans%j==0)
        {
            ans=ans/j*n;
        }else
        {
            ans=(ans*n)/j;
        }
    }
    return ans;
}*/
/*
long long pw( long long base, long long power)
{
    if (power == 0) return 1;
    if (power % 2) return pw(base, power - 1)*base % 1000000007;
    if (power % 2 == 0) return pw((base*base) % 1000000007, power / 2);
}
*/
/*int t,so,st,bo,bt;
    string s;
    cin>>t;
    while(t--)
    {
        cin>>s;
        so=st=bo=bt=0;
    }*/
        /*template <typename K, typename V>
bool comparePairs(const std::pair<K,V>& lhs, const std::pair<K,V>& rhs)
{
    if(lhs.first < rhs.first)
       return 1;
    if(lhs.se > rhs.se)
        return 1;
    return 0;
}*/