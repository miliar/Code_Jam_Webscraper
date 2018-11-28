#include <cstring>
#include <iostream>
using namespace std;
const int MOD = 1000000007;
int testCase, ret, tot, n, m, size, len[10], b[10], t[200][30];
char s[10][100];

void calc()
{
	int sum = 0;
	for (int i = 0; i < m; i ++) {
		size = 0;
		memset(t, -1, sizeof(t));
		for (int j = 0; j < n; j ++)
		if (b[j] == i) {
			int r = 0;
			for (int k = 0; k < len[j]; k ++) {
				int v = s[j][k] - 'A';
				if (t[r][v] == -1) {
					size ++;
					t[r][v] = size;
				}
				r = t[r][v];
			}
		}
		if (size == 0) {
			return;
		}
		sum += size + 1;
	}
	if (sum > ret) {
		ret = sum;
		tot = 1;
	} else if (sum == ret) {
		tot ++;
	}
}

void search(int k)
{
	if (k == n) {
		calc();
	} else {
		for (int i = 0; i < m; i ++) {
			b[k] = i;
			search(k + 1);
		}
	}
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testCase);
	for (int Case = 1; Case <= testCase; Case ++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i ++) {
			scanf("%s", s[i]);
			len[i] = strlen(s[i]);
		}
		ret = -1;
		search(0);
		printf("Case #%d: %d %d\n", Case, ret, tot);
	}
	return 0;
}
