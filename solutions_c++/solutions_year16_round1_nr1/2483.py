#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;
typedef pair<int,int> pii;
#define sz(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define FOREACH(I,C) for(__typeof(C.begin()) I = (C).begin(); I != (C).end(); I++)
#define pb push_back
#define all(x) x.begin() , x.end()
#define mp make_pair

string solve_smart(string s) {
	string ans = "";
	FOR(i, sz(s)) {
		string a = ans + s[i];
		string b = s[i] + ans;
		if (a > b) {
			ans = a;
		} else {
			ans = b;
		}
	}
	return ans;
}

void solve() {
	string s;
	cin >> s;
	string ans = solve_smart(s);

	/*
	vector<string> strings;
	strings.pb("");
	FOR(i, sz(s)) {
		vs new_strings;
		FOR(j, sz(strings)) {
			string ss = strings[j] + s[i];
			new_strings.pb(ss);
			ss = s[i] + strings[j];
			new_strings.pb(ss);
		}
		strings = new_strings;
	}
	sort(all(strings));

	string ans2 = strings[ sz(strings) - 1 ];
	if (ans != ans2) {
		cout << "ERROR" << endl;
	} else {
	*/
		cout << ans << endl;
	// }
}

int main() {
  int num_testes;
  scanf("%d", &num_testes);
  for(int t = 1; t <= num_testes; t++) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
