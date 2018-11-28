//============================================================================
// Name        : Codejam15.cpp
// Author      : Mahmoud Saleh A. Gawad
// Version     :
// Copyright   : None.
// Description : Codejam'15 Qualification Round.
//============================================================================

#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

#define pcase(tt) out << "Case #" << tt << ": "
#define mem(arr,val) memset(arr,val,sizeof arr)
#define loopi(i,val,n) for(i=val;i<=n;i++)
#define loopd(i,val,val2) for(i=val;i>=val2;i--)
#define sz(vec) (int)vec.size()
#define print1(n) out << n <<endl
#define print2(n,m) out << n<<" "<<m<<endl
#define print3(n,m,l) out << n<<" "<<m<< " "<<l<<endl

const char* fin[] = { "a.txt", "b.txt", "c.txt", "d.txt" };
const char* fout[] = { "a.out", "b.out", "c.out", "d.out" };
const int IDX = 0;


int main() {
	ifstream in(fin[IDX]);
	ofstream out(fout[IDX]);

	int TC;
	in >> TC;
	for (int tt = 1; tt <= TC; tt++) {
		int r,c,w;
		in>>r>>c>>w;
		int ans = r*(c/w) + (w-1) + (c%w!=0);
		pcase(tt);
		print1(ans);
	}
	return 0;
}

