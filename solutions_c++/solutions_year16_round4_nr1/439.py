#include <bits/stdc++.h>

using namespace std;


const int MOD = 1e9 + 7;
const int N = 17;
const int M = (1 << N);
int n, r, p, s;
int main(){
  freopen("out", "w", stdout);
  int t; scanf("%d", &t);
  while (t--){
    static int ca = 0;
    printf("Case #%d: ", ++ ca);
    scanf("%d %d %d %d", &n, &r, &p, &s);
    int res = 1;
    string s1 = "P", s2 = "R", s3 = "S";
    for (int i = 1; i <= n; ++ i){
      string a = s1, b = s2, c = s3;
      s1 = a + b;
      s2 = a + c;
      s3 = b + c;
    }
    map <char, int> mp;
    for (int i = 0; i < s1.length(); ++ i){
        mp[s1[i]]++;
    }
    if (mp['R'] == r && mp['P'] == p && mp['S'] == s){
      cout << s1 << endl;
      continue;
    }
    mp.clear();
    for (int i = 0; i < s2.length(); ++ i){
        mp[s2[i]]++;
    }
    if (mp['R'] == r && mp['P'] == p && mp['S'] == s){
      cout << s2 << endl;
      continue;
    }
    mp.clear();
    for (int i = 0; i < s3.length(); ++ i){
        mp[s3[i]]++;
    }
    if (mp['R'] == r && mp['P'] == p && mp['S'] == s){
      cout << s3 << endl;
      continue;
    }
    puts("IMPOSSIBLE");
  }
}
