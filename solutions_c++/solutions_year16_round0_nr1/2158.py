#include <cstdio>
#include <sstream>
#include <string>

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)

bool has[10];

int main() {
	int cN, tN, x;
	scanf("%d", &tN);
	FOR(cN, 1, tN) {
		scanf("%d", &x);
		printf("Case #%d: ", cN);
		if (x == 0) {
			puts("INSOMNIA");
			continue;
		}
		int nHas = 0;
		memset(has, 0, sizeof(has));
		int ans = 0;
		while (nHas < 10) {
			++ans;
			string s;
			ostringstream oss(s);
			oss << x * ans;
			s = oss.str();
			REP(i, s.size()) {
				int d = s[i] - '0';
				if (!has[d]) {
					has[d] = 1;
					++nHas;
				}
			}
		}
		printf("%d\n", x * ans);
	}
}
