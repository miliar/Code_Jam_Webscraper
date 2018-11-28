#include <iostream>
#include <string>
#include <vector>
#define sz(x) ((int)((x).size()))
#define pb push_back
using namespace std;

int tn;
int n;
string s;
vector<int> a;

int main(int argc, char *argv[])
{
  cin >> tn;
  for (int ti = 1; ti <= tn; ++ti) {
    cin >> n >> s;
    a.clear();
    for (int i = 0; i < sz(s); ++i)
      a.pb(s[i] - '0');

    int need = 0;
    int sum = a[0];
    for (int i = 1; i <= n; ++i) {
      if (sum < i) {
        need += i - sum;
        sum = i;
      }
      sum += a[i];
    }
    cout << "Case #" << ti << ": " << need << endl;
  }
  return 0;
}
