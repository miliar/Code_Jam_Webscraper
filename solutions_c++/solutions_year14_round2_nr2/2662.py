#include<iostream>

using namespace std;

main() {
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    long long int A, B, K;
    long long int T;
    long long int cnt;

    cin >> T;

    for(int t = 1; t <= T; t++){
        cnt = 0;
        cin >> A >> B >> K;
        for(int i = 0; i < A; i++) {
            for(int j = 0; j < B; j++) {
                if( (i&j)  < K ) cnt++;
            }
        }
        cout << "Case #" << t << ": " << cnt << endl;
    }
    return 0;
}

