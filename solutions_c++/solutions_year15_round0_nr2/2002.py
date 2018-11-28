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
const int INF = 1e9;
const int MAX_N = 1001;

int T;
int N;
int A[MAX_N];

int main(){
  scanf("%d", &T);
  
  for(int tc = 1; tc <= T; tc++){
    scanf("%d", &N);
    for(int i = 0; i < N; i++)
      scanf("%d", A + i);

    int res = INF;
    for(int i = 1; i < MAX_N; i++){
      int s = i;
      for(int j = 0; j < N; j++)
	s += max(0, (A[j] - 1) / i);
      if(res > s){
	res = s;
      }
    }
    
    printf("Case #%d: %d\n", tc, res);
  }
  return 0;
}
