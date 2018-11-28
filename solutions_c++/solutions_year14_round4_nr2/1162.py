#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T, N;
int A[1005];

void print(vector<int> va) {
    for (int i = 0; i < N; ++i) {
        cout << va[i] << " ";
    }
    cout << endl;
}

int power(int N) {
    int rst = 1;
    for (int i = 0; i < N; ++i) {
        rst = rst * 2;
    }
    return rst;
}

int solve() {
    vector<int> va(N), vb(N);
    int left, right;
    long ans = 0, best = -1;
    for (int i = 0; i < N;  ++i) {
        for (int j = 0; j < power(N - 1); ++j) {
            for (int k = 0; k < N; ++k) {
                vb[k] = A[k];
                va[k] = A[k];
            }
            sort(va.begin(), va.end());
            sort(vb.begin(), vb.end());
            va[i] = vb[N - 1];
            left = 0; right = N - 1;
            for (int k = 0; k < N - 1; ++k) {
                if (((j >> k) & 1) == 0) {
                    va[left++] = vb[k];
                } else {
                    va[right--] = vb[k];
                }

            }
            if (left == i && right == i) {
                for (int k = 0; k < N; ++k)
                    vb[k] = A[k];

                sort(va.begin(), va.begin() + i);
                sort(va.begin() + i + 1, va.end());
                reverse(va.begin() + i + 1, va.end());

                ans = 0;
                for (int k = 0; k < N; ++k) {
                    int w;
                    for (w = k; w < N; ++w) {
                        if (vb[w] == va[k]) break;
                    }
                    ans += w - k;
                    for (int z = w; z >= k + 1; --z) {
                        vb[z] = vb[z - 1];
                    }
                }
                if (best == -1 || ans < best) {
                    best = ans;
                }

            }
        }
    }
    return best;
}

int main(int argc, char *argv[]) {
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> N;
        for (int j = 0; j < N; ++j) {
            cin >> A[j];
        }
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }
    return 0;
}
