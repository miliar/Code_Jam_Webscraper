#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;
typedef long long int64;
typedef pair<int, int> PII;
const int MOD = 1000000007;
const double EPSILON = 1e-10;

#define FORU(i, a, b) for (int i = (a); i <= (b); ++i)
#define FORD(i, a, b) for (int i = (a); i >= (b); --i)
#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define SIZE(A) ((int) A.size())
#define PB(X) push_back(X)
#define MP(A, B) make_pair(A, B)

template<class T> inline T tmin(T a, T b) {return (a < b) ? a : b;}
template<class T> inline T tmax(T a, T b) {return (a > b) ? a : b;}
template<class T> inline T tabs(T a) {return (a > 0) ? a : -a;}
template<class T> T gcd(T a, T b) {if (b == 0) return a; return gcd(b, a % b);}

int main(int argc, char const *argv[])
{
	int ntest, board[5][5], row1, row2;
	bool e[17];
	scanf("%d", &ntest);
	FORU(t, 1, ntest) {
		memset(e, 0, sizeof(e));
		scanf("%d", &row1);
		REPU(i, 1, 5) {
			REPU(j, 1, 5) {
				scanf("%d", &board[i][j]);
				if (i == row1) e[board[i][j]] = true;
			}
		}
		scanf("%d", &row2);
		int cnt = 0, num = 0;
		REPU(i, 1, 5) {
			REPU(j, 1, 5) {
				scanf("%d", &board[i][j]);
				if (i == row2) {
					if (e[board[i][j]]) {
						cnt++;
						num = board[i][j];
						e[board[i][j]] = false;
					}
				}
			}
		}
		if (cnt == 0) printf("Case #%d: Volunteer cheated!\n", t);
		else if (cnt == 1) printf("Case #%d: %d\n", t, num);
		else printf("Case #%d: Bad magician!\n", t);
	}
	return 0;
}