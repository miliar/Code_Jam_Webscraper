#include<bits/stdc++.h>
#define INF  INT_MAX  //infinity
#define NINF  INT_MIN //Negetive_infinity
#define MEM(a, b) memset(a, (b), sizeof(a))//memory initialisation
#define PI 3.1415926535897932384626
#define MOD 1000000007
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define MEM(a, b) memset(a, (b), sizeof(a))
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define PA(a,L,R) FOR(i,L,R,1) cout << a[i] << (i==R?'\n':' ')
#define P2A(a,N,M)FOR(i,0,N-1,1) FOR(j,0,M-1,1) cout << a[i][j] << ((j==M-1)?'\n':' ')
#define all(c) c.begin(), c.end()
#define PV(a) PA(a,0,a.size()-1)
#define gcd  __gcd
#ifndef ONLINE_JUDGE
#define gc getchar
#define pc putchar
#else
#define gc getchar_unlocked
#define pc putchar_unlocked
#endif
#define FOR(i, j, k, in) for (int i=j ; i<=k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define mp make_pair
#define pb push_back
using namespace std;
typedef long int ld;
typedef unsigned long int uld;
typedef long long int lld;
typedef unsigned long long int  ulld;
typedef pair<lld,lld> PII;
typedef vector<lld> VI;
typedef vector<string> VS;
typedef vector<PII> VII;
typedef vector<VI> VVI;
typedef map<int,int> MPII;
typedef set<int> SETI;
typedef multiset<int> MSETI;
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

template <class T>
inline T read()
{
    T n=0;
    bool sign=0;
    char p=gc();
    if(p=='-')
        sign=1;
    while((p<'0'||p>'9')&&p!=EOF&&p!='-')
        p=gc();
    if(p=='-')
        sign=1,p=gc();
    while(p>='0'&&p<='9') {
        n = (n<< 3) + (n<< 1) + (p - '0');
        p=gc();
    }
    if(sign)
        return -n;
    return n;
}
inline void readStr(char *str)
{
    register char c=0;
    register int i = 0;
    while (c < 33)
        c = gc();
    while (c > 65)
    {
        str[i] = c;
        c = gc();
        i = i + 1;
    }

    str[i] = '\0';
}
//Generic fast output function
template <class T> inline void write(T x)
{
    int i = 20;
    char buf[21];
    buf[20] = '\n';

    do
    {
        buf[--i] = x % 10 + '0';
        x/= 10;
    }while(x);
    do
    {
        pc(buf[i]);
    } while (buf[i++] != '\n');

}
int main()
{
    #ifndef ONLINE_JUDGE
       freopen("input.in","r",stdin);
       freopen("output.txt","w",stdout);
       #endif

    int t=read<int>();
    string digits[]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};

    FOR(i,0,t-1,1)
    {
    string l;
    int arr[10]={0};
    int count[26]={0};
    cin>>l;
    FOR(j,0,l.size()-1,1)
    {
      count[l[j]-65]+=1;
    }
    //zero
    int z=count[25];
    count[4]-=z;
    count[17]-=z;
    count[14]-=z;
    arr[0]=z;

    int u=count[20];
    count[5]-=u;
    count[14]-=u;
    count[17]-=u;
    arr[4]=u;
    int x=count[23];
    count[18]-=x;
    count[8]-=x;
    arr[6]=x;
    int g=count[6];
    count[4]-=g;
    count[8]-=g;
    count[7]-=g;
    count[19]-=g;
    arr[8]=g;
    int w=count[22];
    count[19]-=w;
    count[14]-=w;
    arr[2]=w;
    int o=count[14];
    count[13]-=o;
    count[4]-=o;
    arr[1]=o;
    int f=count[5];
    count[8]-=f;
    count[21]-=f;
    count[4]-=f;
     arr[5]=f;
    int s=count[18];
    count[4]-=2*s;
    count[21]-=s;
    count[13]-=s;
    arr[7]=s;
    int ii=count[8];
    arr[9]=ii;
    int h=count[7];
    count[19]-=h;
    count[17]-=h;
    count[4]-=2*h;
    arr[3]=h;
    cout<<"Case #"<<i+1<<": ";
    FOR(x,0,9,1)
    {

     FOR(n,1,arr[x],1)
     {
         cout<<x;
     }
    }
    cout<<"\n";

}
    return 0;

}



