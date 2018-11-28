#include<iostream>
#include<cstdio>
using namespace std;

int main() {
  int cas, cases;
  cin >> cases;
  for (int cas = 1; cas <= cases; cas++) {
    bool a[1005];
    string s;
    int k;
    cin >> s >> k;
    int le = s.length();
    for (int i = 0; i < le; i++) {
      if (s[i] == '-') a[i] = false;
      else a[i] = true;
    }
    int ret = 0;
    for (int i = le - k; i >= 0; i--) {
      int j = i + k -1 ;
      if (!a[j]) {
	//printf("j %d\n", j);
	ret++;
	for (; j >= i; j--) {
	  a[j] = !a[j];
	}
      }
    }
    bool ok = true;
    for (int i = 0; i < k; i++) {
      if (!a[i]) ok = false;
    }
    
    //cout << ret << endl;

    printf("Case #%d: ", cas);
    if (ok) cout << ret << endl;
    else cout << "IMPOSSIBLE\n";
  }
  return 0;
}
