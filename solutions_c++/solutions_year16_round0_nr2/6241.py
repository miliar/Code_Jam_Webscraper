#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    string s;
    cin >> n;
    getline(cin,s);
    for (int i = 0; i < n; i++) {
        getline(cin,s);
        int count = 0;
        while (s.find("-") != string::npos) {
            int pos = s.rfind('-');
            for (int j = 0; j <= pos; j++) {
                if (s[j] == '+')
                    s[j] = '-';
                else s[j] = '+';
            }
            count++;
        }
        cout << "Case #" << i + 1 << ": " << count << endl;
    }
    return 0;
}