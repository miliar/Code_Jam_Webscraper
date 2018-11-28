#include <iostream>
#include <set>
#include <string>
using namespace std;


int main() {
  int Z;
  cin >> Z;
  for (int cn=0;cn<Z;++cn) {
    int m, n;
    cin >> m >> n;
    string s[20];
    for (int i=0;i<m;++i) cin >> s[i];
    int best=0,best_count=0;
    int maxz=1;
    for (int i=0;i<m;++i) maxz*=n;
    for (int as=0;as<maxz;++as) {
      set<string> setz[4];
      int bc = as;
      for (int i=0;i<m;++i) {
        set<string>& ss = setz[bc % n];
        bc /= n;
        for (int j=0; j<=s[i].size(); ++j)
          ss.insert(s[i].substr(0, j));
      }
      int res=0;
      for (int i=0;i<n;++i) res += setz[i].size();
      if (res > best) { 
        best = res;
        best_count = 0;
      }
      if (res==best) best_count++;
    }
    cout << "Case #"<<(cn+1)<<": " << best << " " << best_count << endl;
  }
}
