#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>

using namespace std;

struct state {
  string pancake;
  int flips;
};

char oppo (char c) {
  if (c == '+') return '-';
  return '+';
}

string flip (string s, int n) {
  string ns = s;
  for (int i = 0; i < n; i ++) {
    ns[i] = oppo(s[n-i-1]);
  }
  return ns;
}

int main () {
  int t;
  string s;
  cin >> t;
  unordered_set<string> seen;

  for (int aa = 0; aa < t; aa++) {
    cin >> s;
    //cout << s << endl;

    cout << "Case #" << aa+1 << ": ";

    state temp;
    temp.pancake = s;
    temp.flips = 0;


    queue <state> q;

    q.push(temp);
    seen.insert (temp.pancake);

    int res = -1;

    while (res==-1) {
      state cur = q.front();
      q.pop();

      //cout << cur.pancake << endl;
      //for (const string& x: seen) cout << " " << x;
      //cout << endl;

      bool found = true;
      for (int i = 0; i < cur.pancake.length() ; i++) {
        if (cur.pancake[i] == '-') {
          found = false;
          break;
        }
      }

      if (found) {
        res = cur.flips;
        break;
      } else {
        for (int i = 1; i <= cur.pancake.length(); i++) {
          string tstr = flip(cur.pancake,i);
          if (seen.find(tstr) == seen.end()){
            state temp;
            temp.pancake = tstr;
            temp.flips=cur.flips+1;
            q.push(temp);
            seen.insert(tstr);
          }
        }
      }

    }
    cout << res << endl;
    seen.clear();
  }
}
