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
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

vector<string> fairs;

char A[120], B[120];

void readCase()
{
	scanf("%s %s", &A, &B);
}

bool lesser( string s1, string s2 )
{
	if( s1.size() < s2.size() ) {
		return true;
	} else if( s2.size() < s1.size() ) {
		return false;
	}

	return s1 < s2;
}

int count(string s)
{
	int pos = lower_bound(fairs.begin(), fairs.end(), s, lesser) - fairs.begin();
	return pos;
}

void solve()
{
	int cnt = count(B) - count(A);
	if( binary_search(fairs.begin(), fairs.end(), B, lesser) ) cnt++;
	printf("%d", cnt);
}

int main()
{
	//string fname = "./test/C-example.in";
	//string fname = "./test/C-small-attempt0.in";
	//string fname = "./test/C-large-1.in";
	string fname = "./test/C-large-2.in";

	FILE *ffairs = fopen("fairs.txt", "r");
	while(!feof(ffairs)) {
		char fair[120];
		fscanf(ffairs, "%s", &fair);
		fairs.push_back(fair);
	}
	
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

