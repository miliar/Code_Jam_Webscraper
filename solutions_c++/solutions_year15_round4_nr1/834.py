#include <cstdio>
#include <complex>
#include <iostream>
#include <cassert>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define REPE(i,x,y) for (int i=(x);i<(y);i++)
#define REP(i,x,y) for (int i=(x);i<=(y);i++)
#define DREP(i,x,y) for (int i=(x);i>=(y);i--)
#define mp make_pair
#define pb push_back
#define MAXN 200
#define endc '\n'
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

char A[MAXN][MAXN];
int S[MAXN][MAXN];

int sum(int x1,int y1,int x2,int y2) {
	return S[x2][y2] + S[x1-1][y1-1] - S[x1-1][y2] - S[x2][y1-1];
}

void solve(int tc) {
	cout<<"Case #"<<tc<<": ";
	int n,m; cin>>n>>m; string s;
	REPE(i,0,MAXN) REPE(j,0,MAXN) S[i][j] = 0;
	REP(i,1,n) {
		cin>>s;
		s = " " + s;
		REP(j,1,m) {
			A[i][j] = s[j];
			//ut<<A[i][j]<<endl;
			S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] ;
			if ((A[i][j] == '^') or (A[i][j] == 'v') or (A[i][j] == '<') or (A[i][j] == '>')) {
				S[i][j]++;
			}
			
		}
	}
	int ans = 0;
	REP(i,1,n) {
		REP(j,1,m) {
			// is out
			bool out = false;
			if ((A[i][j] == '^') and (sum(1,j,i-1,j) == 0)) { out = true; }
			if ((A[i][j] == 'v') and (sum(i+1,j,n,j) == 0)) { out = true; }
			if ((A[i][j] == '<') and (sum(i,1,i,j-1) == 0)) { out = true; }
			if ((A[i][j] == '>') and (sum(i,j+1,i,m) == 0)) { out = true; }
			//cout<<i<<" "<<j<<endl;
			//cout<<sum(1,j,i-1,j) << sum(i+1,j,n,j) << sum(i,1,i,j-1) << sum(i,j+1,i,m) <<endl;

			if (out and (sum(1,j,i-1,j)==0) and (sum(i+1,j,n,j) == 0) and (sum(i,1,i,j-1) == 0) and (sum(i,j+1,i,m) == 0)) {
				cout <<"IMPOSSIBLE"<<endl;
				return;
			}
			
			if (out) { ans ++; } //cout<<"Ok"<<" "<<i<<" "<<j<<endl; cout<<A[i][j]<<endl; }
		}
	}
	cout<<ans<<endl;
}

				

		

int main() {
	ios::sync_with_stdio(false); 
	//cin.tie(0);
	int t; cin>>t;
	REP(i,1,t) solve(i);
	return 0;

}
