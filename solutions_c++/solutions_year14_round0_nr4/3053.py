#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

static double arr1[1000];
static double arr2[1000];

static void exec(int tn)
{
  int N, ans1 = 0, ans2;
  cin >> N;
  for(int i = 0; i < N; ++i) cin >> arr1[i];
  for(int i = 0; i < N; ++i) cin >> arr2[i];

  set<double> sd(&arr2[0], &arr2[N]);

  ans2 = N;
  for(int i = 0; i < N; ++i) {
    const double &ir = arr1[i];
    set<double>::iterator it = sd.upper_bound(ir);
    if( it == sd.end() ) it = sd.begin();
    else --ans2;
    sd.erase(it);
  }

  sort(&arr1[0], &arr1[N]);
  sort(&arr2[0], &arr2[N]);
#if 0
  for(int i = 0, k = 0; i < N; ++i) {
    const double &ir = arr1[i];
    while(k < N) {
      if(arr2[k] < ir) ++k;
      else {
        ++k;
        break;
      }
    }
    ans2 += (k == N);
  }
#endif
  int f1 = 0, e1 = N-1, e2 = N-1;
  while(f1 <= e1) {
    const double &ir = arr1[e1];
    while(f1 <= e1 && ir < arr2[e2]) {
      --e2;
      ++f1;
    }
    if(f1 <= e1) ++ans1;
    --e1;
    --e2;
  }
  cout << "Case #" << tn << ": " << ans1 << ' ' << ans2 << '\n';
}

int main()
{
  int T;
  cin >> T;
  for(int cn = 1; cn <= T; ++cn) exec(cn);
  return 0;
}

