#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
#define FOR(i,a,b) for(int i = (a); i < (b); i++)

int main() {
	int t;
	cin >> t;
 FOR(tc, 1, t+1) {
 	string s;
 	cin >> s;
 	string res =  "";
 	for (char c : s) {
 		if (c >= res[0]) res =  c +  res;
 		else res = res + c;
 	}
 	printf("Case #%d: %s\n", tc, res.c_str());
 }
}
