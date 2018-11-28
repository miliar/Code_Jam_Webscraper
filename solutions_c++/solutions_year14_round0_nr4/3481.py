#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<cstdio>

using namespace std;

/**
freopen("file.txt", "w", stdout) - вывод
<stdio.h>
freopen("file.txt", "r", stdin) - ввод
freopen("input.txt", "r", stdin)
*/

template<typename T>
void PrintMt(vector<vector<T> > &vc) {
    for (int i = 0; i < vc.size(); ++i) {
        for (int j = 0; j < vc[i].size(); ++j)
            cout << vc[i][j] <<" ";
        cout << endl;
    }
    cout << endl;
}

template<typename T>
void PrintV(vector<T> &vc) {
    for (int i = 0; i < vc.size(); ++i)
        cout << vc[i] << " ";
    cout << endl;
}

int T, N, z, y;

void cheat_play(vector<double> n, vector<double> k) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j)
            if (n[i] > k[j]) {
                ++y;
                k[j] = 2;
                break;
            }
    }
}

void fair_play(vector<double> n, vector<double> k) {
    for (int i = 0; i < N; ++i) {
    bool flag = false;
        for (int j = 0; j < N; ++j)
            if (n[i] < k[j]) {
                k[j] = 0;
                flag = true;
                break;
            };
        if (!flag) ++z;
    }
}

void try_magic() {
    y = 0; z = 0;
    cin >> N;
    double c;
    vector<double> n, k;
    for (int i = 0; i < N; ++i) {
        cin >> c;
        n.push_back(c);
    }
    for (int i = 0; i < N; ++i) {
        cin >> c;
        k.push_back(c);
    }
    sort(n.begin(), n.end());
    sort(k.begin(), k.end());
    fair_play(n , k);
    cheat_play(n , k);
}

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int i = 0; i < T; ++i) {
        try_magic();
        cout << "Case #" << i+1 << ": " << y << " " << z << endl;
    }
    return 0;
}
