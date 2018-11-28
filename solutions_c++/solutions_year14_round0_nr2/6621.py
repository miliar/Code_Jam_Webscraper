#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility> 
#include <stack>
#include <cstring> 
#include <cmath>
#include <stdio.h>
#include <iomanip>
#include <string.h>

#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
 
#define oo ((int) 1e9)
#define mp make_pair

using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	//freopen("test.in","r",stdin);
	freopen("out.in","w",stdout);
	int t  , con  , al = 1; 
	long double c , f , x  , a , t1 , t2  , r1 , r2; 
	cin >>t ; 
	while(t--) {
		a =  2 ; 
		cin >> c >> f >> x ; 
		t1 = x / a; 
		t2 = c / a; 
		while (true ) {

			a+=f;
		    r2 = t2 + c / a;
			r1 = t2 + x / a;
			if ( r1 > t1 ) break;
			t2 = r2; 
			t1 = r1;
		}

		cout <<"Case #" <<al++ << ": " << std::fixed << setprecision (7) << t1 <<endl;
	}
	
	return 0;
}