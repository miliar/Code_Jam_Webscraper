#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define pb push_back
#define mp make_pair
#define SZ(v) ((int)((v).size()))
#define LE(s) ((int)((s).size()))
#define ALL(v) (v).begin(), (v).end()


const int MAX = 201;

// FIRST : IND OF PROBA
// SECOND : NUMBER OF VOTES
// THIRD : NUMBER OF YES

/*double solve___(vector<double> &probs, int K){
	double dp[2][MAX][MAX];
	for (int i=0; i<2; i++){
		for (int j=0; j<MAX; j++){
			for (int k=0; k<MAX; k++){
				dp[i][j][k] = 0.0;
			}
		}
	}
	dp[0][0][0] = 1.0;
	int prev = 0, curr = 1;
	for (int i=1; i<=SZ(probs); i++){
		double yes = probs[i-1];
		double no = 1.0-yes;
		for (int j=0; j<=i; j++){
			for (int k=0; k<=i; k++){
				dp[curr][j][k] = dp[prev][j][k];
				if (j > 0) {
					dp[curr][j][k] = max(dp[prev][j][k], dp[prev][j-1][k]*no);
					if (k > 0) {
						dp[curr][j][k] = max(dp[prev][j][k], dp[prev][j-1][k-1]*yes);
					}
				}
			}
		}
		swap(prev, curr);
	}
	return dp[prev][K][K/2];
}*/

double solve(vector<double> props){
	double dp[MAX][MAX] = {{0.0}};
	dp[0][0] = 1.0;
	for (int i=1; i<=SZ(props); i++){
		double yes = props[i-1];
		double no = 1.0 - yes;
		for (int j=0; j<=i; j++){
			dp[i][j] = dp[i-1][j] * no;
			if (j > 0)
				dp[i][j] += dp[i-1][j-1]*yes;
		}
	}
	return dp[SZ(props)][SZ(props)/2];
}

double _solve(vector<double> vec, int K){
	double res =0.0 ;
	for (int i=0; i<(1<<SZ(vec)); i++){
		int cnt = 0;
		vector<double> take;
		for (int j=0; j<SZ(vec); j++){
			if ((i & (1<<j)) != 0){
				cnt++;
				take.pb(vec[j]);
			}
		}
		//cout << i << "         " << cnt << endl;
		if (cnt == K){
			/*cout << h << " :    ";
			for (double e : take) {
				cout << e << "   ";
			}
			cout << endl << endl;*/
			res = max(res, solve(take));
		}
		cnt = 0;
		take.clear();
	}
	return res;
}

int main(){
	int T;
	cin >> T;
	for (int i=1; i<=T; i++){
		int N, K;
		cin >> N >> K;
		vector<double> probs;
		for (int j=0; j<N; j++){
			double h;
			cin >> h;
			probs.pb(h);
		}
		/*sort(ALL(probs));
		vector<double> take;
		for (int j=0; j<K/2; j++){
			take.pb(probs[j]);
			take.pb(probs[SZ(probs)-1-j]);
		}*/
		cout << "Case #" << i << ": " << _solve(probs, K) << endl;
	}
}		
