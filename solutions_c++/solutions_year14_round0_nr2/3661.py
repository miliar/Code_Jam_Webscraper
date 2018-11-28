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

int T;
double C, F, X;

double try_magic() {
    cin >> C >> F >> X;
    double ans = 0, inflow = 2, t1 = 0, t2 = 0;
    while (true) {
        t1 = X*(1.0/inflow);
        t2 = C*(1.0/inflow) + X*(1.0/(inflow + F));
        if (t1 >= t2) {
            ans += C*(1.0/inflow);
            inflow += F;
        }
        else break;
    }
    ans += t1;
    return ans;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int i = 0; i < T; ++i) {
        double ans = try_magic();
        //cout << "Case #" << i+1 << ": ";
        printf("Case #%d: ", i+1);
        printf("%7.7f\n", ans);
    }
    return 0;
}
