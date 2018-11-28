#include<iostream>
#include<algorithm>
using namespace std;
const int BUF = 15;


int N;
int next[BUF];

void read() {
    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> next[i];
        --next[i];
    }
}


void rec(int fst, int prev, int nPpl, bool used[BUF], int &maxV) {

    maxV = max(maxV, nPpl);
    
    for (int i = 0; i < N; ++i) {
        
    }
}


void work(int cases) {
    int order[BUF];
    for (int i = 0; i < N; ++i) order[i] = i;
    
    int maxV = 1;
    do {

        for (int cnt = 2; cnt <= N; ++cnt) {
            for (int i = 0; i < cnt; ++i) {
                if (!(next[order[i]] == order[(i + 1) % cnt] || next[order[i]] == order[(i + cnt - 1) % cnt]))
                    goto _fail;
            }
            maxV = max(maxV, cnt);
        _fail:;
        }
    } while(next_permutation(order, order + N));
    
    cout << "Case #" << cases << ": " << maxV << endl;
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
