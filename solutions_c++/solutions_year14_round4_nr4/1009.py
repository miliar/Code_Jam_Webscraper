#include <vector>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <bitset>
#include <map>
#include <ctime>
#include <tr1/unordered_map>
#include <cassert>
#include <set>

#define MOD 1000000007

using namespace std;
using namespace tr1;
typedef long long ll;
typedef pair<int, int> pi;

int n, m;
pi dp[1 << 8][4];
bool vis[1 << 8][4];

vector< string > V;

int comp(int mask){
    set< string > suff;
    for(int i = 0; i < n; i++){
        if(mask & (1 << i)){
            string S = "";
            S.reserve(15);
            for(int j = 0; j < V[i].size(); j++){
                S += V[i][j];
                suff.insert(S);
            }
        }
    }
    return suff.size();
}

pi solve(int mask, int idx){
    if(mask == 0) return pi(-10000, 0);
    if(vis[mask][idx]) {
        return dp[mask][idx];
    }
    vis[mask][idx] = true;
    pi& ret = dp[mask][idx];
    ret = pi(0, 0);
    
    if(idx == m - 1){
        if(mask == 0) return pi(-10000, 0);
        return ret = pi(comp(mask), 1);
    }else{
        for (int masK = (mask-1)&mask;masK;masK = (masK-1)&mask){
            int a, b, cost = 0;
            a = masK & mask;
            b = masK ^ mask;
            pi res = solve(b, idx + 1);
            cost += comp(a);
            res.first += cost;
            if(res.first > ret.first){
                ret.first = res.first;
                ret.second = res.second;
            }else if(res.first == ret.first){
                ret.second += res.second;
            }
            if(ret.second >= MOD) ret.second -= MOD;
        }
    }
    return ret;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "r", stdin);
    freopen("out.in", "w", stdout);
#endif
    
    
    /*freopen("in.in", "w", stdout);
    cout << 100 << endl;
    for(int i = 0; i < 100; i++){
        cout << 10 << endl;
        for(int j = 0; j < 10; j++){
            cout << rand() << " ";
        }
        cout << endl;
    }
    
    return 0;*/
    
    int T, t = 1, A, B;
    
    cin >> T;
    while(T--){
        V.clear();
        memset(vis, false, sizeof vis);
        cin >> n >> m;
        string S;
        for(int i = 0; i < n; i++){
            cin >> S;
            V.push_back(S);
        }
        pi qq = solve((1 << n) - 1, 0);
        cout << "Case #" << t++ << ": " << qq.first + m << " " << qq.second << endl;
    }
            
    return 0;
}
