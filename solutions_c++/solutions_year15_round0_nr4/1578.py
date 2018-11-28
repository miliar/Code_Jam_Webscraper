#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    fstream cin, cout;
    cin.open("input.txt", ios_base::in);
    cout.open("output.txt", ios_base::out);
    
    int t, ti;
    int x, r, c, res;
    int i, j;
    string res_sam[2] = {"GABRIEL", "RICHARD"};
    
    cin >> t;
    for (ti = 1; ti <= t; ++ti) {
        res = 0;
        cin >> x >> r >> c;
        
        if (r < c) swap(r, c);
        if ((r * c) % x != 0) res = 1;
        if (r < x) res = 1;
        if (c <= x - 2) res = 1;
        
        cout << "Case #" << ti << ": " << res_sam[res] << endl;
    }
    cout.close();
}
