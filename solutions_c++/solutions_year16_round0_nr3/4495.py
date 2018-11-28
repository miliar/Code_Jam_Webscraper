#include <bits/stdc++.h>
using namespace std;


const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
const double PI=acos(-1.0);

#define    READ(f) 	         freopen(f, "r", stdin)
#define    WRITE(f)   	     freopen(f, "w", stdout)

#define    m_p(x, y) 	     make_pair(x, y)
#define    p_b(x)             push_back(x)

#define    rep(i,n)         for(i=1;i<=n;i++)
#define    rep0(i,n)         for(i=0;i<n;i++)


#define    SET(p) 	         memset(p, -1, sizeof(p))
#define    CLR(p)            memset(p, 0, sizeof(p))
#define    MEM(p, v)         memset(p, v, sizeof(p))
#define    CPY(d, s)         memcpy(d, s, sizeof(s))

#define    getI(a) 	         scanf("%d", &a)
#define    getII(a,b) 	     scanf("%d%d", &a, &b)
#define    getIII(a,b,c)     scanf("%d%d%d", &a, &b, &c)
#define    getL(a)           scanf("%lld",&a)
#define    getLL(a,b)        scanf("%lld%lld",&a,&b)
#define    getLLL(a,b,c)     scanf("%lld%lld%lld",&a,&b,&c)
#define    getC(n)           scanf("%c",&n)
#define    getF(n)           scanf("%lf",&n)
#define    getS(n)           scanf("%s",n)

#define    vi 	 vector < int >
#define    vii 	 vector < vector < int > >
#define    pii 	 pair< int, int >
#define    ff 	 first
#define    ss 	 second
#define    ll	 long long
#define    ull 	 unsigned long long
#define    ui    unsigned int


template< class T > inline T _abs(T n) { return ((n) < 0 ? -(n) : (n)); }
template< class T > inline T _max(T a, T b) { return (!((a)<(b))?(a):(b)); }
template< class T > inline T _min(T a, T b) { return (((a)<(b))?(a):(b)); }
template< class T > inline T _swap(T &a, T &b) { a=a^b;b=a^b;a=a^b;}
template< class T > inline T gcd(T a, T b) { return (b) == 0 ? (a) : gcd((b), ((a) % (b))); }
template< class T > inline T lcm(T a, T b) { return ((a) / gcd((a), (b)) * (b)); }


//******************DELETE****************

#ifdef rafsan_rana
     #define debug(args...) {cerr<<"Debug: "; dbg,args; cerr<<endl;}
#else
    #define debug(args...)  // Just strip off all debug tokens
#endif

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

int bitOn(int N,int pos)
{
    return N=N | (1<<pos);
}
int bitOff(int N,int pos)
{
    return N=N & ~(1<<pos);
}
bool bitCheck(int N,int pos)
{
    return (bool)(N & (1<<pos));
}

ll int poww(ll int x, ll int y)
{
    ll int temp=1;
    for(ll int i=1;i<=y;i++)
    {
        temp*=x;
    }

    return temp;
}

int cc=0;


ll int conv(ll int i, ll int j)
{
    ll int temp=0;
    ll int p=0;
    while(i!=0)
    {
        ll int rem = i%10;

        temp+= poww(j,p)*rem;

        p++;
        i/=10;
    }

   // cout<<temp<<endl;

    int f=0;

    ll int sq = sqrt(temp);
    for(ll int ii=2;ii<=sq;ii++)
    {
        if(temp%ii==0)
        {
            f=1;
            return ii;
        }
    }

   // cout<<i<<" "<<temp<<" "<<j<<endl;

    if(f==0) return -1;
}























int main()
{

   //freopen("out.txt","w",stdout);

    int t;
    getI(t);
    int n,j;
    getII(n,j);

    cout<<"Case #1:"<<endl;

    int countt=0;

     vector<ll int> vec;

     for(ll int i=1000000000000001;i<=1111111111111111;i++)
     {
         int rem = i%10;
         if(rem!=1) continue;
         ll int temp =i;
       //  cout<<i<<endl;
         int dd=0;
         while(temp!=0)
         {
             int remtem = temp%10;
             if(remtem!=0 && remtem!=1)
             {
                 dd=1;
                 break;
             }

             temp/=10;
         }


         if(dd) continue;

       //  cout<<i<<endl;



        int ff=0;

                 vec.clear();

        for(int k=2;k<=10;k++)
        {
            ll int r = conv(i,k);

            if(r!=-1) vec.p_b(r);
            else
            {
                ff=1;
                break;
            }
        }

        if(ff) continue;

         cout<<i<<" ";
         for(int pp=0;pp<8;pp++) cout<<vec[pp]<<" ";
         cout<<vec[8];
         cout<<endl;
         countt++;
         if(countt==50) break;

         vec.clear();
     }


    // cout<<"End"<<endl;


}
