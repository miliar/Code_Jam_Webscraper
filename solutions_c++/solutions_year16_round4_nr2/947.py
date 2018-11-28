#include <bits/stdc++.h>
using namespace std;

int T;
long double P[205] = {0};
bool used[205] = {0};
int N, K;
long double best = 0;

void bruteforce(int n, int k){
    if (n == N && k == K){

        //cout << "Found a case" << endl;
        long double dp[20] = {0};
        dp[0] = 1;
        for(int i = 0; i<N; i++){
            if (!used[i]) continue;
            //cout << "using "<< i << endl;
            long double dp2[20] = {0};
            for(int j = 0; j<=k; j++){
                dp2[j] = dp[j] * (1-P[i]);
                if (j > 0) dp2[j] += dp[j-1] * P[i];
            }
            for(int j = 0; j<=k; j++) dp[j] = dp2[j];
        }

        long double tie = dp[K/2];

        //cout << "case yeilds " << tie << endl;
        best = fmaxl(tie, best);
        return;
    }
    else if (n == N && k < K) return;
    else if (k > K) return;
    else{
            if (k < K){
                used[n] = true;
                bruteforce(n+1, k+1);
                used[n] = false;
            }

            bruteforce(n+1, k);
    }
}

int main(){
    freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas<=T; cas++){
        printf("Case #%d: ", cas);


        best = 0;
        cin >> N;
        cin >> K;
        for(int i = 0; i<N; i++){
            cin >> P[i];
        }

        bruteforce(0,0);
        cout << fixed << setprecision(12) << best << endl;


    }


}
