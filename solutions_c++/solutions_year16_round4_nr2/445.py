//start of jonathanirvings' template v3.0.0 (BETA)

#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
typedef pair<string,string> pss;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vii;
typedef vector<LL> vl;
typedef vector<vl> vvl;

double EPS = 1e-9;
int INF = 1000000005;
long long INFF = 1000000000000000005LL;
double PI = acos(-1);
int dirx[8] = {-1,0,0,1,-1,-1,1,1};
int diry[8] = {0,1,-1,0,-1,1,-1,1};

#ifdef TESTING
  #define DEBUG fprintf(stderr,"====TESTING====\n")
  #define VALUE(x) cerr << "The value of " << #x << " is " << x << endl
  #define debug(...) fprintf(stderr, __VA_ARGS__)
#else
  #define DEBUG 
  #define VALUE(x)
  #define debug(...)
#endif

#define FOR(a,b,c) for (int (a)=(b);(a)<(c);++(a))
#define FORN(a,b,c) for (int (a)=(b);(a)<=(c);++(a))
#define FORD(a,b,c) for (int (a)=(b);(a)>=(c);--(a))
#define FORSQ(a,b,c) for (int (a)=(b);(a)*(a)<=(c);++(a))
#define FORC(a,b,c) for (char (a)=(b);(a)<=(c);++(a))
#define REP(i,n) FOR(i,0,n)
#define REPN(i,n) FORN(i,1,n)
#define MAX(a,b) a = max(a,b)
#define MIN(a,b) a = min(a,b)
#define SQR(x) ((x) * (x))
#define RESET(a,b) memset(a,b,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ALL(v) v.begin(),v.end()
#define ALLA(arr,sz) arr,arr+sz
#define SIZE(v) (int)v.size()
#define SORT(v) sort(ALL(v))
#define REVERSE(v) reverse(ALL(v))
#define SORTA(arr,sz) sort(ALLA(arr,sz))
#define REVERSEA(arr,sz) reverse(ALLA(arr,sz))
#define PERMUTE next_permutation
#define TC(t) while(t--)

inline string IntToString(LL a){
  char x[100];
  sprintf(x,"%lld",a); string s = x;
  return s;
}

inline LL StringToInt(string a){
  char x[100]; LL res;
  strcpy(x,a.c_str()); sscanf(x,"%lld",&res);
  return res;
}

inline string GetString(void){
  char x[1000005];
  scanf("%s",x); string s = x;
  return s;
}

inline string uppercase(string s){
  int n = SIZE(s); 
  REP(i,n) if (s[i] >= 'a' && s[i] <= 'z') s[i] = s[i] - 'a' + 'A';
  return s;
}

inline string lowercase(string s){
  int n = SIZE(s); 
  REP(i,n) if (s[i] >= 'A' && s[i] <= 'Z') s[i] = s[i] - 'A' + 'a';
  return s;
}

inline void OPEN (string s) {
  freopen ((s + ".in").c_str (), "r", stdin);
  freopen ((s + ".out").c_str (), "w", stdout);
}

//end of jonathanirvings' template v3.0.0 (BETA)

int T;
double data[205];
double dp[205][205];
bool sudah[205][205];
int n,k;
vector<int> c;
double risan;

double jahja(int now,int win,int lost)
{
  if (now == k)
  {
    return (win == 0 && lost == 0 ? 1 : 0);
  }
  double &ret = dp[win][lost];
  if (sudah[win][lost]) return ret;
  ret = 0;
  sudah[win][lost] = 1;
  if (win > 0) 
    ret += jahja(now + 1,win-1,lost) * data[c[now]];
  if (lost > 0)
    ret += jahja(now + 1,win,lost-1) * (1-data[c[now]]);
  return ret;
}

void coba()
{
  RESET(sudah,0);
  assert(SIZE(c) == k);
  MAX(risan,jahja(0,k/2,k/2));
}

int main()
{
	scanf("%d", &T);
  REPN(cases,T)
  {
    printf("Case #%d: ", cases);
    scanf("%d %d",&n,&k);
    REP(i,n) scanf("%lf",&data[i]);
    SORTA(data,n);
    risan = 0;
    REP(i,n)
    {
      c.clear();
      REP(j,k) c.pb((i+j)%n);
      coba();
    }
    /*c.clear(); REP(i,k) c.pb(i);
    coba();
    c.clear(); REP(i,k) c.pb(n-1-i);
    coba();
    c.clear(); REP(i,k/2) c.pb(i); REP(i,k/2) c.pb(n-1-i);
    coba();*/
    printf("%.9lf\n",risan);
  }
	return 0;
}
















