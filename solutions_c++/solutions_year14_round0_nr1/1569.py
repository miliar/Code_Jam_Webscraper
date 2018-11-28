#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <string>
#include <functional>
#include <utility>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

void print_vector(vi v);
void print_array(int* array, int start, int end);

#define FOR(i,a,b) for (int i = (a),_b = (b); i < _b; i++)
#define DOW(i,b,a) for (int i = (b),_a = (a); i > _a; i--)
#define fill(a,v) memset(a, v, sizeof a)
#define checkbit(n,b) ((n >> b) & 1)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

int tc;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int cse = 1;
    s(tc);
    int n, m, cards[10][10];
    set<int> trick;
    while(tc--){
      s(n);
      trick.clear();
      FOR(i, 0, 4)FOR(j, 0, 4){
        s(cards[i][j]);
      }
      FOR(i, 0, 4){ trick.insert(cards[n-1][i]);}
      s(m);
      FOR(i, 0, 4)FOR(j, 0, 4){
        s(cards[i][j]);
      }
      int ans = 0, ans2 = 0;
      FOR(i, 0, 4){
        if(trick.count(cards[m-1][i]) > 0) ans++, ans2 = cards[m-1][i];
      }
      printf("Case #%d: ", cse++);
      if(ans == 1) printf("%d\n", ans2);
      else if (ans == 0) printf("Volunteer cheated!\n");
      else printf("Bad magician!\n");

    }
    return 0;
}

void print_array(int* array, int start, int end){
  printf("[");
  FOR(i, start, end){
    printf("%d ", array[i]);
  }
  printf("]");
  printf("\n");
}

void print_vector(vi v){
  printf("[");
  FOR(i, 0, v.size()){
    printf("%d ", v[i]);
  }
  printf("]");
  printf("\n");
}