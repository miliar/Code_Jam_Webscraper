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
#include <bitset>

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

string toBinary(int64 n)
{
    string r;
    while(n!=0) {r=(n%2==0 ?"0":"1")+r; n/=2;}
    return r;
}

int64 convToDec(string num, int64 base) {
	int64 n = 0, pow = 1;
	for( int64 i = num.length() - 1; i>=0; i-- ) {
		if( num[i] == '1' ) n +=  pow;
		pow *= base;
	}
	return n;
}

int main()
{
	ios::sync_with_stdio(false);
	//freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	int test, case_no = 0, tot;
	cin >> test;
	vector< pair<string, vector<int64> > > res;
	int64 div[10];
	while( test-- ) {
		res.clear();
		int64 n;
		cin >> n >> tot;
		int64 t1 = 1 << (n-1);
		int64 t2 = (1 << n) - 1;
		for( int64 i=t1; i<=t2; i++ ) {
			std::string num = toBinary(i);
			if( num[0] != '1' || num[n-1] != '1' ) continue;
			int j, l=0;
			for(j=2; j<=10; j++) {
				int64 dec = convToDec(num, (int64)j);
				int64 sq = (int64)sqrt((double)dec);
				int64 k;
				for( k = 2; k<=sq; k++ ) {
					if( !(dec % k) )
						break;
				}
				if( k > sq ) break;
				div[l++] = k;
			}
			if( l == 9 ) {
				res.push_back( make_pair(num, vector<int64>(div, div+l)) );
			}
			if( res.size() == tot ) break;
		}
		cout << "Case #" << ++case_no << ":" << endl;
		for(int i=0; i<res.size(); i++) {
			cout << res[i].first;
			for(int j=0; j<res[i].second.size(); j++) {
				cout << " " << res[i].second[j];
			}
			cout << endl;
		}
	}
	return 0;
}