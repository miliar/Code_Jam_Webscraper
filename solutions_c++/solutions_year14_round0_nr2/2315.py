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
        
        long double c, f, x, s = 2.0, dt = 0.0;
        cin >> c >> f >> x;
        
        long double m = x / s;
        
        while (true) {
            dt += c / s;
            s += f;
            long double nm = dt + x / s;
            if (nm < m)
                m = nm;
            else
                break;
        }
        char buf[1000];
        sprintf(buf, "%.8Lf", m);
        cout << buf;
    }
    
    if (NT > 0)
        cout << endl;
    return 0;
}
