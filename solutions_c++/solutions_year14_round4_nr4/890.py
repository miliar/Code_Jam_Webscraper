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
vector<int> readVI(int n = 0);
vector<double> readVD(double n = 0);
vector<string> readVS(int n = 0);
vector<int> itokens(string s, string sep = " \n\r\t");
vector<string> stokens(string s, string sep = " \n\r\t");

int count(vector<string> &s, vector<int> &w, int N) {
  vector<int> u(N, 0);
  for (size_t i = 0; i < w.size(); i++) u[w[i]]++;
  for (int i = 0; i < N; i++) if (u[i] == 0) return 0;

  vector<set<string> > t(N);
  for (size_t i = 0; i < s.size(); i++) {
    for (size_t j = 0; j < s[i].size(); j++) {
      t[w[i]].insert(s[i].substr(0, j+1));
    }
  }

  int ct = 0;
  for (int i = 0; i < N; i++) ct += t[i].size();

//  for (size_t i = 0; i < s.size(); i++) printf("%d ", w[i]);
//  printf(": %d\n", ct);
  return ct + N;
}

void doIt() {
  int M, N;
	scanf("%d %d ", &M, &N);
  vector<string> s = readVS(M);
  vector<int> w(M, 0);

  int mx = count(s, w, N), mxct = 1;
  while (true) {
    int i = 0;
    while (i < M && w[i] == N-1) i++;
    if (i == M) break;
    w[i--]++;
    while (i >= 0) w[i--] = 0;

    int x = count(s, w, N);
    if (x >= mx) {
      if (x > mx) {
        mxct = 1;
      } else {
        mxct++;
      }
      mx = x;
    }
  }
  printf("%d %d\n", mx, mxct);
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		printf("Case #%d: ", cn);
		doIt();
	}
	return 0;
}








string readLine() {
	char sz[10000];
	fgets(sz, 10000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}
int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}
vector<int> readVI(int n) {
	if (!n) scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}
vector<string> readVS(int n) {
	if (!n) scanf("%d ", &n);
	vector<string> v(n);
	for (int i = 0; i < n; i++) v[i] = readLine();
	return v;
}
vector<string> stokens(string s, string sep) {
	vector<string> res;
	size_t start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(s.substr(start, end-start));
	}
	return res;
}
vector<int> itokens(string s, string sep) {
	vector<int> res;
	size_t start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(atoi(s.substr(start, end-start).c_str()));
	}
	return res;
}
