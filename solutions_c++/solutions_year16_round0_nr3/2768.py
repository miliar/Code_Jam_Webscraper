#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
const int INF = 1000000000;
#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define rep(i,n) REP(i, 0, n)
map<int, vector<ll>> ans;
set<int> used;
ll pow(int temp, int n){
    ll res = 1;
    rep(i, n) res *= temp;
    return res;
}
ll diviser(ll n){
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return i;
    }
    return 0;
}
bool init(int nisin, int keta){
    vector<ll> divs;
    REP(i, 2, 11){
        ll num = 0;
        rep(j, keta) num += pow(i, j) * (1 & nisin >> j);
        ll div = diviser(num);
        if(div <= 0) return false;
        divs.push_back(div);
    }
    ans[nisin] = divs;
    return true;
}
void bfs(int coin, int n, int m){
    queue<int> que;
    que.push(coin);
    int sum = 0;
    if(init(coin, n)) sum++;
    while(!que.empty()){
        int now = que.front(); que.pop();
        REP(i, 1, n - 1){
            int bf = now;
            bf ^= (1 << i);
            if(used.count(bf) != 0) continue;
            if(init(bf, n)) sum++;
            if(sum >= m) return;
            que.push(bf);
            used.insert(bf);
        }
    }
    return;
}
int main(){
    ifstream ifs("C-small-attempt0.in");
    ofstream ofs("op_c.txt");
    
    int test;
    cin >> test;
    rep(casenum, test){
        int n, m; cin >> n >> m;
        int ip = (1 << n) - 1;
        used.insert(ip);
        bfs(ip, n, m);
        ofs << "Case #" << casenum + 1 << ": " << endl;
        int it = 0;
        for(auto k : ans){
            int temp = k.first;
            for(int i = n - 1; i >= 0; --i) ofs << (1 & temp >> i);
            ofs << ' ';
            vector<ll> kk = k.second;
            rep(i, kk.size()){
                ofs << kk[i];
                if(i == kk.size() - 1) ofs << endl; else ofs << ' ';
            }
        }
    }
    return 0;
}