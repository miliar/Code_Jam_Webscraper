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

void doIt() {
  int N;
  double V, X;
	scanf("%d %lf %lf ", &N, &V, &X);
  vector<double> r(N), c(N);
  double maxc = -1.0, minc = 1000.0;
  for (int i = 0; i < N; i++) {
    scanf("%lf %lf", &r[i], &c[i]);
    if (c[i] > maxc) maxc = c[i];
    if (c[i] < minc) minc = c[i];
  }

  if (maxc < X || minc > X) {
    printf("IMPOSSIBLE\n");
    return;
  }

  double t = 0;
  if (N == 1) {
    t = V / r[0];
  } else if (N == 2) {
    if (fabs(c[0] - c[1]) < 1e-8) {
      t = V / (r[0] + r[1]);
    } else {
//    t0 * r0 + t1 * r1 = V;
//    t0 = (V - (t1 * r1)) / r0;
//    t0 * r0 * c0 + t1 * r1 * c1 = X * V
//    (V - (t1 * r1))/r0 * r0 * c0 + t1 * r1 * c1 = X * V;
//    V * c0 - t1 * r1 * c0 + t1 * r1 * c1 = X * V;
//    t1 * r1 * (c1 - c0) = X * V - V * c0;
      double t1 = (X * V - V * c[0]) / (r[1] * (c[1] - c[0]));
      double t0 = (V - (t1 * r[1])) / r[0];
      t = max(t1, t0);
    }
  }
  printf("%.10lf\n", t);
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
