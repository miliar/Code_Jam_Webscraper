#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    long long N;
    cin >> T;
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        cin >> N;
        if (!N) {
            cout << "Case #" << caseNum << ": " << "INSOMNIA" << endl;
            continue;
        }
        vector<bool> seen(10, false);
        int count = 0;
        long long val = 0;
        while (count < 10) {
            val += N;
            long long n = val;
            while(n) {
                int digit = n % 10;
                if (!seen[digit]) ++count;
                seen[digit] = true;
                n /= 10;
            }
        }
        cout << "Case #" << caseNum << ": " << val << endl;
    }
        
}
