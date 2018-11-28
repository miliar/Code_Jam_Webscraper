#include <bits/stdc++.h>
#define fr(i,a,b) for (int i = (a), __ = (b); i < __; ++i)
#define st first
#define nd second
#define dbg(x) cout << #x << " " << x << endl
using namespace std;

const double eps = 1e-7;
const int inf = 0x3f3f3f3f;
typedef pair<int,int> ii;
typedef long long ll;

int qnt[20];

int main() {
	int nt; scanf("%d", &nt); ++nt;
	fr(_,1,nt) {
		memset(qnt, 0, sizeof qnt);
		fr(kk,0,2) {
			int row; scanf("%d", &row); --row;
			fr(i,0,4) {
				fr(j,0,4) {
					int a; scanf("%d", &a);
					if (i == row) qnt[a]++;
				}
			}
		}
		int who = -1, q = 0;
		fr(i,1,17) {
			if (qnt[i] == 2) {
				if (who == -1) who = i;
				++q;
			}
		}
		printf("Case #%d: ", _);
		if (q == 1) printf("%d\n", who);
		else if (q > 1) puts("Bad magician!");
		else puts("Volunteer cheated!");
	}
	return 0;
}
