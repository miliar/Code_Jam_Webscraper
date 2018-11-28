#include <iostream>
#include <algorithm>

const int maxn = 1000;

int n;
long double me[maxn], you[maxn];

int war() {
  int i = 0, j = 0;
  int sol = 0;
  for(;i<n&&j<n;++i) {
    for(;j<n&&me[i]>you[j];j++);
    if(j < n) {
      ++sol;
      ++j;
    }
  }
  return n-sol;
}

int dwar() {
  int i = n-1, j = n-1;
  int sol = 0;
  for(;i>=0;--i) {
    for(;j>=0&&me[i]<you[j];--j);
    if(j>=0) {
      ++sol;
      --j;
    }
  }
  return sol;
}

int main() {
  int T;
  using std::cin;
  using std::cout;
  using std::cerr;
  using std::sort;
  cin >> T;
  for(int tcase=1;tcase<=T;++tcase) {
    cin >> n;
    for(int i=0;i<n;i++)
      cin >> me[i];
    sort(&me[0], &me[n]);
    for(int i=0;i<n;i++)
      cin >> you[i];
    sort(&you[0], &you[n]);

    cout << "Case #" << tcase << ": " << dwar() << ' ' << war() << '\n';
  }
}
