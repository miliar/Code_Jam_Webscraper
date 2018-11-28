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

int main()
{
  int T;
  cin >> T;
  rep(t,T){
    string S;
    cin >> S;
    int res = 0;
    for(int i=0;i<S.size()-1;i++) if(S[i] != S[i+1]) res++;
    if(S[S.size()-1] == '-') res++;
    
    cout << "Case #" << t+1 << ": " << res << endl;
  }
  return 0;
}
