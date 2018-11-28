/*
ID:maruf911
PROG:
LANG: C++
*/

/**Bismillahir Rahmanir Rahim
   In the name of ALLAH, most gracious, most merciful */
#include <bits/stdc++.h>
using namespace std;
#define inf           100000000000000000LL
#define pb            push_back
#define mp            make_pair
#define eps           1e-9
#define nl            printf("\n")
#define spc           printf(" ")
#define sci(n)        scanf("%ld",&n)
#define sc64(n)       scanf("%I64d",&n)
#define scii(a,b)     scanf("%ld %ld",&a,&b)
#define sc6464(a,b)   scanf("%I64d %I64d",&a,&b)
#define scs(s)        scanf("%s",s)
#define scss(a,b)     scanf("%s %s",a,b)
#define scd(f)        scanf("%lf",&f)
#define scdd(a,b)     scanf("%lf %lf",&a,&b)
#define prc(k)        printf("Case %ld: ",k);
#define pri(a)        printf("%ld",a)
#define pr64(a)       printf("%I64d",a)
#define prii(a,b)     printf("%ld %ld",a,b)
#define pr6464(a,b)   printf("%I64d %I64d",a,b)
#define prs(a)        printf("%s",a)
#define prss(a,b)     printf("%s %s",a,b)
#define prd(a)        printf("%lf",a)
#define prdd(a,b)     printf("%lf %lf",a,b)
#define rep(i,n)      for(int i(0),_n(n);i<_n;++i)
#define repr(i,n)     for(int i=n;i>=0;i--)
#define repi(i,a,b)   for(int i(a),_b(b);i<=_b;++i)
#define repl(i,n)     for(int i(1),_n(n);i<=_n;++i)
#define repir(i,a,b)  for(int i=a;i>=b;i--)
#define chk(a,k) ((bool)(a&(1<<(k))))
#define off(a,k) (a&(~(1<<(k))))
#define on(a,k) (a|(1<<(k)))
int Set(int N,int pos) {return N |= (1LL<<pos);}
int Reset(int N,int pos) {return N&= ~(1LL<<pos);}
bool Check(int N,int pos) {return N&(1LL<<pos);}
#define ff            first
#define ss            second
#define all(a)        a.begin(),a.end()
#define mem(x,a)      memset(x,a,sizeof(x))
#define repe(it,c)    for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
int dx[]={0,0,1,-1,1,-1,1,-1},dy[]={1,-1,0,0,1,-1,-1,1};
typedef vector<int> vi;
typedef vector<long> vl;
typedef vector<long long> vll;
typedef vector<string> vs;
#define ll long long
typedef vector<vector<int> > vvi;
typedef pair<int,int> pr;
inline void cn( long &n )//fast input function
{
n=0;
long ch=getchar();int sign=1;
while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getchar();}
while(ch >= '0' && ch <= '9')
n = (n<<3)+(n<<1) + ch-'0', ch=getchar();
n=n*sign;
}
template<class T> void cmin(T &a,T b){if(b<a) a=b;}
template<class T> void cmax(T &a,T b){if(b>a) a=b;}
template<class T> int len(const T&c){return (int)c.size();}
template<class T> int len(char c[]){return (int)strlen(c);}
//string itos(long n){string s;while(n){s+=(n%10+48);n/=10;}reverse(all(s));return s;}
long stoi(string s){long n=0;rep(i,len(s))n=n*10+(s[i]-48);return n;}

int ar[11],cnt;

void fun(long n)
{
    while(n)
    {
        int r;
        r=n%10;
        if(ar[r]==0)
        {
            ar[r]=1;
            cnt--;
        }
        n/=10;
    }
}

int main()
{
ios_base::sync_with_stdio(false);
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
long t,kase;
cin>>t;
for(kase=1;kase<=t;kase++)
{
    long long n,i;
    cnt=10;
    for(int j=0;j<10;j++) ar[j]=0;
    cin>>n;
    cout<<"Case #"<<kase<<": ";
    if(n==0) {
            cout<<"INSOMNIA"<<endl;
    continue;
    }
    i=1;
    long long c;
    while(1)
    {
        c=n*i;
        if(c<0)
        {
             cout<<"INSOMNIA"<<endl;
            break;
        }
        fun(c);
        if(cnt==0)
        {
            cout<<c<<endl;
            break;
        }
        i++;
    }

    //cout<<"Case "<<kase<<": ";


}



return 0;
}
