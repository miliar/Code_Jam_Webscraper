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
vector<vector<int> > square_grid;

int try_magic() {
    int q1, q2, ans, card, b;
    ans = 0;
    cin >> q1;
    --q1;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> square_grid[i][j];
        }
    }
    cin >> q2;
    --q2;
    for (int i = 0; i < q2; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> b;
        }
    }
    for (int j = 0; j < 4; ++j) {
        cin >> card;
        if (count(square_grid[q1].begin(), square_grid[q1].end(), card) != 0) {
            if (ans == 0) ans = card;
            else ans = -1;
        }
    }
    for (int i = q2+1; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> b;
        }
    }
    return ans;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    square_grid.assign(4, vector<int>(4, 0));
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int ans = try_magic();
        switch(ans) {
            case -1:
                cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
                break;
            case 0:
                cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
                break;
            default:
                cout << "Case #" << i+1 << ": " << ans << endl;
                break;
        }
    }
    return 0;
}
