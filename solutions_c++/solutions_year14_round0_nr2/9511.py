//a
#include <iostream>
#include <string>
#include <sstream>
#include <complex>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <memory>
#include <functional>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
 
#define REP(i,b,n) for(int i=b;i<n;i++)
#define REPR(i,b,n) for(int i=n-1;i>=b;i--)
#define CLR(mat) memset(mat, 0, sizeof(mat))
#define NCLR(mat) memset(mat, -1, sizeof(mat))
#define ALL(c) (c).begin(), (c).end()
#define RALL(c) (c).rbegin(), (c).rend()
#define EACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define EXIST(s, e) ((s).find(e) != (s).end())
#define BIT(n, b) ((n>>b) & 1)
#define PB push_back
#define MP make_pair
 
#define LIM 300010
 
using namespace std;
 
static const double PI = acos(-1.0);
static const double EPS = 1e-9;
typedef long long ll;
typedef pair<int, int> pii;

int main(){
	
	int T;
	double C, F, X;
	
	cin >> T;
	
	for(int ca = 1; ca <= T; ++ca){
		
		vector<double> results;
		double t = 0;
		double cps = 2.0;
		
		cin >> C >>	F >> X;
		
		for(int k = 0; k<60000; ++k){
			
			results.push_back(t + X/cps);
			t += C/cps;
			cps += F;
		}
		
		sort(ALL(results));
		printf("Case #%d: %.8f\n", ca, results[0]);
	}
}