#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <cstring>
#include <math.h>
#include<cstdio>
#include<deque>
#include<sstream>
using namespace std;
#define mp make_pair
#define eps 1e-6
int dx[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
vector<string> v;
int t, n, k;
void calc(int ind, string s) {
	if (ind == n - 2) {
		v.push_back("1" + s + "1");
		return;
	}
	calc(ind + 1, s + "0");
	calc(ind + 1, s + "1");
}
//17000
int main() {
	freopen("a.txt", "rt", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &t);
	scanf("%d%d", &n, &k);
	calc(0, "");
	puts("Case #1:");
	for (int i = 0; i < v.size() && k; i++) {

		unsigned long long nub = 0;
		vector<unsigned long long> temp;
		for (int j = 2; j <= 10; j++) {
			nub = 0;
			for (int jj = 0, pos = n - 1; jj < n; jj++, pos--)
				nub += (unsigned long long) pow(j, pos)
						* (unsigned long long) (v[i][jj] - '0');

			bool f = 0;

			for (long long jj = 2; jj <= sqrt(nub); jj++)
				if (nub % jj == 0) {
					temp.push_back(jj);
					f = 1;
					break;
				}
			if (!f)
				break;
		}
		if (temp.size() == 9) {
			k--;
			cout << v[i];
			for (int j = 0; j < 9; j++)
				cout << " " << temp[j];
			cout << endl;
		}
		temp.clear();
	}
	return 0;
}
