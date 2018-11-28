#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <algorithm>
#include <cstring>
#include <fstream>

using namespace std;

int main() {
    const string PATH_BASE = "/Users/mac/topcoder/";
    int NT, CT;
    
    ifstream cin(PATH_BASE + "input.txt");
    ofstream cout(PATH_BASE + "output.txt");
    
    cin >> NT;
    for (CT = 0; CT < NT; CT ++) {
        if (CT > 0)
            cout << endl;
        cout << "Case #" << (CT + 1) << ": ";
        
        int n, x;
        cin >> n >> x;
        vector<int> s(n, 0);
        for (int i = 0; i < n; i ++)
            cin >> s[i];
        
        sort(s.begin(), s.end());
        vector<bool> a(n, false);
        int p = n - 1;
        
        int r = 0;
        
        while (p >= 0) {
            if (a[p]) {
                p --;
                continue;
            } else {
                r ++;
                a[p] = true;
                int v = p - 1;
                while (v >= 0) {
                    if (!a[v] && s[p] + s[v] <= x)
                        break;
                    v --;
                }
                if (v >= 0)
                    a[v] = true;
                p --;
            }
        }
        cout << r;
    }
    
    if (NT > 0)
        cout << endl;
    return 0;
}
