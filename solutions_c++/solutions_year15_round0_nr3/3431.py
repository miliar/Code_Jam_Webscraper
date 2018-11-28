// Author : Abhisar Singhal
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
#include <stack>
#include <cctype>
#include <utility>   
#include <map>
#include <string>  
#include <climits> 
#include <set>
#include <string>    
#include <sstream>
#include <utility>   
#include <ctime>
#include <cassert>
#include <fstream>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> II;
typedef vector<long long> VLL;
typedef vector<bool> VB;

#define SZ(A) ((int)A.size())
#define LEN(A) ((int)A.length())
#define MS(A) memset(A, 0, sizeof(A))
#define MSV(A,a) memset(A, a, sizeof(A))
#define MAX(a,b) ((a >= b) ? (a) : (b))
#define MIN(a,b) ((a >= b) ? (b) : (a))
#define ABS(a) (((a) > 0) ? (a) : (-a))
#define MP make_pair
#define X first
#define Y second
#define PB push_back
#define FOUND(A, x) (A.find(x) != A.end())
#define getcx getchar_unlocked
#define INF (int(1e9))
#define INFL (LL(1e18))
#define EPS 1e-12

#define chkbit(s, b) (s & (1<<b))
#define setbit(s, b) (s |= (1<<b))
#define clrbit(s, b) (s &= ~(1<<b))

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, a, n) for(int i = a; i < n; i++)
#define REV(i, a, n) for(int i = a; i > n; i--)
#define FORALL(itr, c) for(itr = (c).begin(); itr != (c).end(); itr++)
#define ALL(A) A.begin(), A.end()
#define LLA(A) A.rbegin(), A.rend()
//int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};
//int dx[] = {1, 1, 1, 0, 0, -1, -1, -1}, dy[] = {1, 0, -1, 1, -1, 1, 0, -1};
inline void inp( int &n ) {
        n=0; int ch = getcx(); int sign = 1;
        while(ch < '0' || ch > '9') { if(ch == '-') sign=-1; ch = getcx(); }
        while(ch >= '0' && ch <= '9') { n = (n << 3) + (n << 1) + ch - '0', ch = getcx(); }
		n = n * sign;
}

int s[4][4];
int t[4][4];

int main() {
	std::ios_base::sync_with_stdio(false);
	REP (i, 4) REP (j, 4) {
		t[i][j] = (i + j) % 4;
		s[i][j] = 1;
	}
	t[1][0] = 1;
	t[1][1] = 0;
	t[1][2] = 3;
	t[1][3] = 2;
	t[3][0] = 3;
	t[3][1] = 2;
	t[3][2] = 1;
	t[3][3] = 0;
	s[1][1] = -1;
	s[1][3] = -1;
	s[2][1] = -1;
	s[2][2] = -1;
	s[3][2] = -1;
	s[3][3] = -1;
	int tests, tc = 0;
	cin >> tests;
	while (tests--) {
		tc++;
		int n, k;
		cin >> n >> k;
		string ts, str;
		cin >> ts;
		REP (i, k) str += ts;
		int state = 0;
		int sign = 1, ch = str[0] - 'i' + 1;
		if (state == 0 && ch == 1 && sign == 1) {
			state = 1;
		}
		FOR (i, 1, LEN(str)) {
			sign = sign * s[ch][str[i] - 'i' + 1];
			ch = t[ch][str[i] - 'i' + 1];
			if (state == 0 && ch == 1 && sign == 1) {
				state = 1;
			}
			if (state == 1 && ch == 3 && sign == 1) {
				state = 2;
			}
			if (i == LEN(str) - 1 && state == 2 && sign == -1 && ch == 0) {
				state = 3;
			}
		}
		printf("Case #%d: ", tc);
		puts(state == 3 ? "YES" : "NO");
	}
	return 0;
}

