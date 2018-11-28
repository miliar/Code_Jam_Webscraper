#include <iostream>
#include <string>
#include <set>
#include <sstream>

using namespace std;

string itos(int q) {
  stringstream A;
  A << q; 
  string s; 
  A >> s; 
  return s; 
}

void solve(int ind) {
    // input
    int irow, n;
    // first layout
    cin >> irow;
    set<int> row;
    for (int i = 1; i <= 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> n;
            if (i == irow) {
                row.insert(n);
            }
        }
    }
    // second layout
    cin >> irow;
    int nsame = 0;
    int vsame = -1;
    for (int i = 1; i <= 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> n;
            if (i == irow) {
                if (row.find(n) != row.end()) {
                    ++nsame;
                    vsame = n;
                }
            }
        }
    }
    string res;
    if (nsame == 0) {
        res = "Volunteer cheated!";
    } else
        if (nsame > 1) {
            res = "Bad magician!";
        } else {
            res = itos(vsame);
        }
    
    // output
    cout << "Case #" << ind << ": " << res << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        solve(i);
    }
}