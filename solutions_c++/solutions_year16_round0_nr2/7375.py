#include <iostream>

using namespace std;

int main()
{
    int t,nt; cin >> nt;t = nt;
    while (t--) {
      string s; cin >> s;
      int result = 0;
      char prev = '+';
      for (char c : s) {
        if ((prev=='+') && (c=='-'))
            result+=2;
        prev = c;
      }

      cout << "Case #" << nt-t <<  ": " << ((s[0]=='-')?result-1:result)<< endl;
    }
    return 0;
}
