#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iomanip>   

#define mp make_pair
#define pb push_back

#define REP(i, n) for(int i = 0; i < (n); ++i)
#define REP2(i, s, n) for (int i = (s); i < (n); ++i)

using namespace std;
typedef long long ll;

int N, K;
int cnt[110];
double p[210];

double go(int n, int k) {
    if(n == N) {
        if (k != K) return 0;
        vector<double> prob(K/2+1);
        prob[0] = 1.0;

        for(int i = 0; i < N; ++i) {
            if (!cnt[i]) continue;
            vector<double> prob2(K/2+1);
            prob2[0] = prob[0] * (1.0 - p[i]);
            for(int j = 1; j <= K/2; ++j) {
                prob2[j] = prob[j-1] * p[i] + prob[j] * (1.0 - p[i]);
            }
            prob = prob2;
            /*
            cout << "------" << endl;
            for(int i = 0; i < prob.size(); ++i) {
                cout << prob[i] << endl;
            }
            */
        }

        return prob[K/2];
    }
    else {
        cnt[n] = 0;
        double val1 = go(n+1, k);
        cnt[n] = 1;
        double val2 = go(n+1, k+1);
        return max(val1, val2);
    }
}

//double dy[210][210][110];

void solve()
{
    
    cin >> N >> K;

    
    REP(i, N) cin >> p[i];

/*
    //double dy[210][210][110] = {0, };
    REP(i, N)
        REP(j, K)
            REP(k, K/2) dy[i][j][k] = 0;
    dy[0][0][0] = 1.0;
    
    for(int i = 1; i <= N; ++i) {
        for(int j = 0; j <= K; ++j) {
            for(int k = 0; k <= K/2; ++k) {
                dy[i][j][k] = dy[i-1][j][k];

                cout << dy[i][j][k] << endl;

                if (j > 0) {
                    double val = dy[i-1][j-1][k] * (1.0 - p[i-1]);
                    if (k > 0) val += dy[i-1][j-1][k-1] * p[i-1];
                    if (val > dy[i][j][k]) dy[i][j][k] = val;
                }
                cout << i << " " << j << " " << k << " " << dy[i][j][k] << endl;                
            }
        }
    }

    cout << setprecision(9) << dy[N][K][K/2] << endl;
    */
    cout << setprecision(9) << go(0, 0) << endl;

}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}
