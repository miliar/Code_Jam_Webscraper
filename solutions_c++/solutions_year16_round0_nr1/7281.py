#include <iostream>
#include <vector>
using namespace std;

bool all (vector<bool> & v) {
    for (int i = 0; i< 10; i++) {
        if (v[i]==false)
            return false;
    }
    return true;
}

void update (vector<bool> &v, int n) {
    string s = std::to_string(n);
    for (char c : s)
        v[c-'0'] = true;
}

int main()
{
    int t,nt; cin >> nt;t = nt;
    while (t--) {
      int n; cin >> n;
      int oldn = n;
      if (n==0) {cout << "Case #" << nt-t <<  ": INSOMNIA" << endl; continue;}
      vector<bool> d (10, false);
      update (d, n);
      while (!all(d))
      {
        n += oldn;
        update(d,n);
      }
      cout << "Case #" << nt-t <<  ": " << n << endl;
    }
    return 0;
}
