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

int N, X;
map<int, int> files;

inline void assert(bool v)
{
	if(!v) throw "ERROR";
}

void readCase()
{
	cin >> N >> X;
	files.clear();
	for(int i = 0; i < N; i++) {
		int v;
		cin >> v;
		files[v]++;
	}
}

void decandrem(int v)
{
	files[v]--;
	assert(files[v] >= 0);
	if(files[v] == 0) files.erase(v);
}

void solve()
{
	int cnt = 0;
	while(files.size()) {
		int big = files.rbegin()->first;
		decandrem(big);
		int low = -1;
		for(int v = X - big; v >= 0; v--) {
			if(files.count(v)) {
				low = v;
				break;
			}
		}
		if(low >= 0) decandrem(low);
		cnt++;
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

