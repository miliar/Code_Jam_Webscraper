/*
Author : SRIRAM S
*/
// Libs 
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,A,n) for(i=A;i<n;i++)
#define sz(c) (signed int) c.size()
#define pb(c) push_back(c)
#define INF (int) 1e9
#define all(c) c.begin(),c.end()
#define GI(t) scanf("%d",&t)
#define VI vector<int>
#define PII pair <int,int>
typedef long long LL;

using namespace std;

int main() {
	int t;
	GI(t);
	REP(i,t) {
		vector<string>A;
		string temp;
		REP(j,4) {
			cin>>temp;	
			A.pb(temp);
		}
		int row_sum[4][2];
		int col_sum[4][2];
		REP(j,4) REP(k,2) row_sum[j][k] = 0, col_sum[j][k] = 0;
		int buffer = 0;
		REP(j,4) {
			buffer = 0;
			REP(k,4) {
				if(A[j][k]=='X') row_sum[j][0]++;
				else if(A[j][k]=='O') row_sum[j][1]++;
				else if(A[j][k]=='T') buffer++;
			}
			if(row_sum[j][0]>row_sum[j][1]) row_sum[j][0] += buffer;
			else if(row_sum[j][1] > row_sum[j][0]) row_sum[j][1] += buffer;
		}
		REP(j,4) {
			buffer = 0;
			REP(k,4) {
				if(A[k][j]=='X') col_sum[j][0]++;
				else if(A[k][j]=='O') col_sum[j][1]++;
				else if(A[k][j]=='T') buffer++;
			}
			if(col_sum[j][0]>col_sum[j][1]) col_sum[j][0] += buffer;
			else if(col_sum[j][1] > col_sum[j][0]) col_sum[j][1] += buffer;
		}	
		
		int flag = 0;
		REP(j,4) {
			if(row_sum[j][0]==4 || col_sum[j][0]==4) {
				flag = 1;
				break;
			}
		}
		if(flag) {
			printf("Case #%d: X won\n",i+1);	
			continue;
		}
		flag = 0;
		REP(j,4) {
			if(row_sum[j][1]==4 || col_sum[j][1]==4) {
				flag = 1;
				break;
			}
		}
		if(flag) {
			printf("Case #%d: O won\n",i+1);	
			continue;
		}
		flag = 0;

		// Check diagonal
		int diag1[2];
		diag1[0] = 0; diag1[1] = 0;
		buffer = 0;
		REP(j,4) {
			if(A[j][j]=='X') diag1[0]++;
			else if(A[j][j]=='O') diag1[1]++;
			else if(A[j][j]=='T') buffer++;
		}
		if(diag1[0]>diag1[1]) diag1[0] += buffer;
		else if(diag1[1] > diag1[0]) diag1[1] += buffer;

		if(diag1[0]==4 || diag1[0]==4) {
			printf("Case #%d: X won\n",i+1);	
			continue;
		}
		if(diag1[1]==4 || diag1[1]==4) {
			printf("Case #%d: O won\n",i+1);	
			continue;
		}

		// Check other diagonal
		int diag2[2];
		diag2[0] = 0; diag2[1] = 0;
		buffer = 0;
		for(int j=0,k=3;j<4 && k>=0;j++,k--) {
			if(A[j][k]=='X') diag2[0]++;
			else if(A[j][k]=='O') diag2[1]++;
			else if(A[j][k]=='T') buffer++;
		}
		if(diag2[0]>diag2[1]) diag2[0] += buffer;
		else if(diag2[1] > diag2[0]) diag2[1] += buffer;
		if(diag2[0]==4 || diag2[0]==4) {
			printf("Case #%d: X won\n",i+1);	
			continue;
		}
		if(diag2[1]==4 || diag2[1]==4) {
			printf("Case #%d: O won\n",i+1);	
			continue;
		}

		flag = 0;
		REP(j,4) {
			REP(k,4) {
				if(A[j][k]=='.') {flag = 1; break;}
			}
			if(flag) break;
		}
		if(flag) {
			printf("Case #%d: Game has not completed\n",i+1);	
			continue;
		}
		else {
			printf("Case #%d: Draw\n",i+1);	
		}
		
	}
}
