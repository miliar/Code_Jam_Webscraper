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

double p[210][2];

double middle(vector<double> a) {
    p[0][0] = 1;
    for (int i = 0; i < a.size(); i ++) {
        int next = (i + 1) % 2;
        
        for (int j = 0; j <= i; j ++)
            p[j][next] = p[j][i % 2] * (1 - a[i]);
        p[i + 1][next] = 0;
        
        for (int j = 0; j <= i; j ++)
            p[j + 1][next] += p[j][i % 2] * a[i];
    }
    return p[a.size() / 2][a.size() % 2];
}

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
        int n, k;
        scanf("%d%d", &n, &k);
        printf("Case #%d: ", CT);
        
        vector<double> a(n);
        
        for (int i = 0; i < n; i ++)
            scanf("%lf", &a[i]);
        
        double b = 0;
        for (int i = 0; i < (1 << a.size()); i ++) {
            vector<double> t;
            for (int j = 0; j < a.size(); j ++)
                if (i & (1 << j))
                    t.push_back(a[j]);
            
            if (t.size() == k)
                b = max(b, middle(t));
        }
        
        cout << b << endl;
    }
    
    
    return 0;
}
