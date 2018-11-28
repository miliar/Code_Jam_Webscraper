#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <algorithm>

using namespace std;

#define rep(i,j) REP((i), 0, (j))
#define REP(i,j,k) for(int i=(j);(i)<(k);++i)
#define BW(a,x,b) ((a)<=(x)&&(x)<=(b))
#define ALL(v) (v).begin(), (v).end()
#define LENGTHOF(x) (sizeof(x) / sizeof(*(x)))
#define AFILL(a, b) fill((int*)a, (int*)(a + LENGTHOF(a)), b)
#define SQ(x) ((x)*(x))
#define Mod(x, mod) (((x)+(mod)%(mod))
#define MP make_pair
#define PB push_back
#define Fi first
#define Se second
#define INF (1<<29)
#define EPS 1e-10
#define MOD 1000000007

typedef pair<int, int> pi;
typedef pair<int, pi> pii;
typedef vector<int> vi;
typedef queue<int> qi;
typedef long long ll;

int T;
int ex[5][5]={ {0,0,0,0,0},
	       {0,1,2,3,4},
	       {0,2,-1,4,-3},
	       {0,3,-4,-1,2},
	       {0,4,3,-2,-1} };

int toInteger(char c)
{
  return c=='i'?2:c=='j'?3:4;
}

int expr(int a, int b)
{
  int ret = 0;
  int negative = 0;
  if(a < 0){ negative++; a *= -1;}
  if(b < 0){ negative++; b *= -1;}
  /*  if(a==b) ret = -1;
  else if(a == 1 || b == 1) ret = a*b;
  else if(a == 2 && b == 3) ret = 4;
  else if(a == 2 && b == 4) ret = -3;
  else if(a == 3 && b == 2) ret = -4;
  else if(a == 3 && b == 4) ret = 2;
  else if(a == 4 && b == 2) ret = 3;
  else ret = -2;*/
  ret = ex[a][b];
  if(negative&1) ret *= -1;
  
  return ret;
}

int expr2(int a, int c)
{
  int ret = 0;
  int negative = 0;
  if(a<0){ negative++; a *= -1;}
  for(int i=1;i<=4;i++){
    if(ex[a][i] == c) ret = i;
    if(ex[a][i] == -1*c){
      if(negative) ret = i;
      else ret = -1*i;
    }
  }
  return ret;  
}

int judge(string s)
{
  //  cout << s << endl;
  int x = 1;
  for(int i=0;i<s.size();i++){
    x = expr(x, toInteger(s[i]));
    //    printf("x %d\n", x);
    if(x == 2){
      int y = 1;
      int z = 1;
      for(int j=i+1;j<s.size();j++) z = expr(z, toInteger(s[j]));
      for(int j=i+1;j<s.size();j++){
	y = expr(y, toInteger(s[j]));
	z = expr2(toInteger(s[j]), z);
	//	printf("y %d z %d\n", y, z);
	if(y == 3 && z == 4) return 1;
      }
    }
  }
  return 0;
}

int main()
{
  scanf("%d", &T);
  for(int tcase=1;tcase<=T;tcase++){
    string ss, s;
    int X,L;
    scanf("%d%d", &X, &L);
    cin >> ss;
    rep(i, L) s += ss;
    int res = judge(s);
    printf("Case #%d: %s\n", tcase, res?"YES":"NO");
  }
  return 0;
}
