#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); ++i)
#define SIZEOF(a) (sizeof(a)/sizeof((a)[0]))

typedef long long ll;

int K, C, S;

void SolveCase()
{
	if(K!=S){
		// Large data-set
		cout << "IMPOSSIBLE";
		return;
	}
	// S == K, Small dataset
	FOR(i, S) cout << i+1 << " ";
}

int main()
{
	//test1(); return 0;
	int t; cin >> t;
	FOR(i,t){
		cin >> K >> C >> S;
		cout << "Case #" << i+1 << ": ";
		SolveCase();
		cout << endl;
	}
	return 0;
}
