#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <deque>
#include <numeric>
#include <iterator>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <sys/time.h>

using namespace std;

#define DEBUG(x) cout << #x << ": " << x << endl

#define SZ(a) int((a).size())
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

typedef vector<int> VI;
typedef vector<VI> VVI;


int main() 
{
	
	freopen("B-large.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC ; ++tc)
	{
		double C,F,X;
		C = 1;
		F = 1;
		X = 1;
		cin >> C >> F >> X;
		double sum = 0;
		double t = 1000000000;
		int i;
		for(i = 0; i <= X; ++i)
		{
			double cand = sum + X / (2 + i*F);
			if(t < cand)break;
			else t = cand;
			sum += C / (2 + i*F);
		}
		printf("Case #%d: %0.7lf\n",tc,t);
	}
	
	
	// SUM( i / (2 + F*(i-1)) )
	
	
	
			
	
}







