#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

string S;

inline void assert(bool v)
{
	if(!v) 
		throw "ERROR";
}

void readCase()
{
	cin >> S;
}


void solve()
{
	sort(S.begin(), S.end());
	map<char, int> chars;
	for(int i = 0; i < S.size(); i++) chars[S[i]]++;

	int solved[10];

	solved[0] = chars['Z'];
	solved[6] = chars['X'];
	solved[2] = chars['W'];

	for(solved[4] = 0; solved[4] < chars['F'] + 1; solved[4]++) {
		solved[5] = chars['F'] - solved[4];
		if(solved[5] < 0) continue;
		solved[7] = chars['V'] - solved[5];
		if(solved[7] < 0) continue;
		solved[1] = chars['O'] - solved[4] - solved[2] - solved[0];
		if(solved[1] < 0) continue;
		solved[9] = chars['N'] - solved[1] - solved[7];
		if(solved[9] < 0) continue;
		if(solved[9] % 2 != 0) continue;
		solved[9] /= 2;
		int Tlim = chars['T'] - solved[2];
		for(solved[8] = 0; solved[8] < Tlim + 1; solved[8]++) {
			solved[3] = chars['T'] - solved[2] - solved[8];
			if(solved[3] < 0) continue;

			string tst;
			for(int i = 0; i < solved[0]; i++) tst += "ZERO";
			for(int i = 0; i < solved[1]; i++) tst += "ONE";
			for(int i = 0; i < solved[2]; i++) tst += "TWO";
			for(int i = 0; i < solved[3]; i++) tst += "THREE";
			for(int i = 0; i < solved[4]; i++) tst += "FOUR";
			for(int i = 0; i < solved[5]; i++) tst += "FIVE";
			for(int i = 0; i < solved[6]; i++) tst += "SIX";
			for(int i = 0; i < solved[7]; i++) tst += "SEVEN";
			for(int i = 0; i < solved[8]; i++) tst += "EIGHT";
			for(int i = 0; i < solved[9]; i++) tst += "NINE";
			sort(tst.begin(), tst.end());

			if(tst != S) continue;

			string result;
			for(int d = 0; d < 10; d++) {
				for(int i = 0; i < solved[d]; i++) result += '0' + d;
			}
			cout << result;
			return;
		}
	}
}

int main()
{
	//string fname = "./test/A-example.in";
	//string fname = "./test/A-small-attempt0.in";
	string fname = "./test/A-large.in";
	
	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
		fprintf(stderr, "Done %d %%     \r", 100 * tCase / T );
	}
	return 0;
}

