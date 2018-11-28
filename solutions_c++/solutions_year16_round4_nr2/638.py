#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
using namespace std;
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )
typedef long long LL;
typedef pair<int, int> pii;
double g[400][400]; 

double gao(vector<double> P, int K) {
	memset(g, 0, sizeof g);
	g[0][1] = P[0]; g[0][0] = 1 - P[0];
	for (int i = 1; i < K; i++) {
		double p = P[i];
		REP(j, 210) if (g[i - 1][j] > 0) {
			g[i][j] += g[i - 1][j] * (1 - p);
			g[i][j + 1] += g[i - 1][j] * p;
		}
	}
	// cout<<'x';
	return g[K - 1][K / 2];
}

int main(){
    int caseNumber;
    cin>>caseNumber;
    REP(caseN, caseNumber) {
    	int N, K;
    	cin>>N>>K;
    	vector<double> P;
    	REP(i, N) {
    		double x; cin>>x; P.pb(x);
    	}
    	sort(P.begin(), P.end());
    	double b = 0;
    	REP(i, N) {
            vector<double> C;
    		REP(x, i) C.pb(P[x]);
            REP(x, K - i) C.pb(P[P.size() - 1 - x]);
			double g = gao(C, K);
			if (g> b) {
				b = g;
			}
    	}
    	printf("Case #%d: %.12lf\n", caseN + 1, b);
    }
    return 0;
}