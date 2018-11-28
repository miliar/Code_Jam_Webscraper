#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;

void print_vector(vi v);
void print_array(int* array, int start, int end);

#define FOR(i,a,b) for (int i = (a),_b = (b); i < _b; i++)
#define DOW(i,b,a) for (int i = (b),_a = (a); i >= _a; i--)
#define fill(a,v) memset(a, v, sizeof a)
#define checkbit(n,b) ((n >> b) & 1)
#define pb(a) push_back(a)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()

#define INF 1e9
#define PI acos(-1.0)

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

int tc, cse = 1, r, c;
int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
string maze[140];

bool valid(int x, int y){
  return x >= 0 && x < r && y >= 0 && y < c;
}

int main() {
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif 

  s(tc);
  while(tc--){
    cin >> r >> c;
    FOR(i, 0, r) cin >> maze[i];
    int ans = 0;
    FOR(i, 0, r) FOR(j, 0, c){
      if(maze[i][j] == '.') continue;
      else {
        // check neighbour
       // printf("Current %d %d\n", i, j);
        bool fail = true;
        FOR(d, 0, 4){
          int x = i+dir[d][0], y = j + dir[d][1];
          //printf("%d %d\n", x, y);
          while(valid(x, y)){
            if(maze[x][y] != '.') {fail = false;
              break;
            } else {
              x = x+dir[d][0], y = y + dir[d][1];
            }
          }
          if(!fail) break;
        }
        if(fail){
          printf("Case #%d: IMPOSSIBLE\n", cse++);
          goto hell;
        } else {
          int d = 0;
          if(maze[i][j] == '^') d = 0;
          else if (maze[i][j] == '>') d = 1;
          else if (maze[i][j] == 'v') d = 2;
          else d = 3;
          bool fail = true;
          int x = i+dir[d][0], y = j + dir[d][1];
          while(valid(x, y)){
            if(maze[x][y] != '.') { fail = false;
              break;
            } else {
              x = x+dir[d][0], y = y + dir[d][1];
            }
          }
          if(fail) ans++;
        }
      }
    }
    printf("Case #%d: %d\n", cse++, ans);
    hell:;
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