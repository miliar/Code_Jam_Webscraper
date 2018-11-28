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
  int R, C;
	scanf("%d %d ", &R, &C);
  vector<string> g = readVS(R);

  int ct = 0;
  bool poss = true;

  for (int y = 0; y < R; y++) for (int x = 0; x < C; x++) if (g[y][x] != '.') {
    int okb = 0;
    for (int j = y-1; j >= 0; j--) if (g[j][x] != '.') okb |= 1;
    for (int j = y+1; j < R; j++) if (g[j][x] != '.') okb |= 2;
    for (int i = x-1; i >= 0; i--) if (g[y][i] != '.') okb |= 4;
    for (int i = x+1; i < C; i++) if (g[y][i] != '.') okb |= 8;

    if (okb == 0) {
      poss = false;
      break;
    }
    if ((g[y][x] == '^' && (okb&1)) ||
        (g[y][x] == 'v' && (okb&2)) ||
        (g[y][x] == '<' && (okb&4)) ||
        (g[y][x] == '>' && (okb&8))) {
      // it is ok
    } else {
      ct++;
    }
  }

  if (poss) {
    printf("%d\n", ct);
  } else {
    printf("IMPOSSIBLE\n");
  }
  return;
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
