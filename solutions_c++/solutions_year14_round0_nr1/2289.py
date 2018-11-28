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
        
        vector<int> a, b;
        int r, t;
        
        cin >> r;
        for (int i = 0; i < 4; i ++)
            for (int j = 0; j < 4; j ++) {
                cin >> t;
                if (i == (r - 1))
                    a.push_back(t);
            }
        
        cin >> r;
        for (int i = 0; i < 4; i ++)
            for (int j = 0; j < 4; j ++) {
                cin >> t;
                if (i == (r - 1))
                    b.push_back(t);
            }
        
        vector<int> c;
        for (int i = 0; i < a.size(); i ++)
            for (int j = 0; j < b.size(); j ++)
                if (a[i] == b[j])
                    c.push_back(a[i]);
        
        if (c.size() > 1)
            cout << "Bad magician!";
        if (c.size() == 0)
            cout << "Volunteer cheated!";
        if (c.size() == 1)
            cout << c[0];
    }
    
    if (NT > 0)
        cout << endl;
    return 0;
}
