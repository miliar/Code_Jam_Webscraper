#include <bits/stdc++.h>

using namespace std;

const int N = 30;
int a[N];

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    int n;
    scanf("%d", &n);
    set<pair<int, int>> s;
    int sum = 0;
    for (int i = 0; i < n; ++i) {
      scanf("%d", a + i);
      s.insert({-a[i], i});
      sum += a[i];
    }
    vector<string> sol;
    while (!s.empty()) {
      vector<set<pair<int, int>>::iterator> v;
      auto x = s.begin();
      int cnt = 0;
      for (int i = 0; i < 3; ++i) {
        v.push_back(x);
        if (x != s.end())
          x++, cnt++;
      }
//      cout << cnt << ' ' << tst << endl;
//      for (int i = 0; v[i] != s.end() && i < (int)v.size(); ++i)
//        cout << -v[i]->first << ' ';
//      cout << endl;
//      cout << (v[2] == s.end()) << endl;
//      break;
      if (cnt > 2 && -v[0]->first > 1 && (v[1] == s.end() || -v[1]->first <= (sum - 2) / 2)) {
        sum -= 2;
        sol.push_back(string(2, (char)(v[0]->second + 'A')));
        if (v[0]->first + 2)
          s.insert({v[0]->first + 2, v[0]->second});
        s.erase(v[0]);
      } else if (v[1] != s.end() && ((v[0]->first == v[1]->first) || (-v[0]->first > 1 && -v[1]->first > 1)) && (v[2] == s.end() || -v[2]->first <= (sum - 2) / 2)) {
        sum -= 2;
        sol.push_back(string(1,(char)(v[0]->second + 'A')) + string(1, (char)(v[1]->second + 'A')));
        if (v[0]->first + 1)
          s.insert({v[0]->first + 1, v[0]->second});
        if (v[1]->first + 1)
          s.insert({v[1]->first + 1, v[1]->second});
        s.erase(v[0]);
        s.erase(v[1]);
      } else if (-v[0]->first <= (sum - 1) / 2) {
        sol.push_back(string(1,(char)(v[0]->second + 'A')));
        if (v[0]->first + 1)
          s.insert({v[0]->first + 1, v[0]->second});
        s.erase(v[0]);
      } else {
        printf("\n\nWTF!\n\n");
        return 0;
      }
    }
    printf("Case #%d: ", tst);
    for (int i = 0; i < (int)sol.size(); ++i)
      printf("%s%c", sol[i].c_str(), " \n"[i + 1 == (int)sol.size()]);
    ++tst;
  }
}
