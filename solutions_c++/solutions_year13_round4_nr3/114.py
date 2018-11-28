#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

const int SIZE = 2<<10;

int n;
int lt[SIZE], rt[SIZE];
bool matr[SIZE][SIZE];

typedef pair<int, int> pii;
multiset<pii> rem;
int deg[SIZE];
bool used[SIZE];

int perm[SIZE];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d", &n);
		for (int i = 0; i<n; i++) scanf("%d", &lt[i]);
		for (int i = 0; i<n; i++) scanf("%d", &rt[i]);

		memset(matr, 0, sizeof(matr));
		for (int i = 0; i<n; i++)
			for (int j = i+1; j<n; j++) {
				if (!(lt[i] < lt[j]))
					matr[j][i] = true;
				if (!(rt[i] > rt[j]))
					matr[i][j] = true;
			}
		for (int i = 0; i<n; i++) {
			int j;
			for (j = i-1; j>=0; j--)
				if (lt[j] == lt[i]-1)
					break;
			if (j >= 0)
				matr[j][i] = true;
		}
		for (int i = n-1; i>=0; i--) {
			int j;
			for (j = i+1; j<n; j++)
				if (rt[j] == rt[i]-1)
					break;
			if (j >= 0)
				matr[j][i] = true;
		}
		
/*		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n; j++)
				printf("%c", matr[i][j] ? '#' : '.');
			printf("\n");
		}
		printf("\n");
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n; j++)
				printf("%c", matr[i][j] | matr[j][i] ? '#' : '.');
			printf("\n");
		}
		printf("\n");*/

/*		for (int u = 0; u<n; u++)
			for (int i = 0; i<n; i++)
				for (int j = 0; j<n; j++)
					matr[i][j] |= matr[i][u] && matr[u][j];*/

/*		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n; j++)
				printf("%c", matr[i][j] ? '#' : '.');
			printf("\n");
		}
		printf("\n");
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n; j++)
				printf("%c", matr[i][j] | matr[j][i] ? '#' : '.');
			printf("\n");
		}
		printf("\n");*/

		for (int i = 0; i<n; i++) {
			deg[i] = 0;
			for (int j = 0; j<n; j++) deg[i] += matr[j][i];
			rem.insert(pii(deg[i], i));
			used[i] = false;
		}
		int k = 0;
		while (!rem.empty()) {
			pii q = *rem.begin();
			rem.erase(rem.begin());

			int v = q.second;
			used[v] = true;
			perm[v] = k++;

			for (int i = 0; i<n; i++) if (!used[i] && matr[v][i]) {
				rem.erase(pii(deg[i], i));
				deg[i]--;
				rem.insert(pii(deg[i], i));
			}
		}

		printf("Case #%d: ", tt);
		for (int i = 0; i<n; i++) printf("%d ", perm[i]+1);
		printf("\n");
		fflush(stdout);
	}
	return 0;
}
