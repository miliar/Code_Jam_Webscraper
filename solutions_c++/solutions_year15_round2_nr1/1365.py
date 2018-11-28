#include <bits/stdc++.h>

using namespace std;

ifstream f("a.in");
//ofstream g("a.out");

const int NMAX = 1e6+1;
const int INF = (1<<30);

queue<int> q;
int cnt[NMAX];

int reverseNr(int x){
    int inv = 0;
    while(x){
        inv = inv * 10 + x % 10;
        x /= 10;
    }
    return inv;
}

void preprocess(){
    for(int i=1; i<NMAX; ++i) cnt[i] = 0;
    q.push(1);
    cnt[1] = 1;
    for(; !q.empty(); ){
        int node = q.front();
        q.pop();
        //cout << node << "\n";
        if (node + 1 < NMAX && cnt[node+1] == 0){
            cnt[node+1] = cnt[node]+1;
            q.push(node+1);
        }
        int reverseX = reverseNr(node);
        //cout << reverseX << ""
        if (reverseX < NMAX && cnt[reverseX] == 0){
            cnt[reverseX] = cnt[node] + 1;
            q.push(reverseX);
        }
    }
}

void scrie(int testNo, int ans){
    printf("Case #%d: %d\n", testNo, ans);
}

int main(){
    freopen("a.out", "w", stdout);
    int t;

    preprocess();
    f >> t;
    //cout << t << "\n";
    for(int i=1; i<=t; ++i){
        int n; f >> n;
        scrie(i, cnt[n]);
    }
    return 0;
}
