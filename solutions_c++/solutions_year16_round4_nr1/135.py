#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

int n, r, p, s;

int seen[14][200];
string res[14][200];

void read() {
	scanf("%d %d %d %d", &n, &r, &p, &s);
}



string gen(int n, char final) {
	if (n == 0) {
		string k = "";
		k += final;
		return k;
	}

	string &ret = res[n][final];
	if (!seen[n][final]) {
		seen[n][final]=1;

		string s1, s2;
		if (final == 'R') {
			s1 = gen(n-1,'R');
			s2 = gen(n-1,'S');
		}
		else if (final == 'S') {
			s1 = gen(n-1,'S');
			s2 = gen(n-1,'P');
		}
		else {
			s1 = gen(n-1,'P');
			s2 = gen(n-1,'R');
		}

		if (s1 > s2) swap(s1,s2);
		ret = s1 + s2;
	}

	return ret;
}

bool ok(string& sss) {
	int rr = 0, pp = 0, ss = 0;
	for (char c : sss) {
		if (c == 'R') rr++;
		if (c == 'P') pp++;
		if (c == 'S') ss++;
	}

	return rr == r && ss == s && pp == p;
}

void solve() {
	string s1 = gen(n, 'R');
	string s2 = gen(n, 'P');
	string s3 = gen(n, 'S');

	string oo = "IMPOSSIBLE";
	if (ok(s1) && (oo == "IMPOSSIBLE" || oo > s1)) oo = s1;
	if (ok(s2) && (oo == "IMPOSSIBLE" || oo > s2)) oo = s2;
	if (ok(s3) && (oo == "IMPOSSIBLE" || oo > s3)) oo = s3;

	printf("%s\n", oo.c_str());
}


























int myMod = 0;
int howMany = 1;

int main(int argc, char** argv) {
	if (argc > 1) {
		stringstream ss; ss << argv[1]; ss >> myMod;
		ss.str(""); ss.clear();
		ss << argv[2]; ss >> howMany;
	}

	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		read();
		if (i % howMany == myMod) {
			printf("Case #%d: ", i+1);
			solve();
		}
	}
}