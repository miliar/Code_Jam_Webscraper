#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<vector>
#include<iostream>
#include<fstream>
#define REP(i, N) for(int i = 0; i<(N); i++)

using namespace std;


int N;

int main() {

	freopen("A-small-attempt0.in", "r", stdin);
	ofstream cout("out.out");
	int C = 0;
	cin >> C;


	//cout << (int)'a' << endl; 97
	for (int cases = 0; cases < C; cases++){
		long long n = 0, ans = 0;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << cases + 1 << ": INSOMNIA" << endl;
			continue;
		}
		bool cnt[10] = { 0, };
		int found = 0;
		long long val = n;
		while (found < 10) {
			long long nn = val;
			while (nn) {
				if (!cnt[nn % 10]) {
					found++;
					cnt[nn % 10] = true;
				}
				nn /= 10;
			}
			val += n;
		}
		cout << "Case #" << cases + 1 << ": " << val - n << endl;
	}
	return 0;
}