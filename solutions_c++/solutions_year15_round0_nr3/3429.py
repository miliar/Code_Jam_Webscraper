#define  _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

#define INPUT "C:\\Users\\Mahmoud Sayed\\Desktop\\New folder\\in.txt"
#define OUTPUT "C:\\Users\\Mahmoud Sayed\\Desktop\\New folder\\out.txt"
#define SZ(A) (int)A.size()
#define fr first
#define pb push_back
#define sc second
#define mp make_pair
#define _map unordered_map
#define _set unordered_set
#define pr_q priority_queue
#define pb push_back

typedef pair<int, int> ii;
typedef long long ll;
typedef vector<int> vi;

map<string, int> mp1;

string  A[4][4] = { {"1", "i", "j", "k"},
                    {"i", "-1", "k", "-j"},
                    {"j", "-k", "-1", "i"},
                    {"k", "j", "-i", "-1"} };
string AAA[10100];
string mul(string st1, string st2) {
  bool ng = st1[0] == '-';
  if (ng) st1 = st1.substr(1);
  string res = "";
  res = A[mp1[st1]][mp1[st2]];
  if (ng) {
    if (res[0] == '-') res = res.substr(1);
    else res = "-" + res;
  }
  return res;
}

string too(char c) {
  string res= "";
  res.pb(c);
  return res;
}
bool maybe(string st) {
  string ci = "1", cj = "1", ck = "1";
  string tmpi, tmpj, tmpk;
  for (int i = 0; i < SZ(st); i++) {
    tmpi = mul(ci, too(st[i]));
    if (tmpi == "i") {
      cj = "1";
      for (int j = i + 1; j < SZ(st); j++) {
        tmpj = mul(cj, too(st[j]));
        if (tmpj == "j") {
      if (AAA[j + 1] == "k") return 1; 
        }
        cj = tmpj;
      }
    }
    ci = tmpi;
  }
  return 0;
}
int main() {
#ifndef ONLINE_JUDGE
  freopen(INPUT, "r", stdin);
  freopen(OUTPUT, "w", stdout);
#endif
  mp1["1"] = 0, mp1["i"] = 1, mp1["j"] = 2, mp1["k"] = 3;
  int cse = 1, t;
  for (cin >> t; t--; cse++) {
    printf("Case #%d: ", cse);
    int L, X;
    cin >> L >> X;
    X = min(X, (X%4 +4));
    string tmp, st;
    cin >> tmp;
    st = tmp;
    for (int i = 1; i < X; i++)
      st += tmp; 
    AAA[SZ(st)] = "1"; 
    for (int i = SZ(st)-1; i >= 0; i--){
      AAA[i] = mul(AAA[i+1], too(st[i])); 
      if(i != SZ(st) -1) {
        if(AAA[i][0] == '-') AAA[i] = AAA[i].substr(1); 
        else AAA[i] = "-"+ AAA[i]; 
      }
    }
    if (maybe(st)) puts("YES");
    else puts("NO");
  }
}