#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ullong;

int main () {
    ios::sync_with_stdio(false);

    int T;
    ullong N;
    
    ullong mask = 0;

    for (int i = 0; i < 10; i++) {
        mask <<= 1; mask |= 1ull;
    }

    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> N;
        
        if (N == 0) {
            cout << "Case #" << i << ": INSOMNIA\n";
            continue;
        }
        
        ullong j = 1, check = 0;
        while (true) {
            stringstream ss;
            ss << N * j;
            string s;
            ss >> s;
            
            for (size_t k = 0; k < s.size(); k++)
                check |= 1ull << ((int)(s[k]-'0'));
            if (check == mask)
                break;
            j++;
        }
        
        cout << "Case #" << i << ": " << N * j << "\n";   
    }
}
