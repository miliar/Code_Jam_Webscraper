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

int N;
vector<int> src;

inline void assert(bool v)
{
	if(!v) throw "ERROR";
}

void readCase()
{
	cin >> N;
	src.clear();
	string s;
	cin >> s;
	
	for(int i = 0; i <= N; i++) {
		int v = s[i] - '0';
		src.push_back(v);
	}
}

void solve()
{
	int cnt = 0;
	int clapping = 0;

	for(int i = 0; i <= N; i++) {
		if(src[i] == 0) continue;
		if(i > clapping) {
			cnt += i - clapping;
			clapping += i - clapping;
		}
		clapping += src[i];
	}

	cout << cnt;
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

