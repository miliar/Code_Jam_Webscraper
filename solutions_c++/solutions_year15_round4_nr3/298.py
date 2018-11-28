/*************************************************************************
    > File Name: C.cpp
    > Author: wmg_1001
    > Mail: wmg_1007@163.com 
    > Created Time: Sat 30 May 2015 11:04:26 PM CST
 ************************************************************************/

#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <iomanip>
#include <algorithm>
#include <deque>
#include <queue>
#include <map>
#include <set>
using namespace std;

string S[25][1005], tmp[10005];
int tot[25];
bool B[10005][2];
int s[25][1005];

int main() {
	freopen("C.in", "r", stdin);
	int T, case_T = 0;
	cin >> T;
	while (T--) {
		case_T++;
		cout << "Case #" << case_T << ": ";
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) {
			tot[i] = 0;
			char ch;
			do {
				cin >> S[i][tot[i]++];
				ch = getchar();
			} while (ch == ' ');
		}
		int cnt = 0;
		for (int i = 0; i < n; i++) 
			for (int j = 0; j < tot[i]; j++, cnt++)
				tmp[cnt] = S[i][j];
		sort(tmp, tmp + cnt);
		cnt = unique(tmp, tmp + cnt) - tmp;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < tot[i]; j++)
				s[i][j] = lower_bound(tmp, tmp + cnt, S[i][j]) - tmp;
		int ans = INT_MAX;
		for (int state = 0; state < (1 << n); state++) {
			int res = 0;
			memset(B, false, sizeof(B));
			if ((state & 1) != 0) continue;
			if (((state >> 1) & 1) != 1) continue;
			for (int i = 0; i < n; i++)
				for (int j = 0; j < tot[i]; j++)
					B[s[i][j]][(state >> i) & 1] = true;
			for (int i = 0; i < cnt; i++)
				if (B[i][0] && B[i][1]) res++;
			if (res < ans) ans = res;
		}
		cout << ans << endl;
	}
	return 0;
}
