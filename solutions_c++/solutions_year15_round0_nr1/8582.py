#include <iostream>
#include <stdio.h>
FILE *in=stdin, *out=stdout;
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define DEBUG(x) cerr << #x << " = " << x << endl;

int testcases;
int sMax[100];
int s[100][1000+1];
int sum[100][1000+1];
int res[100];

void input() {
	fscanf(in, "%d", &testcases);
	for(int i = 0; i < testcases; ++i) {
		//cout << "test case # " << i << endl;
		fscanf(in, "%d", &sMax[i]);
		char temp[sMax[i]+1];
		fscanf(in, "%s", temp);
		//cout << "sMax? " << sMax << endl;
		//cout << "temp? " << temp << endl;
		for(int j = 0; j <= sMax[i]; ++j) {
			s[i][j] = temp[j]-48;
			//cout << "s[" << i << "][" << j << "]=" << s[i][j] << endl;
		}
	}
}

void calc() {
	int tempRes, isZero;
	for(int i = 0; i < testcases; ++i) {
		tempRes = 0;
		for(int j = 0; j <= sMax[i]; ++j) {
			isZero = (s[i][j] == 0) ? 0 : 1;
			sum[i][j] = (j == 0) ? 0 : s[i][j-1] + sum[i][j-1];
			if (sum[i][j] < j*isZero) {
				int invitedPeople = (j-sum[i][j]);
				tempRes = tempRes + invitedPeople;
				sum[i][j] += invitedPeople;
				//cout << "invited People(" << invitedPeople << ") at sum[" << i << "][" << j << "]" << endl;
			}
			//cout << "sum[" << i << "][" << j << "]=" << sum[i][j] << endl;
		}
		res[i] = tempRes;
		//cout << "res[" << i << "]=" << res[i] << endl;
	}
}

int main() {
	input();
	calc();
	for(int i = 0; i < testcases; ++i) {
		fprintf(out, "Case #%d: %d\n", i+1, res[i]);
	}
	return 0;
}
