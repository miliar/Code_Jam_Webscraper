#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

const string path = "/Users/mac/Documents/cpp/Code Jam/";

const string IMPOSSIBLE = "IMPOSSIBLE";

string recsmall(string s) {
    if (s.size() == 1)
        return s;
    
    string first = s.substr(0, s.size() / 2);
    string last = s.substr(s.size() / 2, s.size() / 2);
//    cout << first << " + " << last << endl;
    
    first = recsmall(first);
    last = recsmall(last);
    
    if (first > last)
        swap(first, last);
    
//    cout << " = " << first + " + " << last << endl;
    
    return first + last;
};

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        printf("Case #%d: ", CT);
        
        string res = "";
        
        int nn = n;
        while (nn > 0) {
            nn --;
            int s1 = (1 << nn) - r;
            int p1 = (1 << nn) - s;
            int r1 = (1 << nn) - p;
            
            if (s1 < 0 || p1 < 0 || r1 < 0) {
                res = IMPOSSIBLE;
                break;
            }
            
            s = s1;
            p = p1;
            r = r1;
        }
        
        if (res != IMPOSSIBLE) {
            if (s > 0)
                res = "S";
            if (p > 0)
                res = "P";
            if (r > 0)
                res = "R";
            
            for (int i = 0; i < n; i ++) {
                string t = "";
                for (int j = 0; j < res.size(); j ++) {
                    if (res[j] == 'R')
                        t += "RS";
                    else if (res[j] == 'S')
                        t += "SP";
                    else //if (res[j] == 'p')
                        t += "PR";
                }
                res = t;
            }
            
            res = recsmall(res);
        }
        
        printf("%s\n", res.c_str());
    }
    
    
    return 0;
}
