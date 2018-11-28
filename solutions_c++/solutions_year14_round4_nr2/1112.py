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

int inversions(const vector<int> &v) {
  int N = v.size();
  int inv = 0;
  for (int i = 1; i < N; i++) {
    for (int j = 0; j < i; j++) {
      if (v[i] < v[j]) inv++;
    }
  }
  return inv;
}

int count(const vector<int> &v, int m) {
  int ct = 0, n0 = 0,  N = v.size();
  for (int i = 0; i < N; i++) {
    if ((m>>i)&1) {
      ct += n0;
    } else {
      n0++;
    }
  }
  vector<int> f, r;
  for (int i = 0; i < N; i++) {
    if ((m>>i)&1) {
      f.push_back(v[i]);
    } else {
      r.push_back(v[i]);
    }
  }
  reverse(r.begin(), r.end());

  return ct + inversions(f) + inversions(r);
}

void doIt() {
  int N = readIntLine();
  vector<int> v = readVI(N);
  int mins = 1000000000;
  for (int m = 0; m < (1<<N); m++) {
    int ct = count(v, m);
//    printf("%d: %d\n", i, ct);
    if (ct < mins) mins = ct;
  }
  printf("%d\n", mins);
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
