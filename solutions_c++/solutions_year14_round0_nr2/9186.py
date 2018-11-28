#include <iostream>
#include <iomanip>
using namespace std;
#define forn(i,a,b) for(int _b=(b),i=(a);i<=_b;++i)

int t;
double c, f, x;

double next_result(double res, double k) {
  res -= x / (2 + (k - 1) * f);
  res += c / (2 + (k - 1) * f);
  res += x / (2 + k * f);
  return res;
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cout << fixed << setprecision(7);
  cin >> t;
  forn(cs, 1, t) {
    cin >> c >> f >> x;
    double curr = x / 2;
    int k = 1;
    while (true) {
      double next = next_result(curr, k);
      if (next > curr) {
        cout << "Case #" << cs << ": " << curr << endl;
        break;
      } else {
        curr = next;
        k++;
      }
    }
  }
  return 0;
}
