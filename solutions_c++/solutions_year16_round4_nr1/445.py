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
int n;
int r,p,s;
string kosong = "";

string hasil(char x,int rem)
{
  if (rem == 0) return kosong + x;
  string a, b;
  if (x == 'P') 
  {
    a = hasil('P',rem-1);
    b = hasil('R',rem-1);
  }
  if (x == 'R') 
  {
    a = hasil('S',rem-1);
    b = hasil('R',rem-1);
  }
  if (x == 'S') 
  {
    a = hasil('S',rem-1);
    b = hasil('P',rem-1);
  }
  return min(a,b) + max(a,b);
}

bool cek(string S)
{
  int R = 0;
  int P = 0;
  int SS = 0;
  REP(i,SIZE(S))
  {
    if (S[i] == 'R') ++R;
    if (S[i] == 'P') ++P;
    if (S[i] == 'S') ++SS;
  }
  return r == R && p == P && s == SS;
}

int main()
{
	scanf("%d", &T);
  REPN(cases,T)
  {
    scanf("%d %d %d %d",&n,&r,&p,&s);
    printf("Case #%d: ", cases);
    string S = hasil('P',n);
    string T = hasil('S',n);
    string U = hasil('R',n);
    if (cek(S)) printf("%s\n",S.c_str());
    else if (cek(T)) printf("%s\n",T.c_str());
    else if (cek(U)) printf("%s\n",U.c_str());
    else puts("IMPOSSIBLE");
  }
	return 0;
}
















