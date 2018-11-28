#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int tn, n;
vector<string> strs;
int len;
int cnt;
int path[100];
int v[100];

void recur(int level, int chk[]) {
  if (level == n) {
    cnt++;
    // for (int i = 0 ; i < n; ++i) {
    //   cout << path[i] << " " ;
    // }
    // cout << endl;
        
  } else {

    for (int i = 0; i < n; ++i) {
      int chk2[30];
      for (int j = 0; j < 30; ++j) chk2[j] = chk[j];

      if (v[i] == 0) {
        char prev = ' ';
        if (level != 0) {
          string s = strs[path[level - 1]];
          prev = s[s.size() - 1];
        }
        int flag = 0;
        for (int j = 0; j < strs[i].size(); ++j) {
          char now = strs[i][j];
          if (prev != ' ' && now != prev && chk2[now - 'a'] == 1) {
            flag = 1;
            // cout << now << "]FAIL[" << endl;
            break;
          }
          chk2[now - 'a'] = 1;
          prev = now;
          // cout << now;
        }
        if (flag == 1) continue;
        // cout << "]SCSS[" << endl;
        v[i] = 1;
        path[level] = i;
        recur(level+1, chk2);
        v[i] = 0;
      }
    }
  }
}

int main(int argc, char *argv[])
{
  cin >> tn;
  for (int ti = 1; ti <= tn; ti ++ ) {
    cin >> n;
    strs.clear();
    for (int i = 0; i < n; ++i) {
      string str;
      cin >> str;
      strs.push_back(str);
    }
    cnt = 0;
    int chk[30] = {0, };
    recur(0, chk);
    cout << "Case #" << ti << ": " << cnt << endl;
  }
}
    
