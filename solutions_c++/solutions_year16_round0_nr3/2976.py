#include<bits/stdc++.h>

#define pb push_back
#define len(n) n.length()
#define mp make_pair
#define forp(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,n)    for(LL i=0;i<n;i++)
#define ren(i,n)    for(LL i=n-1;i>=0;i--)
#define forn(i,a,b) for(int i=a;i>=b;i--)
#define fre     freopen("0.in","r",stdin),freopen("0.out","w",stdout)
#define ff first
#define ss second
#define pll pair<long long int,long long int>
#define vll vector<long long int>
#define gll(n) scanf("%lld",&n)
#define gstr(n) scanf("%s",n)
#define gl(n) cin >> n
#define g2(m,n) cin >> m >> n
#define oi(n) printf("%d",n)
#define oll(n) printf("%lld",n)
#define onn printf("\n")
#define ostr(n) printf("%s",n)
#define os(n) cout << n
#define os cout<<" "
#define on cout<<"\n"
#define o2(a,b) cout<<a<<" "<<b
#define all(n) n.begin(),n.end()
#define alll(n,i,j) n.begin()+i,n.begin()+j
#define present(s,x) (s.find(x) != s.end())
#define cpresent(s,x) (find(all(s),x) != s.end())
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL)
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define mem(n,m) memset(n,m,sizeof(n))
#define bitc(n) __builtin_popcount(n)
#define MOD 1000000007
#define mod2 1000000009
#define ma(m,n) m = max(m,n)
#define mi(m,n) m = min(m,n)
#define EPSILON 1e-6
#define PI 3.14159265358979323846

#define TRACE

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
using namespace std;
typedef unsigned long long int ull;
typedef long long int LL;
typedef vector<vector<LL> > mat;
//#define N 100005
#define LD              long double

map < long long , int> Factor;
long long pw[11][20];
bool mark[20005];

LL mulmod(LL a,LL b, LL m){LL q=(LL)(((LD)a*(LD)b)/(LD)m);LL r=a*b-q*m;if(r>m)r%=m;if(r<0)r+=m;return r;}
template <typename T> T mod(T a, T b) {return (a < b ? a : a % b);}
template <typename T>T expo(T e, T n){T x=1,p=e;while(n){if(n&1)x=x*p;p=p*p;n>>=1;}return x;}
template <typename T>T power(T e, T n, T m){T x=1,p=e;while(n){if(n&1)x=mulmod(x,p,m);p=mulmod(p,p,m);n>>=1;}return x;}
template <typename T> T gcd(T a, T b){if(a%b) return gcd(b,a%b);return b;}
template <typename T> T lcm(T a, T b){return (a*(b/gcd(a,b)));}

bool isprime(LL p, int base)
{
    if (p<2)                return false;
    if (p!=2 && p%2==0)     return false;
    if (p<8)                return true;
    LL s = p-1, val = p-1, a, m, temp;
    while (s%2==0)
        s/=2;
    for (int i=0; i<10; ++i)
    {
        a = 1LL*rand()%val + 1LL;
        temp = s;
        m = power(a, temp, p);
        while (temp!=(p-1) && m!=1 && m!=(p-1))
        {
            m = mulmod(m, m, p);
            temp<<=1;
        }
        if (m!=(p-1) && temp%2==0)    return false;
    }
    return true;
}

long long get (int mask, int base, int N) {
  long long number = pw[base][N-1] + 1;
  rep (i,N-2) {
    if (mask & (1 << i)) {
      number += pw[base][i+1];
    }
   }
  return number;
}

long long factor (LL num) {
  if (Factor[num]) {
    return Factor[num];
  }
  for (long long i = 2; i * i <= num; i++) {
    if (num % i == 0) {
       Factor[num] = i;
       return i;
    }
  }
}

int main () {
 freopen("C-small-attempt0.in","r",stdin),freopen("op.out","w",stdout);
 forp (i,2,10) {
 	pw[i][0] = 1;
 	forp (j,1,16) {
 	  pw[i][j] = 1ll * pw[i][j-1] * i;
	}
 }
 int t;
 cin >> t;
 forp (TT,1,t) {
 	vector <long long> prime;
 	int N,J;
 	cin >> N >> J;
    int mx = pw[2][N-2];
	rep (mask, mx) {
      int num = pw[2][N-1] + 1;
      rep (i,N-2) {
      	if (mask & (1 << i)) {
		  num += pw[2][i+1];
		}
	  }
	  if (isprime(num, 2) == false) {
	  	prime.pb(mask);
	  }
	}
	mem(mark, true);
	forp (base,3,10) {
	  int k = 0;
	  for (auto mask : prime) {
	    if (mark[k] == false) {
	      k++;
	      continue;
	    }
	  	long long num = pw[base][N-1] + 1;
	  	rep (i, N-2) {
		 if (mask & (1 << i)) {
		   num += pw[base][i+1];
		 }
		}
	  	if(isprime(num, base)) {
	  	  mark[k] = false;
	  	}
	  	k++;
	  }
	}
  	cout << "Case #" << TT << ":\n";
  	int k = 1, e = 0;
  	for (auto mask : prime) {
  	  if (!mark[e++]) continue;
  	  cout << 1;
  	  ren (i,N-2) {
  	    cout << (mask & (1 << i) ? 1 : 0);
  	  }
  	  cout << 1 << " ";
  	  forp (base,2,10) {
  	    long long number = get(mask, base, N);
  	    cout << factor(number) << " ";
  	  }
  	  ++k;
  	  if (k > J) break;
  	  cout << "\n";
	}
	cout << "\n";
 }
 return 0;
}
