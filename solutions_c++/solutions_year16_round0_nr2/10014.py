
#include<bits/stdc++.h>

using namespace std;



void all(string str);

int c=0,z=0,o=0,q=0;
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
int f=0;
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

string flip(string in,int p,int k)
{


        f++;


    string str = in.substr(p,k);
    //cout<<str<<endl;
    reverse(str.begin(),str.end());
    //cout<<str<<endl;
    for(int i=0; i<str.length(); ++i)
    {
        if(str[i]=='+')
            str[i]='-';
        else
            str[i]='+';
    }
    //cout<<str<<endl;
    for(int j=p; j<str.length(); ++j)
    {
        //cout<<in[j]<<endl;
        in[j]=str[j-p];
    }
    //cout<<in<<endl;
    return in;
}


void solve()
{
    int t;
    cin>>t;
    vector<string>v;
    string str;
    for(int i=1; i<=t; ++i)
    {
        cin>>str;
        all(str);
       cout<<"Case #"<<i<<": ";
        if(z>1||c>1)
        {
            if(c>1)
                cout<<q<<endl;
            else
                cout<<o<<endl;
        }

        else
            cout<<f<<endl;
        f=0;c=0,z=0,o=0;
    }
}

void all(string str)
{

    int siz = str.length();
    //cout<<"str size = "<<siz<<endl;
    int a=0,p=0,m=0;
    for(int j=0; j<siz; ++j)
    {
        if(str[j]=='+')
        {
            p++;
        }
        if(str[j]=='-')
        {
            m++;
        }
    }
 //  cout<<"p = "<<p<<" m = "<<m<<endl;

    if(p==siz)
    {
        //cout<<"Case #"<<i<<": ";
        //cout<<0<<endl;
       //  cout<<"Here in pos . f = "<<f<<endl;

        if(c<1)
        {
            f=f+0;
            q=f;
        }

        //solve();
        //goto x;
        c++;
        return;
    }
    if(m==siz)
    {
       // cout<<"Here in neg . f = "<<f<<endl;

        //cout<<"Case #"<<i<<": ";
     //   cout<<"z = "<<z<<endl;
        if(z<1)
        {
          //  cout<<"prev f = "<<f;
            f=f+1;
            o=f;
          //  cout<<"curr f = "<<f<<endl;
        }
        //solve();
        //goto x;
        z++;
       // cout<<"z = "<<z<<endl;
      //  cout<<"Here in neg . f = "<<f<<endl;
        return;
    }
    if(m>p)
    {
        //str=flip(str,0,siz);
    }
    for(int k=0; k<siz; ++k)
    {
        int prev=0;
        if(str[k]=='-'&&k!=0)
        {
            str=flip(str,prev,k);
            //cout<<str<<" f= "<<f<<endl;
            while(str[k]!='+'&&k<siz)
            {
                k++;
            }
            //str=flip(str,prev,k+1);
         //  cout<<str<<" f = "<<f<<endl;
         //   cout<<"here in if and f="<<f<<endl;
            //goto x;
            all(str);
        }
        else if(str[k]=='-')
        {
            while(str[k]!='+'&&k<siz)
            {
                k++;
            }
            str=flip(str,prev,k);
         //   cout<<"here in else and f="<<f<<endl;
          //  cout<<str<<" f = "<<f<<endl;//goto x;
            all(str);
        }
    }
}
//main_function
int Mahmud
{
    //ios_base::sync_with_stdio(0); cin.tie(0);
//#ifdef _LOCAL_
    freopen("B-small-attempt2.in", "r", stdin); freopen("out.txt", "w", stdout);
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




