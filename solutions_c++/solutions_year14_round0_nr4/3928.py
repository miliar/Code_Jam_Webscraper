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
#include <regex.h>

using namespace std;

#define DEBUG(x) cout << #x << ": " << x << endl

#define SZ(a) int((a).size())
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

typedef vector<int> VI;
typedef vector<VI> VVI;

double A[1010];
double B[1010];
bool used[1010];
int solve(int N)
{
	set<double> S;
	for(int i = 0; i < N; ++i)
		S.insert(B[i]);
	int cntK = 0;

	for(int i = 0; i < N; ++i)
	{
		double v = A[i];
		set<double>::iterator it = S.lower_bound(v);
		if(it == S.end())S.erase(S.begin());
		else S.erase(it) , cntK++;
	}
	return N-cntK;
}

int solve2(int N)
{
	sort(A,A+N);
	sort(B,B+N);
	int p = 0 , cnt = 0;
	for(int i = 0; i < N; ++i)
	{
		while(p < N && A[p] < B[i])
			p++;
		if(p < N)
			p++ , cnt++;
	}
	return cnt;
}

int main() 
{
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC ; ++tc)
	{
		int N;
		cin >> N;
		for(int i = 0; i < N; ++i)
			cin >> A[i];
		for(int i = 0; i < N; ++i)
			cin >> B[i];
		
		cout << "Case #" << tc << ": " << solve2(N) << " " << solve(N) << endl;
	}
	
	
	
	// SUM( i / (2 + F*(i-1)) )
	
	
	
			
	
}







