#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}

string prod(const string &s) {
	if (s == "S") {
		return "PS";
	} else if (s == "P") {
		return "PR";
	} else if (s == "R") {
		return "RS";
	}
	return "";
}


string produce(string s, int level) {
	if (level == 0) {
		return s;
	}  else {
		string next = prod(s);
		string a = produce(string(1, next[0]), level - 1);
		string b = produce(string(1, next[1]), level - 1);
		if (a > b) {
			return b + a;
		} else {
			return a + b;
		}
	}
}

int solution(int nTest) {
	int n, r, p, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);

	string temp = "SPR";
	vector<string> res;
	for (int i = 0; i < temp.size(); i++) {
		string S = produce(string(1, temp[i]), n);
		int nR = count(all(S), 'R');
		int nS = count(all(S), 'S');
		int nP = count(all(S), 'P');
		if (nR == r && nP == p && nS == s) {
			res.pb(S);
		}
	}
	sort(all(res));
	if (sz(res) > 0) {
		puts(res[0].c_str());
	} else {
		puts("IMPOSSIBLE");
	}



	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
