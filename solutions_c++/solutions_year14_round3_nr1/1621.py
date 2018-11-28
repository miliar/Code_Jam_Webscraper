#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <list>
#include <vector>
#include <algorithm>

#define RPT(i, x) for (int i = 0; i < (x); i++)

using namespace std;

int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}
void red(int &x, int &y) {
int px = x;
//cout << x << " " << y << endl;
	x = x / gcd(x,y);

	y = y / gcd(px,y);
		//cout << x << " " << y << endl;
}

int co(int p, int q, int lev, int max) {
	if(lev > max) return -1;
	if(p == 1 && q == 1) return 0;
	if(p == 0 && q == 0) return -1;
	
	p *= 2;

	red(p,q);
//cout << p << q << endl;

	if(p > q) {
		p -= q;
		if ( co(p,q,lev+1,max-lev-1) != -1 ) return 1;
		return -1;
	}
	
	int sub = co(p,q,lev+1,max);
	if(sub == -1) return -1;
	else return 1+sub;
}

int main() {
	int n; cin >> n;

	RPT(i,n)
	{
		int p, q; char foo;
		cin >> p >> foo >> q;	
		
		red(p,q);
		//cout << p << " " << q << endl;
		int res;
		
		res = co(p,q,0,40);
		
		if(res != -1) cout << "Case #" << i+1 << ": " << res << endl;
		else cout << "Case #" << i+1 << ": " << "impossible" << endl;
	}
	
	return 0;	
}
