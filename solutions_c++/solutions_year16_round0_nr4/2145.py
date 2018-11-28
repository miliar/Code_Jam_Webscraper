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

inline void assert(bool v)
{
	if(!v) 
		throw "ERROR";
}

int K, C, S;

void readCase()
{
	cin >> K >> C >> S;
}

void solve()
{
	if(K > C * S) {
		cout << "IMPOSSIBLE";
		return;
	}
	

	for(int i = 0; i < K; i += C) {
		long long pos = 0;
		long long d = 1;
		for(int j = i; j < i + C && j < K; j++) {
			pos += j * d;
			d *= K;
		}
		if(i) cout << " ";
		cout << pos + 1;
	}

}

int main()
{
	//string fname = "./test/D-example.in";
	//string fname = "./test/D-small-attempt0.in";
	//string fname = "./test/D-small-attempt1.in";
	//string fname = "./test/D-small-practice.in";
	//string fname = "./test/D-large-practice.in";
	string fname = "./test/D-large.in";
	
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

