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
        
        int n;
        cin >> n;
        vector<int> a(n, 0);
        for (int i = 0; i < n; i ++)
            cin >> a[i];
        
        vector<int> c = a;
        sort(c.begin(), c.end());
        
        int res = 0;
        
        int l = 0, r = n - 1;
        
        for (int i = 0; i < n; i ++) {
            int t = c[i];
//            cout << t << endl;
            
            int p = -1;
            for (int j = 0; j < n; j ++)
                if (a[j] == t) {
                    p = j;
                    break;
                }
            
            if (p - l < r - p) {
                while (p != l) {
                    swap(a[p], a[p - 1]);
                    p --;
                    res ++;
                }
                l ++;
            } else {
                while (p != r) {
                    swap(a[p], a[p + 1]);
                    p ++;
                    res ++;
                }
                r --;
            }
            
//            for (int j = 0; j < n; j ++)
//                cout << a[j] << " ";
//            cout << " = " << res << endl;

        }
        
        cout << res;
    }
    
    if (NT > 0)
        cout << endl;
    return 0;
}
