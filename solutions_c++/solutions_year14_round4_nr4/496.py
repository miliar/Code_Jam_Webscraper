#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>

using namespace std;
typedef long long LL;
const LL MOD = 1000000007;

LL count_nodes(vector<string>& a){
    sort(a.begin(), a.end());
    if(a.size() <= 0) return 1;
    LL res = a[0].size() + 1;
    for(int i = 1; i < a.size(); i++){
        int j = 0;
        while(j < a[i-1].size() && j < a[i].size() && a[i-1][j] == a[i][j]) j++;
        res += a[i].size() - j;
    }
    return res;
}

LL count_nodes(vector<int>& assign, vector<string>& seq, int M, int N){
    vector<vector<string> > sv(N);
    for(int i = 0; i < M; i++){
        sv[assign[i]].push_back(seq[i]);
    }
    LL res = 0;
    for(int i = 0; i < N; i++){
        LL part = count_nodes(sv[i]);
        if(part <= 1) return -1;
        res += part;
        res %= MOD;
    }
    return res;
}

void solve(vector<int>& assign, vector<string>& seq, int M, int N, int pos, LL& cnt, LL& max_nodes){
    if(pos >= M){
        LL nodes = count_nodes(assign, seq, M, N);
        if(nodes > max_nodes){
            max_nodes = nodes;
            cnt = 0;
        }
        if(nodes == max_nodes){
            cnt++;
        }
        return;
    }
    for(int i = 0; i < N; i++){
        assign[pos] = i;
        solve(assign, seq, M, N, pos+1, cnt, max_nodes);
    }
}

pair<LL,LL> solve(vector<string>& seq, int M, int N){
    vector<int> assign(M);
    LL cnt = 0;
    LL max_nodes = 0;
    solve(assign, seq, M, N, 0, cnt, max_nodes);
    return pair<LL,LL>(max_nodes, cnt);
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int M, N;
        cin >> M >> N;
        vector<string> seq(M);
        for(int i = 0; i < M; i++){
            cin >> seq[i];
        }
        pair<LL,LL> res = solve(seq, M, N);
        cout << "Case #" << t << ": " << res.first << " " << res.second << endl;
    }
    return 0;
}

