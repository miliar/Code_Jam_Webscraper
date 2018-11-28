#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

typedef unsigned int uint; 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef unsigned short ushort; 
typedef unsigned char uchar; 

#define T int

typedef pair<T,T> pi;
typedef pair<pi, T> pii;
typedef vector<T> vi; 
typedef vector<pi> vpi;
typedef vector<pii> vpii;

typedef vector<string> vs; 
typedef vector<double> vd; 

#define SZ(A) ((int)(A.size()))
#define LENGTH(A) ((int)(A.length()))
#define MP(A,B) make_pair(A,B)
const double PI=acos(-1.0); 
const double eps=1e-11; 
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,a) for(int i=0;i<(a);++i)
#define ALL(a) (a).begin(),(a).end()
#define inf 1000000000
#define MAX 100001

/***** BIT WISE ******/
/*
Setting a bit
num |= 1 << x;

Clearing a bit
num &= ~(1 << x);

Toggling a bit
number ^= 1 << x;

Checking a bit
bit = (num >> x) & 1;
*/

/*
dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]

*/

bool cmp( )
{

	return true;
}

int do_search( int x, int y ) {
	int l = 0, h = 0;


	return l;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int test;
	cin >> test;
	int case_no = 0;
	while( test-- ) {
		cout << "Case #"<<++case_no<<": ";
		string s;
		cin >> s;
		int cnt1 = 0,cnt2 = 0, res = 0;
		for( int i=0; i<s.length(); i++ ) {
			if( s[i] == '+' ) {
				if( cnt2 > 0 ) {
					res += 1;
					cnt2 = 0;
				}
				cnt1++;
			} else {
				if( cnt1 > 0 ) {
					res += 1;
					cnt1 = 0;
				}
				cnt2++;
			}
		}
		if( cnt2 ) res += 1;
		cout << res << endl;
	}
	return 0;
}