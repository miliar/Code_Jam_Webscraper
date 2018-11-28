#include<iostream>
#include<algorithm>
using namespace std;
const int BUF = 10005;


int N, limit, v[BUF];

void read() {
    cin >> N >> limit;
    for (int i = 0; i < N; ++i)
        cin >> v[i];
}


void work(int cases) {
    sort(v, v + N);
    
    int cnt = 0;
    bool used[BUF] = {};
    
    for (int i = 0; i < N; ++i) {
        if (used[i])
            continue;
        
        int lastIdx = -1;
        for (int j = i + 1; j < N; ++j) {
            if (v[i] + v[j] > limit)
                break;
            if (used[j])
                continue;
            lastIdx = j;
        }

        used[i] = true;
        if (lastIdx != -1)
            used[lastIdx] = true;
        ++cnt;
    }

    cout << "Case #" << cases << ": " << cnt << endl;
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
