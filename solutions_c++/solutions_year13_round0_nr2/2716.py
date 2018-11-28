#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>

using namespace std;

#define REP(i, n) for(int i = 0; i < n; ++i)

int nextInt() {
	int x; scanf("%d", &x); return x;
}

void SolveCase()
{
	int n = nextInt();
	int m = nextInt();
	int row[n]; REP(i, n) row[i] = 0;
	int col[m]; REP(i, m) col[i] = 0;

	int a[n][m];
	REP(i, n) REP(j, m){
		a[i][j] = nextInt();
		if(a[i][j] != 1) continue;
		row[i]++;
		col[j]++;
	}
	REP(i, n) REP(j, m){
		bool approachable = a[i][j] == 2 || row[i] == m || col[j] == n;
		if(!approachable)
		{
			cout << "NO" << endl;
			return;
		}
	}
	cout << "YES" << endl;
}

int main()
{
	int n = nextInt();
	REP(i, n){
		cout << "Case #" << i+1 << ": ";
		SolveCase();
	}
	return 0;
}
