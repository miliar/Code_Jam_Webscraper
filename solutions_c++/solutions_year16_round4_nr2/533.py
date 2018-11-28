#include<vector>
#include<cmath>
#include<complex>
#include<iostream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<float.h>
#include<set>
#include<map>
#include<queue>
#include<math.h>
#include<algorithm>
using namespace std;


typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

#define pb push_back
#define mp make_pair
#define snd second
#define fst first
#define debug printf("--%d--\n",__LINE__)
#define ll long long int

int T;
int K, N;


double calc(vd q){
	int n = q.size();
	double dp[n+1][n+1];
	
	for(int i=0;i<=n;i++)for(int j=0;j<=n;j++) dp[i][j] = 0.0;
	dp[0][0] = 1.0;
	
	for(int j=0;j<n;j++){
		for(int i=0;i<n;i++){
			dp[i][j+1] += (1.0-q[j])*dp[i][j];
			dp[i+1][j+1] += q[j]*dp[i][j];
		}
	}
	return dp[n/2][n];
}


int main(void){
	cin >> T;
	for(int casenum=1;casenum<=T;casenum++){
		cin >> N >> K;
		vd p(N);
		for(int i=0;i<N;i++){
			cin >> p[i];
		}
		sort(p.begin(), p.end());
		
		double ans = 0.0;
		for(int i=0;i<=K;i++){
			vd q(K);
			for(int j=0;j<K;j++){
				if (j<i) q[j] = p[j]; else q[j] = p[j+N-K];
			}
			double prob = calc(q);
			ans = max(prob, ans);
		}
		cout << "Case #" << casenum << ": ";
		cout << ans << endl;
	}
	
	return 0;
}
