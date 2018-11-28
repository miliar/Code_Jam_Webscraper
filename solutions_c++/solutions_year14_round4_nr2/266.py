#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
const int BUF = 1005;
const int INF = 1<<30;


int N, val[BUF];

void read() {
    cin >> N;
    for (int i = 0; i < N; ++i)
        cin >> val[i];
}


int rec(int L, int R, int dp[BUF][BUF], int nTh2nLargerL[BUF], int nTh2nLargerR[BUF]) {
    if (L > R) return 0;
    
    int &ret = dp[L][R];
    if (ret != -1) return ret;

    ret = INF;

    int cur = L + N - 1 - R;
    
    // putL
    ret = min(ret, rec(L + 1, R, dp, nTh2nLargerL, nTh2nLargerR) + nTh2nLargerL[cur]);

    // putR
    ret = min(ret, rec(L, R - 1, dp, nTh2nLargerL, nTh2nLargerR) + nTh2nLargerR[cur]);

    return ret;
}


void work(int cases) {
    static int dp[BUF][BUF];
    memset(dp, -1, sizeof(dp));
    
    pair<int, int> v2idx[BUF]; 
    for (int i = 0; i < N; ++i)
        v2idx[i] = make_pair(val[i], i);
    sort(v2idx, v2idx + N);

    int nTh2nLargerL[BUF], nTh2nLargerR[BUF];
    for (int i = 0; i < N; ++i) {
        int pos, cnt;
        
        pos = v2idx[i].second;
        cnt = 0;
        while (pos >= 0) {
            if (val[pos] > v2idx[i].first) ++cnt;
            --pos;
        }
        nTh2nLargerL[i] = cnt;
        
        pos = v2idx[i].second;
        cnt = 0;
        while (pos < N) {
            if (val[pos] > v2idx[i].first) ++cnt;
            ++pos;
        }
        nTh2nLargerR[i] = cnt;
    }
    
    

    cout << "Case #" << cases << ": " << rec(0, N - 1, dp, nTh2nLargerL, nTh2nLargerR) << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
