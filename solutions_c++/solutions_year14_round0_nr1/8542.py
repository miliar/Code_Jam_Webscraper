#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    for (int i = 0; i < test; ++i) {
        int used[17];
        for (int j = 0; j < 17; ++j) {
            used[j] = 0;
        }
        int r;
        cin >> r;
        --r;
        for(int j = 0; j < 4; ++j) {
            for (int g = 0; g < 4; ++g) {
                int x;
                cin >> x;
                if (j == r) {
                    used[x] = 1;
                }
            }
        }
        cin >> r;
        --r;
        for(int j = 0; j < 4; ++j) {
            for (int g = 0; g < 4; ++g) {
                int x;
                cin >> x;
                if (j == r && used[x] == 1) {
                    used[x] = 1;
                } else {
                    used[x] = 0;
                }
            }
        }
        int cnt = 0;
        for (int j = 0; j < 17; ++j){
            if (used[j] == 1) {++cnt;  cerr << j << endl; } 
        }
        cout << "Case #" << i + 1 << ": ";
        if (cnt == 0){
            cout << "Volunteer cheated!" << endl;
        } else if (cnt == 1) {
            for (int j = 0; j < 17; ++j) {
                if (used[j] == 1) cout << j << endl;
            }
        }
        else {
            cout << "Bad magician!" << endl;
        }
    }           
        
}        