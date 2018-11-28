#include <iostream>
#include <cstdio>
#include <vector>


using namespace std;


bool test(int m, vector < int > &p) {
    for (int add_min = 0; add_min <= 1010; ++add_min) {
        if (add_min >= m) {
            break; 
        }
        int cmin = 0;
        for (int j = 0; j < (int) p.size(); ++j) {
            cmin += (p[j] + m - add_min - 1) / (m - add_min) - 1;  
        }
        if (cmin <= add_min) {
            return true;
        }
    }
    return false;
}  


int binsearch(vector < int > &p) {
    int r = (int) -1e9;
    for (int i = 0; i < (int) p.size(); ++i) {
        r = max(r, p[i]); 
    }
    int l = 0;
    for (; r - l > 1; ) {
        int m = (r + l) / 2;
        if (test(m, p)) {
            r = m; 
        } 
        else {
            l = m;
        }
    }
    return r;
}


int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int t;
    cin >> t;
    for (int q = 1; q <= t; ++q) {
        int d;
        cin >> d;
        vector < int > p (d);
        for (int i = 0; i < d; ++i) {
            cin >> p[i]; 
        } 
        cout << "Case #" << q << ": " << binsearch(p) << endl;
    }
    return 0;
}
