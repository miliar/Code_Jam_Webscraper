#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 1e6;
#define MP make_pair
#define lli long long int
#define y1 y123123

int cnt[500];
int ans[20];

int main() {
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif	
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		string s;
		cin >> s;
		memset(cnt, 0, 500 * sizeof(int));
		memset(ans, 0, 20 * sizeof(int));
		for (int i = 0; i < s.length(); ++i) cnt[s[i]]++;

		ans[0] += cnt['Z']; cnt['E'] -= cnt['Z']; cnt['R'] -= cnt['Z']; cnt['O'] -= cnt['Z']; cnt['Z'] = 0;
		ans[2] += cnt['W']; cnt['T'] -= cnt['W']; cnt['O'] -= cnt['W']; cnt['W'] = 0;
		ans[4] += cnt['U']; cnt['F'] -= cnt['U']; cnt['R'] -= cnt['U']; cnt['O'] -= cnt['U']; cnt['U'] = 0;
		ans[6] += cnt['X']; cnt['S'] -= cnt['X']; cnt['I'] -= cnt['X']; cnt['X'] = 0;
		ans[8] += cnt['G']; cnt['E'] -= cnt['G']; cnt['I'] -= cnt['G']; cnt['H'] -= cnt['G'];  cnt['T'] -= cnt['G'];   cnt['G'] = 0;
		ans[5] += cnt['F']; cnt['I'] -= cnt['F']; cnt['E'] -= cnt['F'];  cnt['V'] -= cnt['F']; cnt['F'] = 0;
		ans[7] += cnt['S']; cnt['E'] -= 2*cnt['S']; cnt['N'] -= cnt['S'];  cnt['V'] -= cnt['S']; cnt['S'] = 0;
		ans[1] += cnt['O']; cnt['N'] -= cnt['O']; cnt['E'] -= cnt['O']; cnt['O'] = 0;
		ans[9] = cnt['N'] / 2;
		ans[3] = cnt['R'];

		for (int i = 0; i <= 10; ++i) {
			for (; ans[i]; --ans[i]) cout << i;
		}

		cout << endl;
	}
}
