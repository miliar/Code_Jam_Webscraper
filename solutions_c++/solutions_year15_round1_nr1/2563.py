#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

int m[1050];

int main(int argc, const char * argv[]) {
    freopen("A-large.in", "r",stdin);
    freopen("A-large.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int cn = 1; cn <= T; cn++) {
        int m1 = 0, m2 = 0, N;
        cin >> N;
        int md = 0;
        cin >> m[0];
        for (int i = 1; i < N; i++) {
            cin >> m[i];
            md = max(m[i-1] - m[i], md);
        }
        
        
        for (int i = 0; i < N-1; i++) {
            if (m[i+1] < m[i]) m1 += (m[i]-m[i+1]);
            
            m2 += min(m[i], md);
        }
        
     
        cout << "Case #" << cn << ": " << m1 << ' ' << m2 << endl;
    }
    
    return 0;
}
