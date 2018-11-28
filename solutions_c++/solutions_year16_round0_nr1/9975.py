#include <iostream>
#include <unordered_set>
#include <cstring>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    bool digits[10];
    int tc, N, num, ans;
    
    cin >> tc;
    
    for(size_t t = 1; t <= tc; t++) {
        unordered_set<long long> set;
        memset(digits, 0, sizeof(digits));
        int seen = 0;
        cin >> N;
        
        cout << "Case #" << t << ": ";
        
        if(N == 0) {
            cout << "INSOMNIA\n";
            continue;
        }
        
        for(int i = 1; seen != 10; i++) {
            ans = num = i * N;
            if(!set.count(num)) {
                set.insert(num);
                while(num != 0) {
                   int digit = num % 10;
                    if(!digits[digit]) {
                        seen++;
                        digits[digit] = 1;
                    }
                    num /= 10;
                }
            }
        }
        cout << ans << "\n";
    }
}