#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second
#define vi vector<int>
#define vii vector< pii >

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

int T;
int N;
vector<int> lists[105];

int arr[55][55];


bool from_smallest;
// <=
bool cmp(int A, int B) {
  if (from_smallest) return A <= B;
  return A >= B;
}
bool cmp2(const vector<int> &A, const vector<int> &B) {
  return cmp(A[0], B[0]);
}
bool lesser(int A, int B) {
  return !(cmp(B, A));
}

vector<int> dfs(int row_i, int col_i, int list_i, int missing_row_i = -1, int missing_col_i = -1) {
//  printf("%d %d %d %d %d\n", row_i, col_i, list_i, missing_row_i, missing_col_i);
  vector<int> ans;
  if (row_i == N && col_i == N) {
    if (missing_row_i != -1) {
      REP(i, N) ans.push_back(arr[missing_row_i][i]);
      return ans;
    }
    REP(i, N) ans.push_back(arr[i][missing_col_i]);
    return ans;
  }
//  printf("arr[row_i][0] %d, arr[0][col_i] %d, lesser %d\n", arr[row_i][0], arr[0][col_i], lesser(arr[row_i][0], arr[0][col_i]));
  if ((row_i != N && (list_i == 2 * N - 1 || (((col_i == N || lesser(arr[row_i][0], arr[0][col_i])) && lesser(arr[row_i][0], lists[list_i][0]))))))
    return dfs(row_i + 1, col_i, list_i, row_i, -1);
//  printf("ok\n");
  if ((col_i != N && (list_i == 2 * N - 1 || (((row_i == N || lesser(arr[0][col_i], arr[row_i][0])) && lesser(arr[0][col_i], lists[list_i][0]))))))
    return dfs(row_i, col_i + 1, list_i, -1, col_i);
  if (row_i < N && lists[list_i][0] == arr[row_i][0]) {
    bool ok = true;
    FOR(i, 0, col_i - 1) if (i != missing_col_i) if (arr[row_i][i] != lists[list_i][i]) ok = false;
    if (ok) {
      REP(i, N) arr[row_i][i] = lists[list_i][i];
      ans = dfs(row_i + 1, col_i, list_i + 1, missing_row_i, missing_col_i);
      if (!ans.empty()) return ans;
    }
  }
  if (col_i < N && lists[list_i][0] == arr[0][col_i]) {
    bool ok = true;
    FOR(i, 0, row_i - 1) if (i != missing_row_i) if (arr[i][col_i] != lists[list_i][i]) ok = false;
    if (ok) {
      REP(i, N) arr[i][col_i] = lists[list_i][i];
      ans = dfs(row_i, col_i + 1, list_i + 1, missing_row_i, missing_col_i);
      if (!ans.empty()) return ans;
    }
  }
  return {};
}

int main() {

  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%d", &N);
    int mn = 10000, mn_cnt = 0;
    int mx = -1, mx_cnt = 0;
    REP(i, 2 * N - 1) {
      lists[i] = vector<int>(N, 0);
      REP(j, N) {
        scanf("%d", &lists[i][j]);
        if (lists[i][j] < mn) {
          mn = lists[i][j]; mn_cnt = 1;
        } else if (lists[i][j] == mn) ++mn_cnt;
        if (lists[i][j] > mx) {
          mx = lists[i][j]; mx_cnt = 1;
        } else if (lists[i][j] == mx) ++mx_cnt;
      }
    }
    if (mn_cnt == 2) from_smallest = true;
    else from_smallest = false;
//    printf("%d %d %d %d\n", mn, mn_cnt, mx, mx_cnt);
    REP(i, 2 * N - 1) sort(lists[i].begin(), lists[i].end(), cmp);
    sort(lists, lists + 2 * N - 1, cmp2);
//    REP(i, 2 * N - 1) { REP(j, N) printf("%d ", lists[i][j]); printf("\n"); }
    REP(i, N) {
      arr[0][i] = lists[0][i];
      arr[i][0] = lists[1][i];
    }
    vector<int> result = dfs(1, 1, 2);
    sort(result.begin(), result.end());
    printf("Case #%d:", t);
    REP(i, N) { printf(" %d", result[i]); }
    printf("\n");
  }

  return 0;
}
