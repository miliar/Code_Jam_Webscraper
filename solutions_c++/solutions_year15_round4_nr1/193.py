#include <bits/stdc++.h>
using namespace std;

const int mx = 1005;
const int inf = 1e9;

const double PI = 3.14159265358979323846;
const int mm = 105;
const int mod = 1000000007;

void inc (char& c){
  c = getchar ();
  while (c == ' '||c == '\n')     c = getchar ();
}

void in(int &x) {
  char ch=getchar();
  bool flag=false;
  while ((ch<'0'||ch>'9')&&ch!='-') ch=getchar();
  if (ch=='-') {
    flag=true;
    ch=getchar();
  }
  x=0;
  while (ch>='0'&&ch<='9') {
    x=x*10+ch-'0';
    ch=getchar();
  }
  if (flag) x=-x;
}

int m,n;

char grid[mx][mx];

int record[mx][mx][5];

void read() {
  in(n), in(m);
  for (int i=1;i<=n;i++) {
    for (int j=1;j<=m;j++) {
       inc(grid[i][j]);
    }
  }
  return;
}

void solve() {
  int res = 0;

  memset(record, 0, sizeof(record));
  for (int i=1;i<=n;i++) {
    for (int j=1;j<=m;j++) {
      if (grid[i][j] != '.') {
        record[i][j][0] = 1;
        break;
      }
    }
  }
  for (int i=1;i<=n;i++) {
    for (int j=m;j>=1;j--) {
      if (grid[i][j] != '.') {
        record[i][j][1] = 1;
        break;
      }
    }
  }
  for (int j=1;j<=m;j++) {
    for (int i=1;i<=n;i++) {
      if (grid[i][j] != '.') {
        record[i][j][2] = 1;
        break;
      }
    }
  }
  for (int j=1;j<=m;j++) {
    for (int i=n;i>=1;i--) {
      if (grid[i][j] != '.') {
        record[i][j][3] = 1;
        break;
      }
    }
  }

  bool flag = true;
  for (int i=1;i<=n;i++) {
    for (int j=1;j<=m;j++) {
      if (record[i][j][0] && record[i][j][1] && record[i][j][2] && record[i][j][3]) {
        flag = false;
        break;
      }
      if (record[i][j][0] && grid[i][j] == '<') res++;
      if (record[i][j][1] && grid[i][j] == '>') res++;
      if (record[i][j][2] && grid[i][j] == '^') res++;
      if (record[i][j][3] && grid[i][j] == 'v') res++;
    }
    if (!flag) break;
  }

  if (!flag) puts("IMPOSSIBLE");
  else cout << res << endl;
  return;
}

int main() {

  freopen("A-large.in", "r", stdin);
  freopen("data.out", "w", stdout);
  int cas;
  scanf("%d", &cas);
  for (int i = 1; i <= cas; i ++) {
    printf("Case #%d: ",i);
    read();
    solve();
  }
  return 0;
}

/**
int t, n;

string str[105];
vector<int> vec[105];

int top;
map<string, int> mp;

set<int> eng, fen;

int main() {

    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("data.out", "w", stdout);

    scanf("%d", &t);
    getchar();
    for(int cas = 1; cas <= t; cas ++) {
        scanf("%d", &n);
        getchar();
        top = 0;
        mp.clear();
        for(int i = 0; i < n; i ++) vec[i].clear();
        for(int i = 0; i < n; i ++) {
            getline(cin, str[i]);
            string tmp = "";
            for(int j = 0; j < str[i].size(); j ++) {
                if(str[i][j] == ' ') {
                    if(mp.find(tmp) == mp.end()) {
                        mp[tmp] = top ++;
                    }
                    vec[i].push_back(mp[tmp]);
                    tmp = "";
                }
                else tmp += str[i][j];
                if(j == str[i].size() - 1) {
                    if(mp.find(tmp) == mp.end()) {
                        mp[tmp] = top ++;
                    }
                    vec[i].push_back(mp[tmp]);
                }
            }
        }


        int res = 0;
        eng.clear();
        fen.clear();
        for(int j = 0; j < vec[0].size(); j ++) eng.insert(vec[0][j]);
        for(int j = 0; j < vec[1].size(); j ++) fen.insert(vec[1][j]);


        for(int i = 2; i < n; i ++) {
            int cnt1 = 0, cnt2 = 0;
            for(int j = 0; j < vec[i].size(); j ++) {
                if(eng.find(vec[i][j]) != eng.end()) cnt1 ++;
                if(fen.find(vec[i][j]) != fen.end()) cnt2 ++;
            }
            //cout << i << " " << cnt1 << " " << cnt2 << endl;
            if(cnt1 > cnt2) {
                for(int j = 0; j < vec[i].size(); j ++) eng.insert(vec[i][j]);
            }
            else if(cnt1 == cnt2){
                int res1 = 0, res2 = 0;
                set<int> engcpy = eng, fencpy = fen;
                for(int j = 0; j < vec[i].size(); j ++) engcpy.insert(vec[i][j]);
                for(set<int>::iterator it = engcpy.begin(); it != engcpy.end(); it ++) {
                    if(fencpy.find(*it) != fencpy.end()) res1 ++;
                }
                engcpy = eng, fencpy = fen;
                for(int j = 0; j < vec[i].size(); j ++) fencpy.insert(vec[i][j]);
                for(set<int>::iterator it = engcpy.begin(); it != engcpy.end(); it ++) {
                    if(fencpy.find(*it) != fencpy.end()) res2 ++;
                }
                if(res1 <= res2) for(int j = 0; j < vec[i].size(); j ++) eng.insert(vec[i][j]);
                else for(int j = 0; j < vec[i].size(); j ++) fen.insert(vec[i][j]);
            }
            else {
                for(int j = 0; j < vec[i].size(); j ++) fen.insert(vec[i][j]);
            }
        }
        for(set<int>::iterator it = eng.begin(); it != eng.end(); it ++) {
            if(fen.find(*it) != fen.end()) res ++;
        }
        /**
        for(int i = 0; i < (1 << (n - 2)); i ++) {
            cnt = 0;
            eng.clear();
            fen.clear();
            for(int j = 0; j < vec[0].size(); j ++) eng.insert(vec[0][j]);
            for(int j = 0; j < vec[1].size(); j ++) fen.insert(vec[1][j]);
            for(int j = 0; j < n - 2; j ++) {
                if(i >> j & 1) {
                    for(int k = 0; k < vec[j + 2].size(); k ++) eng.insert(vec[j + 2][k]);
                }
                else {
                    for(int k = 0; k < vec[j + 2].size(); k ++) fen.insert(vec[j + 2][k]);
                }
            }
            for(set<int>::iterator it = eng.begin(); it != eng.end(); it ++) {
                if(fen.find(*it) != fen.end()) cnt ++;
            }
            res = min(res, cnt);
        }

        printf("Case #%d: %d\n", cas, res);
    }
    return 0;
}
*/
/**
Case #1: 1
Case #2: 4
Case #3: 3
Case #4: 8
Case #5: 974
Case #6: 988
Case #7: 984
Case #8: 996
Case #9: 979
*/

