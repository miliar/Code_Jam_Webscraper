#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <bitset>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int N = 4;

int a[N][N];
int cnt[N * N + 1];
int n;
int testCases;

int main()
{
	cin >> testCases;
	for (int index = 1; index <= testCases; ++index) {
		memset(cnt, 0, sizeof cnt);
		cin >> n;
		--n;
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				cin >> a[i][j];
		for (int i = 0; i < N; ++i) ++cnt[a[n][i]];
		cin >> n;
		--n;
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				cin >> a[i][j];
		for (int i = 0; i < N; ++i) ++cnt[a[n][i]];
		
		int ans = 0;
		for (int i = 1; i <= N * N; ++i) ans += cnt[i] == 2;
		switch (ans) {
			case 0 :
				printf("Case #%d: Volunteer cheated!\n", index);
				break;
			case 1 :
				for (int i = 1; i <= N * N; ++i)
					if (cnt[i] == 2) {
						printf("Case #%d: %d\n", index, i);
						break;
					}
				break;
			default :
				printf("Case #%d: Bad magician!\n", index);
		}
	}
	return 0;
}
