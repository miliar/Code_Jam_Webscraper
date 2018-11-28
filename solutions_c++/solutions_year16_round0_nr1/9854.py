
#include<bits/stdc++.h>

using namespace std;
//constant
const unsigned int M = 1000000007;
const int MOD = (int) 1e9 + 7;
const int INF = (int) 1e9;
const long long LINF = (long long) 1e18;
const long double PI = 2 * acos((long double)0);
//typedef
typedef unsigned long long un;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pi> vii;
typedef complex<double> point;
//definition
#define Mahmud main()
#define endl "\n"
//for_loop
#define for0(i,n) for(int i=0;i<(n);++i)  //for loop from zero
#define for1(i,n) for(int i=1;i<=(n);++i)  //for loop from one
#define for2(i,a,b) for(int i=(a);i<=(b);++i)  //for loop from a to b
#define for3(i,a,b) for(int i=(a)-1;i>=(b);i--) //for loop reverse
//input
#define DRI(X) int (X);scanf("%d",&X)
#define RI(X) scanf("%d", &(X))
#define DRII(X, Y) int X,Y;scanf("%d%d",&X,&Y)
#define RII(X,Y) scanf("%d%d",&(X),&(Y))
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define RS(X) scanf("%s",(X))
#define DRLI(X) ll X;scanf("%lld",&(X))
//print
#define PRINT(x) printf("%d\n",x)
#define CasePrint(i) printf("Case %d: ",n)
#define New_Line printf("\n")
//vector
#define pb push_back
#define pf push_front
#define mp make_pair
#define bitcount(n) __builtin_popcount(n)
#define EPS 1e-9
//function
ll gcd(ll a,ll b)
{
    ll r;    //greatest common divisor
    while(b!=0)
    {
        r=a%b;
        a=b;
        b=r;
    }
    return a;
}
ll lcm(ll a,ll b)
{
    return a/gcd(a,b)*b;   //least common multiple
}
ll power(ll a, ll n)
{
    ll p = 1;
    while (n > 0)
    {
        if(n%2)
        {
            p = p * a;
        }
        n >>= 1;
        a *= a;
    }
    return p;
}
void setmin(int& a,int val)
{
    if(a>val) a=val;
}
void setmax(int& a,int val)
{
    if(a<val) a=val;
}
string DecimalToBinay(ll n)
{
    ll len  ;
    if(n<256)
        len=128;
    else if(n<65536)
        len=32768;
    else
        len=4294967296;
    ll y;
    string bin;
    for(ll i=len; i>0; i/=2)
    {
        if(n & i)
        {
            bin.push_back('1');
            //cout<<"Here 1add  i = "<<i<<" n&i = " << (n&i) << endl;
        }
        else
        {
            //cout<<"Here 0add i = "<<i<<" n&i = " << (n&i) << endl;
            bin.push_back('0');
        }
    }
    //istringstream b(bin);
    //b >> y ;
    return bin;
}

vector<int> split(string str)
{
    int x,y;
    istringstream iss(str);
    vector<int> v ;
    string s;
    while(getline(iss,s,':'))
    {
        istringstream brr(s);
        brr>>x;
        v.push_back(x);
    }
    return v;
}
int one=0,two=0,three=0,four=0,five=0,six=0,seven=0,eight=0,nine=0,zero=0;
bool is(ll n)
{

    ll rem=n,res;
    //cout<<rem<<endl;
    while(rem!=0)
    {
        //cout<<"In while rem"<<rem<<endl;
        res=rem%10;
        rem/=10;
        if(res==0)
            zero++;
        else if(res==1)
            one++;
        else if(res==2)
            two++;
        else if(res==3)
            three++;
        else if(res==4)
            four++;
        else if(res==5)
            five++;
        else if(res==6)
            six++;
        else if(res==7)
            seven++;
        else if(res==8)
            eight++;
        else if(res==9)
            nine++;
    }
    if(one>0&&two>0&&three>0&&four>0&&five>0&&six>0&&seven>0&&eight>0&&nine>0&&zero>0)
        return true;
    return false;
}

void solve()
{
    int t;
    cin>>t;
    ll n,res,rem;
    for(int i=1; i<=t; ++i)
    {
        cin>>n;
        res=n;
        int k=2;
        //cout<<"here"<<i<<endl;
        if(n==0)
        {
             cout<<"Case #"<<i<<": ";cout<<"INSOMNIA"<<endl;continue;
        }

        while(is(res)==false)
        {
            //cout<<"here "<<res<<endl;
            res=n*k++;

        }
        cout<<"Case #"<<i<<": ";
        cout<<res<<endl;
        one=0,two=0,three=0,four=0,five=0,six=0,seven=0,eight=0,nine=0,zero=0;
    }
}
//main_function
int Mahmud
{
    //ios_base::sync_with_stdio(0); cin.tie(0);
//#ifdef _LOCAL_
    freopen("A-large.in", "r", stdin); freopen("out.txt", "w", stdout);
//#endif
    solve();
//#ifdef _LOCAL_
    //printf("\nTime elapsed: %dms", 1000 * clock() / CLOCKS_PER_SEC);
//#endif


//    FILE *f;char c;
//    f=fopen(__FILE__,"r");
//    while((c=fgetc(f))!=EOF)
//        printf("%c",c);
//    fclose(f);

    return 0;
}



