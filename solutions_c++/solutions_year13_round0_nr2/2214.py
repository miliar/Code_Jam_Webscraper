#include <iostream>
#include <list>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <map>
#include <complex>
#include <ctime>
#include <cctype>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

//
// "YES" if and only if, for each i,j, there exists a line (row/column) containing A[i][j]
//		such that A[i][j] is the maximum value in that row/column.

//Proof: If theres a solution, A[i][j] would have been cut by the lawn mower
//	so, the lawnmower would have been set to A[i][j] and cut either the row or the column.
//	And, it can't go over that same row/column again with something smaller than A[i][j], because
//	then the cell (i,j) would have a smaller height than A[i][j] (a contradiction).
//	So, if there is a solution, then A[i][j] is the maximum in either its row or its column (for any i,j).

// 	If A[i][j] is the maximum in its row or its column, take the lawnmower, and apply it to that row and that
//		column. Do this for all (i,j). In the end, you will be left with a lawn equal to the A array.
//		You will never cut the same cell with something smaller than its own value. So then we're done.

// Hence, that is the solution.

// This proof is for anyone who reads this code after the contest and wonders what i'm doing below...

#define MAXN 110
int R[MAXN];
int C[MAXN];
int A[MAXN][MAXN];

int main(){
	int TEST;
	cin >> TEST;
	FOR(test,TEST){
		int N,M;
		cin >> N >> M;
		memset(R,-1,sizeof(R));
		memset(C,-1,sizeof(C));
		FOR(i,N) FOR(j,M) {
			scanf("%d",&A[i][j]);
			R[i] = max(R[i],A[i][j]);
			C[j] = max(C[j],A[i][j]);
		}
		
		bool good = true;
		FOR(i,N) FOR(j,M){
			if (A[i][j] != R[i] && A[i][j] != C[j]) good = false;
		}
		
		cout << "Case #" << (test+1) << ": ";
		cout << (good?"YES":"NO") << endl;
	}
}













