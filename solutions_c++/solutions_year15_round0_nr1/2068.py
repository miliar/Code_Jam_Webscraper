#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;
#define SZ(x) ( (int) (x).size() )
#define dbg(x) cerr << #x << " = " << x << endl;
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef long long ll;
typedef pair<int, int> pii;
// const int INF = 1e9;
// const int MAX_N = ;


int T;
int N;

int main(){
  scanf("%d", &T);
  for(int tc = 1; tc <= T; tc++){
    scanf("%d", &N);

    int x = 0, y, r = 0;
    for(int i = 0; i <= N; i++){
      scanf("%1d", &y);
      if(x < i){
	r += i - x;
	x = i;
      }
      x += y;
    }

    printf("Case #%d: %d\n", tc, r);
  }
  return 0;
}
