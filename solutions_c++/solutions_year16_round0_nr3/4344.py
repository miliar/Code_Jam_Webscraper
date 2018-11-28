#include<bits/stdc++.h>
using namespace std;

#define FOR(i, a, b) for(int i=a; i<=b; i++)
#define DOW(i, a, b) for(int i=a; i>=b; i--)
#define S(a)  scanf("%d",&a)
#define LS(a) scanf("%lld",&a)
#define SS(s) scanf("%s",s)
#define DS(a) scanf("%lf",&a)
#define PC(a) printf("Case %d: ",a)
#define P(a) printf("%d\n",a)
#define LP(a)  printf("%lld",a)
#define DP(a) printf("%.04lf",a)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi   first
#define se     second
#define fast std::ios::sync_with_stdio(false),cin.tie(0)
#define init freopen("input.txt","r",stdin)
#define outit freopen("output.txt","w",stdout)
#define INF 0xfffffff
#define gc getchar
#define MOD 1000000007

typedef long long ll;
typedef vector<ll> vi;
typedef pair<int,int> ii;
typedef vector<ii>  vii;
typedef vector<vector<int>> vvi;
typedef vector<vector<ii>> vvii;

inline void read(int &x)
{

    x=0;
    register char c=gc();
    for(; c<'0' || c>'9'; c=gc());
    for(; c>='0' && c<='9'; c=gc())
        x=(x<<3)+(x<<1)+(c-'0');
}
inline void write(int x)
{

    register char buffor[35];
    register int i=0;
    do
    {
        buffor[i++]=(x%10)+'0';
        x/=10;
    }
    while(x);
    i--;
    while(i>=0) putchar(buffor[i--]);
    putchar('\n');
}

// simple implementaion of sieve taken from book competitive programming 3 by Steven Halim


ll _sieve_size;
bitset<100000010> bs;
vi primes;


// first part

void sieve(ll upperbound)
{
    _sieve_size = upperbound + 1;
    bs.set();
    bs[0] = bs[1] = 0;
    for (ll i = 2; i <= _sieve_size; i++) if (bs[i])
        {

            for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
            primes.push_back(i);
        }
}

bool isPrime(ll N)
{
    if (N <= _sieve_size) return bs[N];
    for (int i = 0; i < (int)primes.size(); i++)
        if (N % primes[i] == 0) return false;
    return true;
}




int main()
{
    init;
    outit;
    sieve(100000010);
    int t;
    S(t);
    for(int tc=1; tc<=t; tc++)
    {
        ll n,j;
        LS(n),LS(j);
        printf("Case #%d:\n",tc);

        string s(n,'0');
        s[n-1]='1';
        s[0]='1';
        string anss;

        FOR(h,0,j-1)
        {

           //cout<<"line "<<h+1<<" ";
            vector<ll> a(10,0);
            int cnt=0;
            while(1)
            {
                //cout<<cnt++<<"\n";
             //   cout<<s<<"Y\n";
                bool ans=true;
                a.assign(10,0);
                for(int i=0; i<n; i++)
                {
                    for(int f=0; f<9; f++)
                    {
                        a[f]= a[f]*(f+2)+ s[i]-'0';


                    }


                }

                for(int i=0; i<9; i++)
                {
                    if(isPrime(a[i]))
                        ans=false;


                }
                if(ans) anss=s;
                int carry =s[n-2]=='0'?0:1;
                s[n-2]=s[n-2]=='0'?'1':'0';
                for(int i=n-3; i>=0; i--)
                {
                    if(s[i]=='0' && carry)
                    {
                        s[i]='1';
                        carry=0;

                    }
                    else if(s[i]=='1' and carry)
                    {
                        s[i]='0';
                        carry=1;


                    }


                }
                if(ans) break;

            }

            vi fct;
            for(int i=0; i<9; i++)
            {
                // if(!isPrime(a[i]))
              //  cout<<a[i]<<" \n";
                {
                    for(int f=0; f<primes.size(); f++)
                    {
                        if(a[i] %primes[f]==0)
                        {

                            fct.pb(primes[f]);
                            break;

                        }


                    }

                }



            }
            cout<<anss<<" ";
            for(int i=0; i<9; i++)
            {
                if(i==8)
                    cout<<fct[i]<<"\n";
                else   cout<<fct[i]<<" ";


            }



        }


    }

    return 0;

}
