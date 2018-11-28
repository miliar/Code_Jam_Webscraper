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
string c, ja;
int res = 100000, res_c = 100000, res_j = 1000000;
string str_c, str_j;
void rec(string t1, string t2) {
	if( (t1.find('?') == string::npos) && (t2.find('?') == string::npos)  ) {
		int n1 = atoi(t1.c_str());
		int n2 = atoi(t2.c_str());

		if( abs( n1 - n2) < res ) {
			res = abs( n1 - n2);
			res_c = n1;
			res_j = n2;
			str_c = t1;
			str_j = t2;
		} else if( abs( n1 - n2) == res ) {
			if( n1 < res_c ) {
				res_c = n1;
				res_j = n2;
				str_c = t1;
				str_j = t2;
			} else if( n1 == res_c ) {
				if( n2 < res_j ) {
					res_c = n1;
					res_j = n2;
					str_c = t1;
					str_j =	t2;
				}
			}
		}
		return;
	}
	
	if( t1.find('?') != string::npos ) {
		for( int i = 0; i<c.length(); i++ ) {
			if( t1[i] == '?' ) {
				for( int j = 0; j<10; j++ ) {
					t1[i] = j + 48;
					rec(t1, t2);
				}
			}
		}
	} else if( t2.find('?') != string::npos ) {
		for( int i = 0; i<t2.length(); i++ ) {
			if( t2[i] == '?' ) {
				for( int j = 0; j<10; j++ ) {
					t2[i] = j + 48;
					rec(t1, t2);
				}
			}
		}
	}
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
		cout<< "Case #"<<++case_no<<": "	;
		cin >> c >> ja;
		res = 100000, res_c = 100000, res_j = 1000000;
		str_c = "", str_j = "";
		rec(c, ja);
		cout << str_c << " "  << str_j << endl;
	}

	return 0;
}