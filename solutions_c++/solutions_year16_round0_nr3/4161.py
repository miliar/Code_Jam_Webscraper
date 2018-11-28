/*
     If opportunity doesn't knock, build a door.

            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |S|.|S|.|R|.|A|.|S|.|A|.|M|.|K|
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    Success is how high you bounce when you hit bottom.
*/


#include <bits/stdc++.h>

#define pii              pair <int,int>
#define pll              pair <long long,long long>
#define sc               scanf
#define pf               printf
#define Pi               2*acos(0.0)
#define ms(a,b)          memset(a, b, sizeof(a))
#define pb(a)            push_back(a)
#define MP               make_pair
#define db               double
#define ll               long long
#define EPS              10E-10
#define ff               first
#define ss               second
#define sqr(x)           (x)*(x)
#define D(x)             cout<<#x " = "<<(x)<<endl
#define VI               vector <int>
#define DBG              pf("Hi\n")
#define MOD              1000000007
#define CIN              ios_base::sync_with_stdio(0); cin.tie(0)
#define SZ(a)            (int)a.size()
#define sf(a)            scanf("%d",&a)
#define sfl(a)           scanf("%lld",&a)
#define sff(a,b)         scanf("%d %d",&a,&b)
#define sffl(a,b)        scanf("%lld %lld",&a,&b)
#define sfff(a,b,c)      scanf("%d %d %d",&a,&b,&c)
#define sfffl(a,b,c)     scanf("%lld %lld %lld",&a,&b,&c)
#define stlloop(v)       for(__typeof(v.begin()) it=v.begin();it!=v.end();it++)
#define loop(i,n)        for(int i=0;i<n;i++)
#define REP(i,a,b)       for(int i=a;i<b;i++)
#define RREP(i,a,b)      for(int i=a;i>=b;i--)
#define TEST_CASE(t)     for(int z=1;z<=t;z++)
#define PRINT_CASE       printf("Case #%d:\n",z)
#define CASE_PRINT       cout<<"Case "<<z<<": "
#define all(a)           a.begin(),a.end()
#define intlim           2147483648
#define infinity         (1<<28)
#define ull              unsigned long long
#define gcd(a, b)        __gcd(a, b)
#define lcm(a, b)        ((a)*((b)/gcd(a,b)))

using namespace std;


/*----------------------Graph Moves----------------*/
//const int fx[]={+1,-1,+0,+0};
//const int fy[]={+0,+0,+1,-1};
//const int fx[]={+0,+0,+1,-1,-1,+1,-1,+1};   // Kings Move
//const int fy[]={-1,+1,+0,+0,+1,+1,-1,-1};  // Kings Move
//const int fx[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int fy[]={-1,  1, -2,  2, -2,  2, -1,  1}; // Knights Move
/*------------------------------------------------*/

/*-----------------------Bitmask------------------*/
//int Set(int N,int pos){return N=N | (1<<pos);}
//int reset(int N,int pos){return N= N & ~(1<<pos);}
bool check(int N,int pos)
{
    return (bool)(N & (1<<pos));
}
/*------------------------------------------------*/

int mm=100000005;

bool prime[100000005];
vector<int>primes;
void sieve()
{
    prime[0]=prime[1]=1;
    for(int i=2; i<mm;)
    {
        primes.pb(i);
        for(int j=i+i; j<mm; j+=i)
            prime[j]=1;
        for(++i;; i++)
            if(prime[i]==0) break;
    }
}

ll bigmod(int n, int pow)
{
    if(pow==0)return 1;
    if(pow==1) return n;

    ll ret=0;

    if(pow % 2==0)
    {
        ret=bigmod(n,pow/2);
        return ret*ret;
    }
    else
        return ret=n*bigmod(n,pow-1);
}

int main()
{

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    sieve();
//    D(SZ(primes));

    int cnt=0;
    int t;
    sf(t);
    TEST_CASE(t)
    {
//    vector<string> ans;
        int nn,kk;
        sff(nn,kk);
        cnt=kk;
        PRINT_CASE;
        for(int i=(1<<nn-1)+1; i<=(1<<nn)-1; i+=2)
        {
//        D(i);
            vector<int>v;
            string str;

            bool test=0;
            int ccnt=2;
            for(int k=2; k<=10; k++)
            {
                if(ccnt!=k) break;
                ll sum=0;
                loop(j,16)
                {
                    if(test==0)
                        str+=check(i,j)+'0';
                    if(check(i,j)) sum+=bigmod(k,j);
                }

                test=1;
                ll xxx=sqrt(sum);
                for(int l=0; primes[l]<=xxx; l++)
                {
                    if(sum%primes[l]==0)
                    {
                        ccnt++;
                        v.pb(primes[l]);
                        break;
                    }
                }

            }
            if(SZ(v)==9)
            {
                reverse(all(str));
                cout<<str;
                loop(l,9) cout<<" "<<v[l];
                cnt--;
                cout<<endl;
            }


            v.clear();
            str.clear();

            if(cnt==0) break;

        }
    }
    return 0;
}



