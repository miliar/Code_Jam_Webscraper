#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define pb              push_back
#define sz              size
#define PII             pair <int,int>
#define PLL             pair <ll,ll>
#define mp              make_pair
#define xx              first
#define yy              second
#define all(v)          v.begin(),v.end()

#define CLR(a)          memset(a,0,sizeof(a))
#define SET(a)          memset(a,-1,sizeof(a))

#define E               2.718281828459045235360287471352
#define eps             1e-9
#define mod             1000000000000000000

/******************************************************************************************/

#define N 100000100

bool numbers[N+10];
vector <ll> primes;

void sieve()
{
    numbers[0]=numbers[1] = 1;
    ll i,j,k;
    for(i=4;i<=N;i+=2) numbers[i]=1;
    for(i=3;i<=sqrt(N);i+=2)
        if(!numbers[i])
            for(j=i*i;j<=N;j+=(i+i)) numbers[j] = 1;

    for(i=2;i<=N;i++)
        if(!numbers[i]) primes.pb(i);
}

ll bigMod(ll a,ll b,ll m)
{
    if(b==0) return 1;
    ll ret = bigMod(a,b/2,m);
    ret *= ret;
    ret %= m;
    if(b%2) ret *= a;
    return ret%m;
}


bool isPrime(ll n)
{
    if(n<=100000000) return !numbers[n];
    else{
        for(ll i=0;primes[i]<=sqrt(n);i++){
            if(n%primes[i]==0) return 0;
        }
        return 1;
    }
}

string intToStr(ll n,ll s)
{
    string str = "";
    str += "1";
    while(n){
        if(n%2) str = "1" + str;
        else str = "0" + str;
        n /= 2;
    }
    while(str.size()!=s-1){
        str = "0" + str;
    }
    str = "1" + str;
    return str;
}

vector <ll> v,d;
string str;

int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    sieve();
    ll T,t,n,k,cnt = 0,m,mask,i,num,j;
    bool fg;
    cin >> T;
    cin >> n >> k;
    mask = 1 <<(n-2);
    cout << "Case #1:\n";
    for(ll b = 0;b<mask;b++){
        str = intToStr(b,n);
        reverse(str.begin(),str.end());
        fg = 1;
        v.clear();
        for(i=2;i<=10;i++){
            num = 0;
            for(j=0;j<n;j++){
                num += (str[j]-48)*bigMod(i,j,mod);
            }
            v.pb(num);
            if(isPrime(num)){
                fg = 0;
                break;
            }
        }
        reverse(str.begin(),str.end());
        if(fg){
            cnt++;
            d.clear();
            for(i=0;i<v.size();i++){
                for(j=0;;j++){
                    if(v[i] % primes[j]==0){
                        d.pb(primes[j]);
                        break;
                    }
                }
            }
            cout << str << " ";
            for(i=0;i<d.size()-1;i++) cout << d[i] << " ";
            cout << d[d.size()-1] << endl;
        }
        if(cnt==k) break;
    }
    return 0;
}
