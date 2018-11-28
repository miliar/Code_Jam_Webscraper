#include <cstdio>
#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>
#include <vector>

using namespace std;

const int U = 1;
const int I = 2;
const int J = 3;
const int K = 4;

int g(int a,int b) {
    if (a == U) return b;
    if (b == U) return a;

    if (a == b) return -U;

    bool sw = false;
    if (a > b) {
        sw = true;
        swap(a,b);
    }

    int ans = 0;
    if (a == I and b == J) ans = K;
    if (a == I and b == K) ans = -J;
    if (a == J and b == K) ans = I;

    if (sw) {
        ans = -ans;
    }

    return ans;
}
int mult(int a,int b) {
    int c = g(abs(a),abs(b));

    if (a < 0 xor b < 0) {
        c = -c;
    }
    return c;
}

int f(char c) {
    if (c == 'i') return I;
    if (c == 'j') return J;
    if (c == 'k') return K;

    assert(false);
}
int mem[10000][10000];

int eval(int a,int b) {
    assert(a <= b);
    return mem[a][b];
}

int N;
vector<int> vc;
string solve() {
    string line;
    int L,X;
    cin >> L >> X >> line;
    vector<int> vc2;
    vc.clear();

    for (int i = 0; i < L; i++) {
        vc.push_back(f(line[i]));
        vc2.push_back(f(line[i]));
    }
    for (int i = 2; i <= X; i++) {
        vc.insert(vc.begin(), vc2.begin(), vc2.end());
    }

    int len = vc.size();
    for (int i = 0; i < len; i++) {
        mem[i][i] = vc[i];
        for (int j = i + 1; j < len; j++) {
            mem[i][j] = mult(mem[i][j-1], vc[j]);
        }
    }


    vector<int> is;
    for (int i = 0; i < len; i++) {
        if (eval(0, i) == I) {
            is.push_back(i);
        }
    }

    int islen = is.size();
    int ii;
    for (int i = len - 1; i >= 0; i--) {
        if (eval(i, len - 1) != K) {
            continue;
        }

        for (int j = 0; j < islen; j++) { ii = is[j];
            if ( ii + 1 >= i) {
                break;
            }

            if (eval(ii + 1, i - 1) == J) {
                return "YES";
            }
        }
    }

    return "NO";
}

int main() {
    int NC;
    cin >> NC;
    for (int i = 1; i <= NC; i++) {
        string ans = solve();
        printf("Case #%d: %s\n", i, ans.c_str());
    }
}