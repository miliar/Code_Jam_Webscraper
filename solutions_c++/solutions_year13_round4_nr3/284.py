#include <iostream>

using namespace std;

int T;
int N;
int A[2000];
int B[2000];
int X[2000];
int X2[2000];

int U[2000];

int M[2000];

bool v;

bool kelpaa(int k) {
    for (int i = 0; i <= k; i++) {
        int t = 1;
        for (int j = 0; j < i; j++) {
            if (X[j] < X[i] && U[j]+1 > t) t = U[j]+1;
        }
        U[i] = t;
        if (A[i] != U[i]) return false;
    }
    return true;
}

bool kelpaab(int k) {
    int p = 0;
    for (int i = 0; i < N; i++) {
        X2[i] = X[i];
    }
    for (int i = N-1; i > k; i--) {
        p++;
        while (M[p]) p++;
        X2[i] = p;
    }
    for (int i = N-1; i >= 0; i--) {
        int t = 1;
        for (int j = N-1; j > i; j--) {
            if (X2[j] < X2[i] && U[j]+1 > t) t = U[j]+1;
        }
        U[i] = t;
        if (i <= k && B[i] > U[i]) return false;
    }
    return true;
}


bool loppu() {
    for (int i = N-1; i >= 0; i--) {
        int t = 1;
        for (int j = N-1; j > i; j--) {
            if (X[j] < X[i] && U[j]+1 > t) t = U[j]+1;
        }
        U[i] = t;
        if (B[i] != U[i]) return false;
    }
    return true;
}

void etsi(int k) {
    if (v) return;
    if (k == N) {
        if (loppu()) {
            for (int i = 0; i < N; i++) {
                cout << X[i] << " ";
            }
            v = true;
        }
        return;
    }
    for (int i = B[k]; i <= N; i++) {
        if (v) return;
        X[k] = i;
        if (M[i]) continue;
        if (!kelpaa(k)) continue;
        if (!kelpaab(k)) continue;
        M[i] = 1;
        etsi(k+1);
        M[i] = 0;
    }
}

void laske(int n) {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < N; i++) {
        cin >> B[i];
    }
    cout << "Case #" << n << ": ";
    v = false;
    etsi(0);
    cout << endl;
}

int main() {
    cin >> T;
    for (int i = 0; i < T; i++) {
        laske(i+1);
    }
}