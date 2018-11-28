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
#include <cstring>

#define lld long long int 
#define EOL '\0'
#define PEL cout<<endl;
#define N 100002
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define rep(n) for(int i =0;(i)<(int)(n);(i)++)
#define repi(n) for(int i =0;(i)<(int)(n);(i)++)
#define repj(n) for(int j =0;(j)<(int)(n);(j)++)
#define repij(n,m) for(int i =0;(i)<(int)(n);(i)++) for(int j =0;(j)<(int)(m);(j)++)
#define rep1n(n) for(int i=1;i<(int )(n);i++)

#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
                  std::ostringstream() << std::dec << x ).str()


using namespace std;

string solve(int x,int y) { 
	string d ="";
	int h= 0; 
	int s = x < 0 ?1:-1; 
	while( h != x ) {
		d = d+ (s>0?"E":"W") ;
		h += s;
		s = (abs(s)+1) * (-1 *(abs(s)/s));		
//		cout<<d<<endl;
	}
	s = y < 0 ?abs(s):-abs(s); 
	h=0;
	while( h != y ) {
		d = d+ (s>0?"N":"S") ;
		h += s;
		s = (abs(s)+1) * (-1 * (abs(s)/s));		
	}
 
	return d;
}


int main() 
{
	
	freopen("D:\\MyCode\\CJ\\Data\\B-small-attempt1.in", "r",stdin);
	freopen("D:\\MyCode\\CJ\\Data\\test.out", "w",stdout);
	
	int t;cin>>t;
	for(int ti=1;ti<=t;ti++) {
		int x,y;
		cin>>x>>y;
		cout<<"Case #"<<ti<<": "<<solve(x,y)<<endl;
	}
	return 0;
}