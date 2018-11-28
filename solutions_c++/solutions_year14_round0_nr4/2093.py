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
        
        vector<double> a(n, 0), b(n, 0);
        
        for (int i = 0; i < n; i ++)
            cin >> a[i];
        for (int i = 0; i < n; i ++)
            cin >> b[i];
        
        sort(a.begin(), a.end());
        reverse(a.begin(), a.end());
        
        sort(b.begin(), b.end());
        reverse(b.begin(), b.end());
        
        int p = 0, bp = n - 1;
        for (int i = n - 1; i >= 0; i --) {
            while (bp >= 0 && b[bp] < a[i])
                bp --;
            if (bp < 0)
                p ++;
            bp --;
        }
        
        int s = 0;
        for (int i = n - 1; i >= 0; i --) {
            if (a[i] < b[i]) {
                a.pop_back();
                reverse(b.begin(), b.end());
                b.pop_back();
                reverse(b.begin(), b.end());
            } else {
                a.pop_back();
                b.pop_back();
                s ++;
            }
        }
        
        cout << s << " " << p;
    }
    
    if (NT > 0)
        cout << endl;
    return 0;
}
