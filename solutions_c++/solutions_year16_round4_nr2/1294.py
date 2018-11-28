#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include <vector>

using namespace std;

typedef pair<int,int> PI;
const int dr[] = {-1,0,1,0};
const int dc[] = {0,1,0,-1};
typedef long long LL;

double p[200];
double q[200];
int N, K;
double memo[16][17];

double rec( int index, int yes_votes ) {
	if( index == K ) return yes_votes == K/2 ? 1.0 : 0.0;
	double& res = memo[index][yes_votes];
	if( res != -1 ) return res;
	res = q[index] * rec( index+1, yes_votes+1 );
	res += (1.0-q[index]) * rec( index+1, yes_votes );
	return res;
}

int main() {
	int cases;
	
	cin >> cases;
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";
		cin >> N >> K;
		assert( 2 <= N && N <= 200 );
		for( int i = 0; i < N; ++i ) cin >> p[i];
		
		double res = 0.0;
		
		for( int i = 0; i < (1<<N); ++i ) {
			int cnt = 0;
			for( int j = 0; j < N; ++j ) {
				if( i & (1<<j) ) {
					q[cnt++] = p[j]; 
				}
			}
			if( cnt != K ) continue;
			for( int i = 0; i < 16; ++i ) 
				for( int j = 0; j < 17; ++j ) memo[i][j] = -1.0;
			double tmp = rec( 0, 0 );
			res = max( res, tmp );
		}
		
		
		
		
		printf( "%.20f\n", res );
	}
	return 0;	
}
