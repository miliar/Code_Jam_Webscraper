#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

double prob(vector<double> team){
    int N = team.size();
    int R = N/2;
    vector<double> dprow(R+1, 0.);
    vector<vector<double> > dp(N+1, dprow);
    // dp[i][j] = prob. j yeses in first i people
    
    dp[0][0] = 1.;
    for(int i=0;i<N;i++){
        double p = team[i];
        for(int j=0;j<=R;j++){
            dp[i+1][j] = p*dp[i][j-1] + (1-p)*dp[i][j];
        }
    }
    
    return dp[N][R];
}

int main(){
    int T;
    cin >> T;
    
    cout << setprecision(9);
    for(int t=1;t<=T;t++){
        int N, K;
        cin >> N >> K;
        vector<double> P(N);
        for(int i=0;i<N;i++) cin>>P[i];
        
        sort(P.begin(), P.end());
        
        double best = 0.;
        for(int i=0;i<=K;i++){
            // i from beginning, K-i from end
            vector<double> team(K);
            for(int j=0;j<i;j++){
                team[j] = P[j];
            }
            for(int j=0;j<K-i;j++){
                team[i+j] = P[N-(K-i)+j];
            }
            
            double p = prob(team);
            if(p>best) best = p;
        }
        
        cout << "Case #" << t << ": " << best << endl;
    }

    return 0;
}