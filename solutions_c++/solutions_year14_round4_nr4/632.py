#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>


using namespace std;

int cnt[10000];
int Max = 0;
int Bor[10000][30];
int Size = 1;

void Add(string s) {
    int v = 0;
    for (int i = 0; i < (int)s.size(); ++i) {
        if (Bor[v][s[i] - 'A'] != -1) {
            v = Bor[v][s[i] - 'A'];
        } else {
            for (int j = 0; j < 30; ++j) {
                Bor[Size][j] = -1;
            }
            Bor[v][s[i] - 'A'] = Size;
            v = Size;
            ++Size;
        }
    }
}

vector <string> S;

vector <int> A;
int K;

void Do() {
    int Sum = 0;
    for (int i = 0; i < K; ++i) {
        Size = 1;
        for (int j = 0; j < 30; ++j) {
            Bor[0][j] = -1;
        }
        int fl = 0;
        for (int j = 0; j < (int)S.size(); ++j) {
            if (A[j] == i){
                Add(S[j]);
                fl = 1;
            }
        }
        if (fl == 0) return;
        Sum += Size;
    }
    if (Sum > Max) Max = Sum;
    cnt[Sum]++;
}

void bt(int i) {
    if (i == (int)S.size())  {
        Do();
    } else {
        for (int j = 0; j < K; ++j) {
            A[i] = j;
            bt(i + 1);
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; ++test) {
        int M, N;
        scanf("%d%d", &M, &N);
        K = N;
        S.resize(M);
        A.resize(M);
        Size = 1;
        for (int j = 0; j < 30; ++j) {
            Bor[0][j] = -1;
        }
        Max = 0;
        for (int i = 0; i < 1000; ++i){
            cnt[i] = 0;
        }
        for (int i = 0; i < M; ++i) {
            cin >> S[i];
        }
        bt(0);
        printf("Case #%d: %d %d\n", test + 1, Max, cnt[Max]);
    
    }
}