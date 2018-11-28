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

int X, R, C;

char* test[] = {
	"444",
	"442",
	"441",
	"434",
	"433",
	"432",
	"431",
	"422",
	"421",
	"412",
	"411",
	"333",
	"331",
	"323",
	"322",
	"321",
	"311",
	"222",
	"221",
	"212",
	"211",
	"111"
};

set<string> testset(test, test + _countof(test));

bool can(int R, int C, int X) 
{
	if(X == 1) return true;
	if(R * C % X) return false;
	if(X == 2) return true;
	if(C < 2 || R <= 2) return false;
	if(X == 3) return true;
	if(R <= 3) return false;
}

void readCase()
{
	cin >> X >> R >> C;
	/*src.clear();
	for(int i = 0; i < M; i++) {
		string s;
		cin >> s;
		src.push_back(s);
	}/**/
}

void solve()
{
	if(C > R) swap(R, C);

	stringstream str;

	str << R << C << X;

	if(testset.count(str.str())) {
		cout << "GABRIEL";
	} else {
		cout << "RICHARD";
	}
}

int main()
{
	//string fname = "./test/D-example.in";
	string fname = "./test/D-small-attempt0.in";
	//string fname = "./test/D-small-attempt1.in";
	//string fname = "./test/D-small-practice.in";
	//string fname = "./test/D-large-practice.in";
	//string fname = "./test/D-large.in";
	
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

