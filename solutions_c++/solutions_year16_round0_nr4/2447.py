#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

int main() {
	FILE *fin = freopen("D-small-attempt0.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("D-small.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";

		int k,c,s;
		cin >> k >> c >> s;

		for (int i = 1; i < k; i++)
		{
			cout << i << " ";
		}

		cout << k;

		cout << endl;
	}

	return 0;
}