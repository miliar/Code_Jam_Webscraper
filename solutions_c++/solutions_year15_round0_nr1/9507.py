#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
    
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        
        int n;
        string s;
        
        cin >> n;
        cin >> s;
        
        int z = 0;
        int k = 0;
        
        for(int i = 0; i <= n; i++) {
            if(i > k) {
                z += i - k;
                k = i;
            }
            k += s[i] - '0';
        }
        
        printf("Case #%d: %d\n", t, z);
    }
}