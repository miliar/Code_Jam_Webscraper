#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int Test, N, M, b[10000];
char temp[100000];
map<string, int> f;
vector<int> a[1000];

int main(int argc, char **argv)
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
		scanf("%d", &N);
		gets(temp);
		f.clear();
		M = 0;
		for (int i = 0; i < N; i ++) {
			gets(temp);
			a[i].clear();
			string st = "";
			for (int j = 0; temp[j];) {
				for (; temp[j] < 'a' || temp[j] > 'z'; j ++);
				for (; temp[j] >= 'a' && temp[j] <= 'z'; j ++) {
					st = st + temp[j];
				}
				if (f[st] == 0) {
					f[st] = ++ M;
				}
				a[i].push_back(f[st]);
				st = "";
			}
		}
		N -= 2;
		int ret = M;
		for (int s = 0; s < (1 << N); s ++) {
			for (int i = 1; i <= M; i ++) {
				b[i] = 0;
			}
			for (int i = 0; i < a[0].size(); i ++) {
				b[a[0][i]] |= 1;
			}
			for (int i = 0; i < a[1].size(); i ++) {
				b[a[1][i]] |= 2;
			}
			for (int i = 0; i < N; i ++) {
				for (int j = 0; j < a[2 + i].size(); j ++) {
					if ((s >> i) & 1) {
						b[a[2 + i][j]] |= 1;
					} else {
						b[a[2 + i][j]] |= 2;
					}
				}
			}
			int cnt = 0;
			for (int i = 1; i <= M; i ++)
				if (b[i] == 3) {
					cnt ++;
				}
			ret = min(ret, cnt);
		}
		printf("Case #%d: %d\n", Case, ret);
	}
	return 0;
}
