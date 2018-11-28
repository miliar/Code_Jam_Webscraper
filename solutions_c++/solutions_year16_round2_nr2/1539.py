#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

struct node {
	string a, b;
	long long diff;
	long long sca, scb;
};

node all[10000000];

bool cmp( const node &n1, const node &n2 ) {
	if( n1.diff == n2.diff ) {
		if( n1.sca == n2.sca ) {
			return n1.scb < n2.scb;
		}
		return n1.sca < n2.sca;
	}
	return n1.diff < n2.diff;
}

int main( void ) {
	int T;
	scanf("%i", &T);
	
	
	for( int t = 1; t <= T; t++ ) {
		
		string sa, sb;
		cin >> sa >> sb;
		
	
		int s = 0;
		for( int a = 0; a <= 9; a++ )
		for( int b = 0; b <= 9; b++ )
		for( int c = 0; c <= 9; c++ )
		for( int x = 0; x <= 9; x++ )
		for( int y = 0; y <= 9; y++ )
		for( int z = 0; z <= 9; z++ ) {
			
			string ta = sa;
			int A[] = {a, b, c};
			
			for( int i = 0; i < sa.size(); i++ ) {
				if( ta[i] == '?' ) ta[i] = A[i] + '0';
			}
			
			string tb = sb;
			int B[] = {x, y, z};
			
			for( int i = 0; i < sb.size(); i++ ) {
				if( tb[i] == '?' ) tb[i] = B[i] + '0';
			}
			
			all[s++] = (node){ta, tb, abs(stoll(ta) - stoll(tb)), stoll(ta), stoll(tb)};
		}
		
		sort(all, all+s, cmp);
		
		printf("Case #%i: %s %s\n", t, all[0].a.c_str(), all[0].b.c_str());
	}
	
	return 0;
}