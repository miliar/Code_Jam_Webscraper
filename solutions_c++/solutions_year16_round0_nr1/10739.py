#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool D[10];


int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t) {
        int N;
        cin >> N;

        if(N == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }

        for(int i=0; i<10; i++) D[i] = false;
        int c = 0;
        int n = 0;
        bool stop = false;
        while(!stop) {
            n += N;
            int k = n;
            while(k > 0) {
                int d = k%10;
                if(!D[d]) {
                    D[d] = true;
                    c++;
                    if(c == 10) stop = true;
                }
                k /= 10;
            }
        }
        printf("Case #%d: %d\n", t, n);

    }


    return 0;
}
