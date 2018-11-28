#define _CRT_SECURE_NO_WARNINGS
#include <fstream>
#include <map>
#include <iostream>
#include <utility>
#include <set>
#include <algorithm>
#include <bitset>
#include <queue>
#include <functional>
#include <assert.h>
#include <ctime>
#include <utility>
#include <stack>
#define SI(i) scanf("%d ", &i)
#define SII(i,j) scanf("%d%d", &i, &j)
#define SIII(i,j, k) scanf("%d%d%d", &i, &j, &k)
#define SF(i) scanf("%lf", &i)
#define SFF(i,j) scanf("%lf%lf", &i, &j)
#define SFFF(i,j, k) scanf("%lf%lf%lf", &i, &j, &k)
#define SL(i) scanf("%I64d", &i)
#define SLL(i,j) scanf("%I64d%I64d", &i, &j)
#define SLLL(i,j, k) scanf("%I64d%I64d%I64d", &i, &j, &k)
#define SS(i) scanf("%s\n", i)
#define SSS(i,j) scanf("%s %s", i, j)
#define SC(i) scanf("%d", &i)
#define SCC(i,j) scanf("%c %c\n", &i, &j)

#define PI(i) printf("%d ", i)
#define PII(i,j) printf("%d %d ", i, j)
#define PL(i) printf("%I64d ", i)
#define PLL(i,j) printf("%I64d %I64d ", i, j)
#define PS(i) printf("%s", i)
#define PSS(i,j) printf("%s %s ", i, j)
#define PC(i) printf("%c", i)
#define PCC(i,j) printf("%c %c ", i, j)
#define PN printf("\n")
#define forin(i, k, n) for(int i = (k); i < (n); ++i)
#define forin2(i, k, n) for(int i = (k); i <= (n); ++i)
#define rforin(i, k, n) for(int i = (k); i > (n); --i)
#define mp make_pair
#define rep(i) i  < 'a' ? 'A' : 'a'
typedef unsigned long long ull;
#define pi pair<ull, ull>
using namespace std;

int t;
char s[1001], s2[3003];
int main() {
#ifdef _DEBUG
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
#endif
	SI(t);
	forin2(ii, 1, t)
	{
		forin(i, 0, 1001)
			s[i] = 0;
		forin(i, 0, 3003)
			s2[i] = 0;
		SS(s);
		int ind = 1001, sz = strlen(s);
		printf("Case #%d: ", ii);
		s2[1001] = s[0];
		for (int i = 1, j = 1001; i<sz; ++i){
			if (s[i] >= s2[ind])
				s2[--ind] = s[i];
			else
				s2[++j] = s[i];
		}
		PS(s2 + ind);
		PN;
	}
	return 0;
}