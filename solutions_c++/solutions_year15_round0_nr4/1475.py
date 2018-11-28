#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int solve(int x, int n, int m) {
	if (x == 1) return 1;
	if (x == 2) {
		return (n * m) % 2 == 0;
	}
	if (n * m % x != 0) return 0;
	if ((n == 1 || m == 1) && x > 2) return 0;

	if (x == 3) return 1;

//	if (x == 3 && n == 2 && m == 3) return 1;
//	if (x == 3 && n == 3 && m == 2) return 1;

	if (x == 4) {
		if (min(n, m) <= 2) return 0;
		return 1;
	}

	cout << x << " " << n << " " << m << endl;
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	for (int i = 1; i <= 4; i++) 
		for (int j = 1; j <= 4; j++)
			for (int k = 1; k <= 4; k++) solve(i, j, k);

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int i, j, k;
		cin >> i >> j >> k;
		cout << "Case #" << tt << ": ";
		if (solve(i, j, k)) puts("GABRIEL"); else puts("RICHARD");

	}
	return 0;
}