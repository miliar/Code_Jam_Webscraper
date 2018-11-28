#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " << 

using namespace std;

int step(int k) {
  if (k == 0)
    return -1;
  set<int> d;
  for (int i=k; ;i+=k) {
    int x = i;
    while (x > 0) {
      d.insert(x%10);
      x /= 10;
    }
    //TRACE(i);
    if ((int)d.size() == 10)
      return i;
  }
  return -1;
}

int main() {
  int t;
  cin >> t;
  for (int tt=0; tt<t; tt++) {
    cout << "Case #" << tt+1 << ": ";
    int x;
    cin >> x;
    int s = step(x);
    if (s == -1)
      cout << "INSOMNIA" << endl;
    else
      cout << s << endl;
  }
  return 0;
}
