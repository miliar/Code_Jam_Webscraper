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

const int M = 1000000007;

int l, res, m, n;
vector<string> s;
vector<int> a;

int count(vector<string> s) {
    vector<string> t;
    for (int i = 0; i < s.size(); i ++)
        for (int j = 0; j <= s[i].size(); j ++) {
            string p = s[i].substr(0, j);
            
            bool exist = false;
            for (int k = 0; k < t.size(); k ++)
                if (t[k] == p) {
                    exist = true;
                    break;
                }
            if (!exist)
                t.push_back(p);
        }
    return (int)t.size();
}

void rec(int i) {
    if (i == m) {
        int p = 0;
        for (int j = 0; j < n; j ++) {
            vector<string> t;
            for (int k = 0; k < m; k ++)
                if (a[k] == j)
                    t.push_back(s[k]);
            p += count(t);
        }
        if (p == l) {
            res ++;
        }
        if (p > l) {
            res = 1;
            l = p;
        }
        return;
    }
    for (int j = 0; j < n; j ++) {
        a[i] = j;
        rec(i + 1);
    }
}

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
        
        cin >> m >> n;
        vector<string> t(m);
        for (int i = 0; i < m; i ++)
            cin >> t[i];
        
        vector<int> t2(m, -1);
        a = t2;
        
        s = t;
        l = res = 0;
        
        rec(0);
        
        cout << l << " " << res % M;
    }
    
    if (NT > 0)
        cout << endl;
    return 0;
}
