#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#define mp make_pair
#define pb push_back
#define fir first
#define sec second
using namespace std;
typedef long long ll;

template <typename T> inline void R(T &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0' || ch>'9'; ch = getchar());
	for (; ch<='9' && ch>='0'; ch=getchar()) x = x*10 + ch-'0';
}
const int N = 15, M = 4097;
int n, p, r, s;

int play[4][4] = {
	{0,0,0,0},
	{0,0,1,3},
	{0,1,0,2},
	{0,3,2,0}
};
string f[N][4];
void pre() {
	n = 12;
	f[0][1] = 'P', f[0][2] = 'R', f[0][3] = 'S';
	for (int i=1; i<=n; ++i) {
		for (int j=1; j<=3; ++j) {
			int k = j % 3 + 1;
			if (f[i - 1][j] < f[i - 1][k])
				f[i][j] = f[i-1][j] + f[i-1][k]; else
				f[i][j] = f[i-1][k] + f[i-1][j];
		}
	}
}
bool check(string x) {
	return
		count(x.begin(), x.end(), 'P') == p &&
		count(x.begin(), x.end(), 'R') == r &&
		count(x.begin(), x.end(), 'S') == s;
}
void run() {
	scanf("%d%d%d%d", &n, &r, &p, &s);
	string ans = "";
	for (int i=1; i<=3; ++i)
		if (check(f[n][i]) && (ans == "" || f[n][i] < ans))
			ans = f[n][i];
	if (ans == "") ans = "IMPOSSIBLE";
	puts(ans.c_str());
}
int main() {
	pre();
	
	int T; scanf("%d", &T);
	for (int i=1; i<=T; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}