#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>

using namespace std;

const int M = 1000002013;

long long N;

long long c(long long k) {
    return ((k + 1) * N - (k + 1) * k / 2) % M;
}

int main() {
    ifstream cin("/Users/mac/topcoder/input.txt");
    ofstream cout("/Users/mac/topcoder/output.txt");
    
    int NT, CT;
    cin >> NT;
    
    for (CT = 0; CT < NT; CT ++) {
        cout << "Case #" << (CT + 1) << ": ";
        
        int n, m;
        cin >> n >> m;
        N = n;
        
        long long b = 0;
        map<int, long long> a;
        
        for (int i = 0; i < m; i ++) {
            int oi, ei, pi;
            cin >> oi >> ei >> pi;
            
            a[oi] += pi;
            a[ei] -= pi;
            
            b += (c(ei - oi) * pi) % M;
        }
        
        long long res = 0;
        map<int, long long>::iterator it, bit;
        for (it = a.begin(); it != a.end(); it ++) {
            if (it->second < 0) {
                bit = it;
                while (it->second < 0) {
                    bit --;
                    long long d = min(bit->second, -it->second);
                    it->second += d;
                    bit->second -= d;
                    res += (c(it->first - bit->first) * d) % M;
                }
            }
        }
        
        cout << ((b - res) % M + M) % M << endl;
    }
    
    return 0;
}
