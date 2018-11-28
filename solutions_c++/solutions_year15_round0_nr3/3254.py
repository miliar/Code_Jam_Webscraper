#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <string.h>
#include <cstring>
#define oo (int)1e9
#define fill( a , v ) memset( a , v , sizeof (a) )
#define bits( x ) __builtin_popcount( x )
#define gcd( a , b ) __gcd( a, b )
#define lcm( a , b ) (a/gcd( a, b ) ) * b
#define s(n)scanf( "%d" , &n )
#define add push_back
const int mxn = 10000 + 10;
typedef long long ll;
#define pii pair<double,double>
using namespace std;
int cs, T;
int count;

string s, input;
int L,X;
int n;
map<char, int>M;

int a[4][4] = {
	{1, 2, 3, 4},
	{2, -1, 4, -3},
	{3, -4, -1, 2},
	{4, 3, -2, -1}
};

int t[4*mxn];

int getVal(int v1, int v2) {

	int sign1 = v1 > 0 ? 1 : -1;
	int sign2 = v2 > 0 ? 1 : -1;
	return a[abs(v1) -1] [abs(v2) - 1] * sign2 * sign1;
}

void create(int k, int low, int high) {

	if(low == high) {
		t[k] = a[0][  M[s[low-1]] - 1  ];
		//cout << s[low-1] << " " << t[k] << endl;
		return;
	}

	int mid = (low + high) / 2;
	create(2*k, low, mid);
	create(2*k + 1, mid+1, high);
	t[k] = getVal( t[2*k], t[2*k+1] );
}


int query(int k, int low, int high,int qlow, int qhigh) {

	if( low >= qlow && high <= qhigh )return t[k];
	
	if( qhigh < low || high < qlow )return 1;
	
	int mid = (low + high)  >> 1;
	
	int left = query( 2*k , low ,mid ,qlow, qhigh );
	int right = query( 2*k + 1, mid + 1 ,high ,qlow, qhigh );
	return getVal(left, right);
}

int main() {

	M['i'] = 2;
	M['j'] = 3;
	M['k'] = 4;
	s(T);
	while(T--) {
		fill(t, 0);
		cin >> L >> X;
		cin >> input;
		s = "";
		while(X-- > 0)
			s += input;

		n = s.size();

		create(1, 1, n);

		vector<int> prefixPoints, suffixPoints;

		for(int i=1;i<=n;i++) {
			int value = query(1, 1, n, 1, i);
			// cout << i << " " << value << endl;
			if(value == M['i'])
				prefixPoints.add(i);
		}

		for(int i=n;i>0;i--) {
			int value = query(1, 1, n, i, n);
			// cout << i << " " << value << endl;
			if(value == M['k'])
				suffixPoints.add(i);
		}

		bool ok = false;
		for(int i=0;i<prefixPoints.size() && !ok;i++) {
			for(int j=0;j<suffixPoints.size() && !ok;j++) {
				// cout << prefixPoints[i] << " " << suffixPoints[j] << endl;
				if(prefixPoints[i] + 1 <= suffixPoints[j] - 1)
					ok |= query(1, 1, n, prefixPoints[i] + 1, suffixPoints[j] - 1) == M['j'];
			}
		}
		string ans = ok ? "YES" : "NO";
		printf("Case #%d: %s\n", ++cs, ans.c_str());
	}
}