#include<iostream>
#include<cctype>
#include<string>
#include<cmath>
#include<algorithm>
#include<functional>
#include<vector>
#include<cstring>
#include<queue>
#include <numeric>
#include<map>
#include<set>
#include<stack>
#include<fstream>
#include<sstream>
using namespace std;

int sq(int n) {
  int x = sqrt(double(n));
  //cout << x << " "  << n<< endl;
  if (x * x == n)
    return x;
  else return 0;
}
bool pal(int n) {
  int res = 0;
  int k = n;
  while (n) {
   res = res * 10 + (n % 10);
    n /= 10;
  }
  return (k != 0 && res == k);
}
int main() {
  ifstream cin("input.in");
  ofstream cout("out.txt");
  int N, ca = 0, a, b;

  cin >> N;

  while (N--) {
    int cnt = 0;
    cout << "Case #" << ++ca << ": " ;
    cin >> a >> b;

    for (; a <= b; ++a)
      if (pal(a) && pal(sq(a)))
        ++cnt;
    cout << cnt << endl;

  }

    return 0;
  }

