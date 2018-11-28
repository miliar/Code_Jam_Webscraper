#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int iter = 1; iter <= t; iter++) {
        long long int smax, count = 0;
        cin >> smax;
        string s;
        cin >> s;
        long long int present = (long long int)(s[0]-'0');
        for(int i=1;i<s.length();i++) {
            if (s[i] != '0' && present < i) {
                count += (i - present);
                present += (i - present);
            }
            present += (long long int) (s[i] - '0');

        }
        cout << "Case #" << iter << ": " << count << "\n";
    }
    return 0;
}
