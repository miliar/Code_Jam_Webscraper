// A7A!
#include <bits/stdc++.h>
#define MAX 1009
#define pb(x) push_back(x)
using namespace std;

const int OO = (int) 2e9;
int memo[MAX][MAX];
int arr[MAX], arr2[MAX];

int foo(int *arr, int n){
  // get the fuckin' max from arr. *including last time added.
  int ret = -1;
  for (int i = 0; i <= n; i++)
    ret = max(ret, arr[i]);
  return ret;
}

int bar(int *arr, int n, int mxx){
  // return idx of the max pancakes.
  for (int i = 0; i < n; i++)
    if (arr[i] == mxx)
      return i;
  // won't reach, but in case.
  return -1;
}

int solve(int n, int mxx){
  if (mxx == 1)
    return mxx;
  int &ret = memo[n - 1][mxx];
  if (ret != -1)
    return ret;
  int indx = bar(arr, n, mxx);
  arr[indx] = mxx / 2, arr[n] = arr[indx] + (mxx % 2); // adding new plate, updating mxx pancakes plate.
  int _mxx = foo(arr, n);
  int path1 = mxx; // leave it.
  int path2 = solve(n + 1, _mxx) + 1; // declare special damn minute.
  return memo[n - 1][mxx] = min(path1, path2);
}

int main(){
  // 3
  // 6 3 9
  //
  // 2
  // 9 3
  freopen("B-small.in", "r", stdin);
  freopen("B-small.out", "w", stdout);
  int tc, ct = 0;
  cin >> tc;
  while (tc--){
    memset(memo, -1, sizeof(memo));
    memset(arr, 0, sizeof(arr));
    memset(arr2, 0, sizeof(arr2));
    int n, mxx = -1;
    cin >> n;
    for (int i = 0; i < n; i++)
      cin >> arr[i], arr2[i] = arr[i], mxx = max(mxx, arr[i]);
    int ret1 = mxx, ret2 = solve(n, mxx);
    for (int all = 1; all <= mxx; all++){
      int tmp = 0, flag = 0;
      for (int i = 0; i < n; i++)
        if (all <= arr2[i]){
          double crap = (arr2[i] * 1.0) / all;
          tmp += ceil(crap) - 1, flag = 1;
        }
      if (flag)
        ret1 = min(ret1, tmp + all);
    }
    //cout << ret1 << " " << ret2 << endl;
    cout << "Case #" << ++ct << ": " << min(ret1, ret2) << endl;
  }
}
