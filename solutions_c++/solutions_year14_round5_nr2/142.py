#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

int P,Q,N,H[100],G[100];
int memo[100][20001];

int solve(int pos, int have){
    if(pos == N) return 0;
    
    int &ret = memo[pos][have];
    
    if(ret == -1){
        ret = solve(pos + 1,have + (H[pos] + Q - 1) / Q);
        
        int hp = H[pos] - (H[pos] - 1) / Q * Q;
        
        int need = (hp + P - 1) / P;
        
        if(need <= have + (H[pos] - 1) / Q) ret = max(ret,G[pos] + solve(pos + 1,have + (H[pos] - 1) / Q - need));
    }
    
    return ret;
}

int main(){
    ios::sync_with_stdio(0);
    
    int TC;
    
    cin >> TC;
    
    for(int tc = 1;tc <= TC;++tc){
        cin >> P >> Q >> N;
        
        for(int i = 0;i < N;++i)
            cin >> H[i] >> G[i];
        
        memset(memo,-1,sizeof memo);
        
        cout << "Case #" << tc << ": " << solve(0,1) << endl;
    }
    
    return 0;
}
