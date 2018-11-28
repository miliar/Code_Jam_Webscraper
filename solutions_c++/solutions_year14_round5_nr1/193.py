#include<iostream>
#include<numeric>
#include<cstdio>
using namespace std;
const int BUF = 1000005;

int N, p, q, r, s, val[BUF];

void read() {
    cin >> N >> p >> q >> r >> s;
    for (int i = 0; i < N; ++i)
        val[i] = (1LL * i * p + q) % r + s;
}


void work(int cases) {
    double ans = 0;
    int L = 0, R = 0;
    long long total = accumulate(val, val + N, 0LL);
    long long A = 0;
    long long B = val[0];
    long long C = accumulate(val + 1, val + N, 0LL);
    
    while (R < N) {
        while (R + 1 < N) {
            long long nexB = B + val[R + 1];
            long long nexC = C - val[R + 1];
            ans = max(ans, 1.0 * (total - max(A, max(nexB, nexC))) / total);
            
            if (B + val[R + 1] > max(A, C - val[R + 1])) {
                break;
            }
            
            B += val[R + 1];
            C -= val[R + 1];
            ++R;
        }
        
        ans = max(ans, 1.0 * (total - max(A, max(B, C))) / total);

        A += val[L];
        B -= val[L];
        ++L;
        
        if (L > R) {
            R = L;
            if (R < N) {
                B += val[R];
                C -= val[R];
            }
        }
    }

    printf("Case #%d: %.15lf\n", cases, ans);
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
