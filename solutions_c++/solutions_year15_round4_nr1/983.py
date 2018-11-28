#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define f first
#define s second

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

void testcase(){
	int r,c;
	VS board;
	string s;

	bool ok = true;
	int res = 0;

	cin >> r >> c;
	
	REP(i,r){
		cin >> s;
		board.PB(s);
	}

	REP(i,r) REP(j,c){
		if(board[i][j] != '.'){
			int cou = 0;
			REP(k,c)
				if(board[i][k] != '.') ++cou;
			REP(k,r)
				if(board[k][j] != '.') ++cou;
		if(cou == 2) ok = false;
		} else continue;

		bool left,right,up,down;
		left = right = up = down = true;

		FOR(k,0,i-1)
			if(board[k][j] != '.') up = false;

		FOR(k,i+1,r-1)
			if(board[k][j] != '.') down = false;

		FOR(k,0,j-1)
			if(board[i][k] != '.') left = false;

		FOR(k,j+1,c-1)
			if(board[i][k] != '.') right = false;

		if((up&&board[i][j]=='^') || (down&&board[i][j]=='v') || (left&&board[i][j]=='<') || (right&&board[i][j]=='>')) ++res;
	}
	if(!ok) cout << "IMPOSSIBLE";
	else
		cout << res;
}

int main(){
	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;

	FOR(i,1,t){
		cout << "Case #" << i << ": ";
		testcase();
		cout << endl;
	}

	return 0;
}
