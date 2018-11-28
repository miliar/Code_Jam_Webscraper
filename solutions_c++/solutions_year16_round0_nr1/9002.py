#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

long long T, a[10], N;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    for(long long t = 0; t < T; t++){
        cin >> N;
        cout << "Case #" << t + 1 << ": ";
        if(N == 0){
            cout << "INSOMNIA" << endl;
            continue;
        }
        int b = 0;
        fill(a, a + 10, 0);
        long long n;
        for(n = N; n <= 10000000 && b == 0; n += N){
            long long c = n;
            for(long long c = n; c > 0; c /= 10){
                a[c % 10] = 1;
            }
            b = 1;
            for(int i = 0; i < 10; i++){
                if(a[i] == 0){
                    b = 0;
                    break;
                }
            }
        }
        n -= N;
        if(b == 0){
            cout << "INSOMNIA" << endl;
        } else cout << n << endl;
    }
    return 0;
}

