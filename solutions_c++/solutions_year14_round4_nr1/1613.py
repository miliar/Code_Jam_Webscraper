#include<vector>
#include<queue>
#include<iostream>
#include<algorithm>
using namespace std;

int solve(int N, int X) {
    int s[N];
    bool used[N];
    for (int i=0; i<N; ++i) {
        cin>>s[i];
        used[i] = false;
    }
    sort(s, s+N);
    int cnt = 0;
    for (int high = N-1; high >= 0; --high) {
        if (used[high]) continue;
        for (int i = 0; i < high; ++i) {
            if (used[i]) continue;
            if (s[i] + s[high] <= X) {
                cnt++;
                used[i] = used[high] = true;
                break;
            }
        }
    }

    return N-cnt;
}

int main() {
    int T, N, X;
    cin>>T;
    for (int i = 1; i <= T; ++i) {
        cin>>N>>X;
        cout<<"Case #"<<i<<": "<<solve(N, X)<<endl;
    }
}
