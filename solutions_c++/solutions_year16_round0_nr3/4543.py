#include <bits/stdc++.h>
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define mp make_pair
#define pb push_back 
#define SET(a,b) memset(a,b,sizeof(a))
#define LET(x,a) __typeof(a) x(a)
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define sortv(a) sort(a.begin(),a.end())
#define test()  int t; cin>>t; while(t--)
#define fi first
#define se second
#define el "\n"
#define ll long long
#define ull unsigned ll
#define TRACE
using namespace std;

FILE *fin = freopen("input.txt","r",stdin);
FILE *fout = freopen("output.txt","w",stdout);

#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< PII > VPII;

#define MAXN 100009
const ll limit = 100000050;
 
vector<bool> prime(limit,true);
vector<int> primes;
void seive()
{
    for(ull i=2;i<limit;i++)
    {
        if(prime[i])
        {
            primes.pb(i);
            for(ull j=i*i;j<limit;j+=i)
            {
                prime[j]=false;
            }
        }
    }
    return;
}
typedef long double float64;

ull mul_mod(ull a, ull b, ull m){
   ull y = (ull)((float64)a*(float64)b/m+(float64)1/2);
   y = y * m;
   ull x = a * b;
   ull r = x - y;
   if ( (ll)r < 0 ){
      r = r + m; y = y - 1;
   }
   return r;
}

ull C,a,b;
ull gcd(){
   ull c;
   if(a>b){
      c = a; a = b; b = c;
   }
   while(1){
      if(a == 1LL) return 1LL;
      if(a == 0 || a == b) return b;
      c = a; a = b%a;
      b = c;
   }
}

ull f(ull a, ull b){
   ull tmp;
   tmp = mul_mod(a,a,b);
   tmp+=C; tmp%=b;
   return tmp;
}

ull pollard(ull n){
   if(!(n&1)) return 2;
   C=0;
   ull iteracoes = 0;
   while(iteracoes <= 1000){
      ull x,y,d;
      x = y = 2; d = 1;
      while(d == 1){
          x = f(x,n);
          y = f(f(y,n),n);
          ull m = (x>y)?(x-y):(y-x);
          a = m; b = n; d = gcd();
      }
      if(d != n)
          return d;
      iteracoes++; C = rand();
   }
   return 1;
}

ull pot(ull a, ull b, ull c){
   if(b == 0) return 1;
   if(b == 1) return a%c;
   ull resp = pot(a,b>>1,c);
   resp = mul_mod(resp,resp,c);
   if(b&1)
      resp = mul_mod(resp,a,c);
   return resp;
}

// Rabin-Miller primality testing algorithm
bool isPrime(ull n){
   ull d = n-1;
   ull s = 0;
   if(n <=3 || n == 5) return true;
   if(!(n&1)) return false;
   while(!(d&1)){ s++; d>>=1; }
   for(ull i = 0;i<32;i++){
      ull a = rand();
      a <<=32;
      a+=rand();
      a%=(n-3); a+=2;
      ull x = pot(a,d,n);
      if(x == 1 || x == n-1) continue;
      for(ull j = 1;j<= s-1;j++){
         x = mul_mod(x,x,n);
         if(x == 1) return false;
         if(x == n-1)break;
      }
      if(x != n-1) return false;
   }
   return true;
}
int main()
{
	ios::sync_with_stdio(false);
	int t,tt;
	seive();
	//cout<<sz(primes);
	cin>>tt;
	ull p[11][35];
	for(ull i=2;i<=10;i++)
	{
		p[i][0]=1;
		for(ll j=1;j<=18;j++)
			p[i][j]=p[i][j-1]*i;
	}
	ull arr[35];
	for(t=1;t<=tt;t++)
	{
		ull n,J;
		//n=16,J=50;
		cin>>n>>J;
		cout<<"Case #"<<t<<":"<<el;
		ull i,j,k;
		ull setsize=p[2][n];
		ull ans[11];
		ull c=1,f;
		for(i=setsize-1;i>=0 && c<=J;i--)
		{
			for(j=0;j<n;j++)
			{
				if(1<<j & i)
					arr[j]=1;
				else
					arr[j]=0;
			}
			if(arr[0]==0 || arr[n-1]==0)
				continue;
			f=0;
			for(j=2;j<=10;j++)
			{
				ll val=0;
				for(k=0;k<n;k++)
				{
					val+=p[j][n-k-1]*arr[k];
				}
				/*for(k=0;k<n;k++)
                    cout<<arr[k];
                cout<<el;
                trace3(n,j,val);
                */if(isPrime(val))
				{
					f=1;
					break;
				}
				else
				{
					for(int k=0;k<sz(primes);k++)
					{
						if(val!=primes[k] && val%primes[k]==0)
						{
							ans[j]=primes[k];
							break;
						}
					}
				}
			}
			if(f==1)
			{
				f=0;
				continue;	
			}
			else
			{
				for(j=0;j<n;j++)
					cout<<arr[j];
				for(j=2;j<=10;j++)
					cout<<" "<<ans[j];
				cout<<el;
				++c;
			}	
		}

	}	
	return 0;
}