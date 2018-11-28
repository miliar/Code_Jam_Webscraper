/* Code Jam Template */
#include <bits/stdc++.h>
using namespace std;
#define MOD 					1000000007
#define pb(x) 					push_back(x)
#define mp(x,y)                 make_pair(x,y)
#define FF 						first
#define SS 						second
#define s(n) 					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
//special macro for reading a character of input
#define sc(n)                   {char temp[4]; ss(temp); n=temp[0];}
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
/*
Use these macros when comparing variables of different data types.
For e.g. comparing int and long long will give error when used with std::max, use maX instead.
*/
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
typedef long long ll;
typedef unsigned long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<ll> vl;
typedef vector<PII> VII;
typedef vector<TRI> VT;

/*Main code begins now*/

void precompute()
{
    /*
    Code that is common to all test cases and should be run before solving for any case, like Prime-NUmber Generation :)
    */
}
int l;
long long x;
string s;
void read()
{

    /*
    Read Global variables here
    */
    cin>>l>>x;
    cin>>s;
}
int arr[10004][10004];
map<char,int> mp;
void solve()
{
    /*
    Main logic goes here
    */
    mp.insert(make_pair('i',0));
    mp.insert(make_pair('j',1));
    mp.insert(make_pair('k',2));
    string str=s;

    while(--x)
    {
        s=s+str;
    }

    l=s.size();
    int i,j;
    for(i=0; i<l; i++)
    {

        arr[i][i]=mp[s[i]];

    }
    for(int len=2; len<=l; len++)
    {

        for(i=0; i+len-1<l; i++)
        {
            j=i+len-1;
            //cout<<j<<endl;
            if(s[j]=='i')
            {
                if(arr[i][j-1]==0) arr[i][j]=7;
                else if(arr[i][j-1]==1) arr[i][j]=5;
                else if(arr[i][j-1]==2) arr[i][j]=1;
                else if(arr[i][j-1]==3) arr[i][j]=6;
                else if(arr[i][j-1]==4) arr[i][j]=2;
                else if(arr[i][j-1]==5) arr[i][j]=4;
                else if(arr[i][j-1]==6) arr[i][j]=0;
                else if(arr[i][j-1]==7) arr[i][j]=3;
            }
            else if(s[j]=='j')
            {
                if(arr[i][j-1]==0) arr[i][j]=2;
                else if(arr[i][j-1]==1) arr[i][j]=7;
                else if(arr[i][j-1]==2) arr[i][j]=3;
                else if(arr[i][j-1]==3) arr[i][j]=5;
                else if(arr[i][j-1]==4) arr[i][j]=6;
                else if(arr[i][j-1]==5) arr[i][j]=0;
                else if(arr[i][j-1]==6) arr[i][j]=1;
                else arr[i][j]=4;
            }
            else
            {
                if(arr[i][j-1]==0) arr[i][j]=4;
                else if(arr[i][j-1]==1) arr[i][j]=0;
                else if(arr[i][j-1]==2) arr[i][j]=7;
                else if(arr[i][j-1]==3) arr[i][j]=1;
                else if(arr[i][j-1]==4) arr[i][j]=3;
                else if(arr[i][j-1]==5) arr[i][j]=6;
                else if(arr[i][j-1]==6) arr[i][j]=2;
                else arr[i][j]=5;
            }
        }
    }
    //cout<<arr[0][2]<<endl;
    int pos1=-1,pos2=-1,tmp;
    for(i=0; i<l; i++)
    {
        if(arr[0][i]==0)
        {
            pos1=i;
            break;
        }
    }
    if(pos1==-1)
    {
        cout<<"NO"<<endl;
        return ;
    }
    for(i=l-1; i>pos1; i--)
    {
        if(arr[i][l-1]==2)
        {
            pos2=i;
            break;
        }
    }

    if(pos2==-1)
    {
        cout<<"NO"<<endl;
        return ;
    }
    tmp=pos2;
    //cout<<pos1<<' '<<pos2<<endl;
    while(pos1<l)
    {
        //cout<<pos1<<' '<<pos2<<endl;
        pos2=tmp;
        while(pos1+1<=pos2-1)
        {
            if(arr[pos1+1][pos2-1]==1)
            {
                cout<<"YES"<<endl;
                return ;
            }
            for(i=pos2-1; i>pos1; i--)
            {
                if(arr[i][l-1]==2)
                {
                    pos2=i;
                    break;
                }
            }
            if(i==pos1) break;
        }
        for(i=pos1+1; i<l; i++)
        {
            if(arr[0][i]==0)
            {
                pos1=i;
                break;
            }
        }
        if(i==l) break;
    }
    cout<<"NO"<<endl;
}
/*
This main function will remain same in all implementations.
Make sure that input file is present in same directory and if changing the filename(s), don't forget to include extensions(.in) as well.
*/
int main()
{
    freopen("C.in", "r", stdin);
    freopen("output.in", "w", stdout);
    precompute();
    int t;
    s(t);

    for(int T = 1; T <= t; T++)
    {
       // cout<<T;
        read();
        printf("Case #%d: ",T);
        solve();
    }
    return 0;
}
