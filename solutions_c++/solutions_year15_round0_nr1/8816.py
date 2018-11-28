#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        int d;
        cin >> d;
        
        string shy;
        cin >> shy;
        
        int count = 0, answer = 0;
        for (int i = 0; i != shy.length(); ++i) {
            if (shy[i] != '0' && count < i) {
                answer += i - count;
                count = i;
            }
            count += shy[i] - '0';
        }
        
        cout << "Case #" << test + 1 << ": " << answer << "\n";
    }
    
    return 0;
}