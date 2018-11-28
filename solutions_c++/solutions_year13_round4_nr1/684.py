#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;
string readLine();
int readIntLine();
vector<int> readVI(int n);
vector<string> readVS(int n);
vector<int> itokens(string s, string sep);
vector<string> stokens(string s, string sep);

#define MOD 1000002013

long long cost(int s, int e, int p, int N) {
  long long d = e-s;
  long long c = (d*N - (d*(d-1)/2)) % MOD;
  return (c*p) % MOD;
}

void doit(bool print = true) {
  int N, M;
  scanf("%d %d ", &N, &M);
  vector<vector<int> > oep(M);
  vector<pair<int, int> > s, e;
  long long oc = 0, nc = 0;
  for (int i = 0; i < M; i++) {
    oep[i] = readVI(3);
    oc = (oc + cost(oep[i][0], oep[i][1], oep[i][2], N)) % MOD;
    s.push_back(make_pair(oep[i][0], oep[i][2]));
    e.push_back(make_pair(oep[i][1], oep[i][2]));
  }
  sort(s.begin(), s.end());
  sort(e.begin(), e.end());

  int cs = 0;
  for (int ce = 0; ce < M; ce++) {
    while (cs+1 < M && s[cs+1].first <= e[ce].first) cs++;
    while (e[ce].second) {
      if (s[cs].second > 0) {
        if (s[cs].second > e[ce].second) {
          nc = (nc + cost(s[cs].first, e[ce].first, e[ce].second, N)) % MOD;
          s[cs].second -= e[ce].second;
          e[ce].second = 0;
        } else {
          nc = (nc + cost(s[cs].first, e[ce].first, s[cs].second, N)) % MOD;
          e[ce].second -= s[cs].second;
          s[cs].second = 0;
        }
      }
      cs--;
    }
  }

  printf("%lld\n", (oc - nc + MOD) % MOD);
}




/**
 * Library code
 */

int main(int argc, char **argv) {
  int wcase = 0;
  if (argc > 1) wcase = atoi(argv[1]);

	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
    bool print = !wcase || wcase == cn;
		if (print) printf("Case #%d: ", cn);
		doit(print);
	}
	return 0;
}

string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}
int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}
vector<int> readVI(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}
vector<string> readVS(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<string> v(n);
	for (int i = 0; i < n; i++) v[i] = readLine();
	return v;
}
vector<string> stokens(string s, string sep = " \n\r\t") {
	vector<string> res;
	size_t start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(s.substr(start, end-start));
	}
	return res;
}
vector<int> itokens(string s, string sep = " \n\r\t") {
	vector<int> res;
	size_t start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(atoi(s.substr(start, end-start).c_str()));
	}
	return res;
}

