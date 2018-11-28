/*
 * Qualification-A
 * Google Code Jam
 *
 *  Created on: 11-04-15
 *      Author: sparks
 */
#include <bits/stdc++.h>
#define make_it_fast ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

typedef long long int ll;
typedef unsigned long long ull;

class TimeTracker {
  clock_t start, end;
public:
  TimeTracker() { start = clock(); }
  ~TimeTracker() { end = clock(); fprintf(stderr, "RunTime : %.3lf s\n", (double)(end - start) / CLOCKS_PER_SEC); }
};

#define ff first
#define ss second
#define pb push_back
#define mkp make_pair
#define mt make_tuple
#define pll pair<ll, ll>
#define loop(i, begin, end) for(__typeof(end) i=(begin)-((begin)>(end)); i!=(end)-((begin)>(end)); i+=1-2*((begin)>(end)))
#define rep(i,n) for(i=0;i<n;i++)
#define all(v) v.begin(), v.end()
#define db(args...) { vector<string> _v = split(#args, ','); debug_fn(_v.begin(), args); }
#define dbp(p) cerr << #p << " = " << '(' << p.ff << ',' << p.ss << ") " << endl;
#define dbn(A,N) for(int __I=0; __I<N; __I++) cerr << A[__I] << " \n"[__I==(N-1)];
#define dbnm(A,N,M) for(int __I=0; __I<N; __I++) { for(int __J=0; __J<M; __J++) cerr << A[__I][__J] << " \n"[__J==(M-1)]; }
#define dbv(v) for(auto __Velem : v) cerr << __Velem << ' '; cerr << endl;
#define dbvp(v) for(auto __Velem : v) cerr << '(' << __Velem.ff << ',' << __Velem.ss << ") " ; cerr << endl;

vector<string> split(const string& s, char c) 
{
  vector<string> v; stringstream ss(s); string x;
  while (getline(ss, x, c)) v.push_back(x);
  return v;
}

void debug_fn(vector<string>::iterator it) {}
template<typename T, typename... Args>
void debug_fn(vector<string>::iterator it, T a, Args... args) 
{
  cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
  debug_fn(++it, args...);
}

# define getcx getchar_unlocked

void inp() {}
template <typename T, typename... Args>
void inp(T& n, Args&... args)//fast input function
{
  int ch=getcx(), sign=1; n=0;
  while( ch < '0' || ch > '9' ) { if(ch=='-')sign=-1; ch=getcx(); }
  while( ch >= '0' && ch <= '9' ) n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
  n=n*sign; inp(args...);
}

void oup() {}
template <typename T, typename... Args>
void oup(T x, Args... args)
{ 
  if(x<0){ putchar('-'); x=-x; } int len=0,data[25];
  while(x) { data[len++]=x%10; x/=10; } if(!len) data[len++]=0;
  while(len--) putchar(data[len]+48); putchar('\n'); oup(args...);
}

#define N 1010
 
int main()
{ 
  #ifdef LOCAL
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    TimeTracker trk;
  #endif
  int t, n, nstand, nextra, sum[N];
  string s;
 
  cin >> t;
 
  for(int j = 1; j <= t; j++)
  {
    nstand = 0;
    nextra = 0;
 
    cin >> n;
    cin >> s;
 
    int i;
    for(i = 0; i <= n; i++)
      sum[i] = ( i == 0 ) ? ( s[i] - '0' ) : ( sum[i - 1] + ( s[i] - '0' ) );
 
    while(true)
    {
      // cout << "IN the loop" << endl;
      if( nstand >= n )
        break;
      else if ( nstand == sum[nstand] + nextra )
      {
        nextra += 1;
        nstand += 1;
      } else 
        nstand = sum[nstand] + nextra;
    }
 
    cout << "Case #" << j << ": " << nextra << endl;
  } 
 
  return 0;
}
 
// 75 7571698133379867048481685219960649908931489677371221509040137411303217565423