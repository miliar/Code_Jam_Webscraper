#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#include <functional>
#include <complex>
#include <iomanip>

using namespace std;

typedef long long ll;

int a[1000];
int b[1000];

int main(void){
  int T;
  cin >> T;
  for(int tt = 0; tt < T; ++ tt){
    int N;
    cin >> N;

    for (int i = 0; i < N; ++i)
      cin >> a[i];

    int l = 0, r = N-1;

    copy(a, a+N, b);
    sort(b, b+N);

    int ans = 0;

    for(int i = 0; i < N; ++i){
      int target = find(a, a+N, b[i]) - a;

      // cout << target << " : " << target-l << ", " << r-target << endl;

      if(target - l < r - target){
        // cout << "left" << endl;
        for(int j = target; j > l; --j){
          swap(a[j], a[j-1]);
          ++ans;
        }
        ++l;
      }
      else{
        // cout << "right" << endl;
        for(int j = target; j < r; ++j){
          swap(a[j], a[j+1]);
          ++ans;
        }
        --r;
      }

      // for(int j = 0; j < N; ++j)
      //   cout << a[j] << ' ';
      // cout << endl;

    }

    cout << "Case #" << tt+1 << ": " << ans << endl;
  }

  return 0;
}
