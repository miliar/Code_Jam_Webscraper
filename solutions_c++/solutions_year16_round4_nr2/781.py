
/// CODEJAM PROBLEM B

#include <bits/stdc++.h>

using namespace std;

const int maxN = 43;
const int mod = 1e9 + 7;
const int add = 18;
vector<double> input;
int n , k;
double dp[maxN][maxN] ;
bool vis[maxN][maxN];
double solve(int pos,int cant){
    if(pos == k){
        if(cant) return 0;
        return 1;
    }
    if(vis[pos][cant + add]){
        return dp[pos][cant + add];
    }
    vis[pos][cant + add] = true;

    double answer = input[pos] * solve(pos+1 , cant + 1) ;
    answer += (1 - input[pos]) * solve(pos+1,cant-1);
    return dp[pos][cant + add] = answer;
}


double a[maxN];

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("on.c","w",stdout);


    int tc , number_case = 1;
    cin >> tc;

    while(tc--){
        cin >> n >> k;
        for(int i = 0; i < n; ++i){
            cin >> a[i];
        }

        double answer = 0;
        for(int mask = 0; mask < 1<<n; mask++){
            int ones = __builtin_popcount(mask);
            if(ones != k){
                continue;
            }
            input.clear();
            for(int i = 0; i < n; ++i){
                if(mask & (1<<i)){
                    input.push_back(a[i]);
                }
            }

            for(int i = 0; i < n; ++i){
                memset(vis[i] , false,sizeof vis[i]);
            }

            answer = max(answer , solve(0,0));
        }

        printf("Case #%d: %.15f\n",number_case++,answer);
    }






    return 0;
}
