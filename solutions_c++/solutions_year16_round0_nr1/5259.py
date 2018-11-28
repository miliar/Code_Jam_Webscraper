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
typedef vector<int> vi;
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



int main()
{
    init;
    outit;

    int t;
    S(t);
    for(int tc=1; tc<=t; tc++)
    {

        ll n;
        LS(n);
        printf("Case #%d: ",tc);
        if(!n) printf("INSOMNIA\n");
        else
        {
            set<ll> a;
            ll k=n;
            ll i=1;
            while(1)
            {
                //cout<<k<<"\n";
                while(k)
                {
                    a.insert(k%10);

                    k=k/10;



                }
                if((int)a.size()==10) break;

                i++;
                k=i*n;



            }

            printf("%lld\n",n*(i));





        }


    }

    return 0;

}
