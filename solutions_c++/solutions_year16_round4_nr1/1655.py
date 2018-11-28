#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool check(vector<char> &v) {
  if (v.size() == 1) return true;
  vector<char> vv;
  for (int i = 0; i < v.size(); i += 2) {
    if (v[i] == 'R' && v[i+1] == 'S') vv.push_back(v[i]);
    else if (v[i] == 'S' && v[i+1] == 'R') vv.push_back(v[i+1]);
    else if (v[i] == 'S' && v[i+1] == 'P') vv.push_back(v[i]);
    else if (v[i] == 'P' && v[i+1] == 'S') vv.push_back(v[i+1]);
    else if (v[i] == 'P' && v[i+1] == 'R') vv.push_back(v[i]);
    else if (v[i] == 'R' && v[i+1] == 'P') vv.push_back(v[i+1]);
    else return false;
  }
  return check(vv);
}

int main() {
  int T, t = 0;
  int n,r,p,s;

  scanf("%d", &T);
  while (T-- && scanf("%d %d %d %d", &n, &r, &p, &s) == 4) {
    printf("Case #%d: ", ++t);

    vector<char> v;
    while (p--) v.push_back('P');
    while (r--) v.push_back('R');
    while (s--) v.push_back('S');

    bool ok = false;
    do {
//      printf(">>>>");
  //    for (int i=0; i < v.size();++i)putchar(v[i]); putchar('\n');
      if (check(v)) { 
        for (int i=0; i < v.size();++i)putchar(v[i]); putchar('\n');
        ok = true;
        break;
      }
    } while (next_permutation(v.begin(),v.end()));
    if (!ok) puts("IMPOSSIBLE");
  }
  return 0;
}
