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
#define pf printf
#define sc scanf
#define V vector
#define nl cout<<"\n";
#define deb(s) cout<<s<<endl;
#define PI (double)3.14159265358979323846264338
//int X[]={1,0,-1,0},Y[]={0,1,0,-1};
//string DIR="SENW";
//string ANS[]={"NO\n","YES\n"};
string Ans[]={"No\n","Yes\n"};
#define MAX 1000000007
#define MOD 1000000009
#define md(x,y) ((x%y+y)%y)
#define oo (int)1e9
#define INF 1000000000
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef int I;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
ull summ(ull n){return ((n*n)+n)/2;}
ull gcd (ull a,ull b){ull c;while(a!=0){c=a;a=b%a;b=c;}return b;}
double dist(ll x, ll y ,ll xx,ll yy){return sqrt((x-xx)*(x-xx)+ (y-yy)*(y-yy));}
///// Sherbi7y ////////////////////Actual solution starts here////////////////////////////////////
string arr[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string get(int n,map<char, int> mm)
{
    if(n== 0)
        return "\\";
    map<char, int> pp;
    for(int i=0;i<10;i++)
    {
        bool fl=1;
        for(int j=0;j<arr[i].len;j++)
        {
            if(!mm[arr[i][j]]){fl=0;break;}
        }
        if(fl)
        {
            pp= mm;
            for(int j=0;j<arr[i].len;j++)
            {
                pp[arr[i][j]]--;
            }
            string tt= get(n- arr[i].len, pp);
            if(tt.len)
                return tt+(char)(48+i);
        }
    }
    return "";
}
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);//cout.tie(0);//Better safe than sorry?
    #ifndef ONLINE_JUDGE
        freopen("A-small-attempt2.in","r",stdin);freopen("A2.out","w",stdout);
    #endif
    int n,cn=1;
    map<char, int> mm;
    cin>>n;
    string gg;
    while(n--)
    {
        cout<<"Case #"<<cn++<<": ";
        cin>>gg;
        mm.clear();
        forr(gg.len) mm[gg[i]]++;
        string gt=get(gg.len, mm);
        sort(all(gt));
        cout<<gt.substr(0,gt.len -1)<<"\n";

    }
    #ifndef ONLINE_JUDGE
       //cout<<fixed<<"TIME: "<<clock()/(CLOCKS_PER_SEC*1.0)<<"\n";
    #endif
    return 0;
}
/*

*/

/*

int Bullshit(int& l,int& r)
{
    int mid,cmp;
    while(l<r)
    {
        mid=(l+r+1)>>1;
        if(good(mid))

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

/*ull combi(ull n,ull k)
{
    ull ans=1;
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
/*
ll lcm(ll a, ll b)
{
    ll temp = gcd(a, b);
    return temp ? (a / temp * b) : 0;
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
