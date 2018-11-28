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

int tc, shy, cse = 1;
string s;

int main() {
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif 

  cin >> tc;
  while(tc--){
    cin >> shy >> s;
    int n = s[0] - '0', ans = 0;
    FOR(i, 1, shy+1){
      if(n < i && s[i] - '0' > 0) ans += i-n, n += i-n;
      //printf("%d\n", ans);
      n += s[i] - '0';
    }
    printf("Case #%d: %d\n", cse++, ans);
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