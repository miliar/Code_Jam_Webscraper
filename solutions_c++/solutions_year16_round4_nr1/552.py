#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <omp.h>
#include <windows.h>

using namespace std;

#define FOR(i, s, t) for(int i(s); i<=(int)(t); i++)
#define REP(i, n) FOR(i,0,n-1)
#define ALL(a) a.begin(),a.end()

vector<string> ansstr;
const char ss[10] = "RPS";

char Trans(char c) {
    if (c == 'R') return 'S';
    if (c == 'S') return 'P';
    if (c == 'P') return 'R';
    return ' ';
}

string run(string s) {
    string t;
    REP(i, s.length()) {
        char a = s[i];
        char b = Trans(s[i]);
        if (a > b) swap(a, b);
        t.push_back(a);
        t.push_back(b);
    }
    return t;
}

string dfs(char c, int i) {
    if (i == 0) {
        string s;
        s += c;
        return s;
    }
    char a = Trans(c);
    string s1 = dfs(a, i - 1);
    string s2 = dfs(c, i - 1);
    if (s1 < s2) return s1 + s2;
    return s2 + s1;
}

bool ok(string t, int r, int p, int s) {
    map<char, int> c;
    REP(i, t.length()) c[t[i]]++;
    return c['R'] == r && c['P'] == p && c['S'] == s;
}

void Work(int casen) {
	ostringstream oss;

    int n, r, p, s;
    cin >> n >> r >> p >> s;

    string q = "";
    REP(si, 3) {
        char c = ss[si];
        string t = dfs(c, n);
        if (ok(t, r, p, s)) {
            if (q == "" || q != "" && t < q) q = t;
        }
    }

    if (q == "") q = "IMPOSSIBLE";

	oss << "Case #" << casen << ": " << q << endl;
	ansstr[casen - 1] = oss.str();
}

int main() {
	omp_set_num_threads(4);

	int n;
	cin >> n;
	ansstr.resize(n);

	//#pragma omp parallel for schedule(dynamic)
	for (int i = 1; i <= n; i++) Work(i);

	for (int i = 0; i < n; i++) cout << ansstr[i];

	return 0;
}
