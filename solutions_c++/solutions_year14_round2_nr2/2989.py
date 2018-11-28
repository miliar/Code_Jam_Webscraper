#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<cstdio>
#include<string>

using namespace std;

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

int T, N;

int try_magic() {
    long int ans = 0;
	long int a, b, c;
	cin >> a;
	cin >> b;
	cin >> c;
    if (a < b) {
        a = b + a;
        b = a - b;
        a = a - b;
    }
    ans = a + b - 1;
    for (int i = 1; i < a; i++)
        for (int j = 1; j < b; j++)
            if ((i & j) < c)
                ++ans;
    return ans;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int ans = try_magic();
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
