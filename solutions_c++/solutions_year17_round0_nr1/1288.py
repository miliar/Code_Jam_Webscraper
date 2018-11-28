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

double f(vector<double> a) {
    vector<double> p(a.size() + 1, 0);
    p[0] = 1;
    for (int i = 0; i < a.size(); i ++) {
        vector<double> pn(a.size() + 1, 0);
        for (int j = 0; j <= a.size(); j ++)
            pn[j] = p[j] * (1 - a[i]);
        for (int j = 1; j < a.size(); j ++)
            pn[j] += p[j - 1] * a[i];
        p = pn;
    }
    
    return p[a.size() / 2];
}

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
        char s[1001];
        int k;
        scanf("%s%d", s, &k);
        printf("Case #%d: ", CT);
        
        int res = 0;
        
        bool ok = true;
        int n = (int)strlen(s);
        for (int i = 0; i < n; i ++)
            if (s[i] == '-') {
                if (i + k - 1 >= n) {
                    ok = false;
                    break;
                }
                for (int j = 0; j < k; j ++)
                    s[i + j] = (s[i + j] == '-') ? '+' : '-';
                res ++;
            }
        
        if (!ok)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", res);
    }
    
    
    return 0;
}
