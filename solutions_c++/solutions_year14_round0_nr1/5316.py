#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000

void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int A[6][6], B[6][6], fi, se;

void sol()
{
	int tmp = 0, ans = -1;
	FOR(a,1,4) FOR(b,1,4) if (A[fi][a]==B[se][b]) { tmp++; ans = A[fi][a]; }
	if (tmp==1) cout << ans;
	else if (tmp==0) cout << "Volunteer cheated!";
	else cout << "Bad magician!";
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin >> t;
	FOR(a,1,t)
	{
		cin >> fi;
		FOR(b,1,4) FOR(c,1,4) cin >> A[b][c];
		cin >> se;
		FOR(b,1,4) FOR(c,1,4) cin >> B[b][c];
		cout << "Case #" << a << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}
