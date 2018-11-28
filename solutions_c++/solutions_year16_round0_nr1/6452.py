// Author: Bony Roopchandani

#include <bits/stdc++.h>
using namespace std;

void clearGlobals(void) {}

bool ok(int N, bool* Mp, int& cnt) {
    while(N > 0) {
        int digit = N % 10;
        if(!Mp[digit]) {
            Mp[digit] = true;
            cnt += 1;
        }
        N /= 10;
    }
    return (cnt == 10);
}

void solve(void) {
    long long N; cin>>N;
    if(N == 0) {
        cout<<"INSOMNIA"<<'\n';
        return;
    }
    bool Mp[12]{};
    int cnt = 0;
    for(long long i = 1; ; i++) {
        if(N*i >= 1e18) {
            break;
        }
        if(ok(N*i, Mp, cnt)) {
            cout<<N*i<<'\n';
            return;
        }
    }
    cout<<"INSOMNIA"<<'\n';
    clearGlobals();
}

int main(void) {
    ios_base::sync_with_stdio(false);
    int testCase;
    cin>>testCase;
    for(int tc=1; tc<=testCase; tc++) {
        cout<<"Case #"<<tc<<": "; solve();
    }
    return (EXIT_SUCCESS);
}
