#include <iostream>

using namespace std;

int main() {
    int T, n, casen = 1, output;
    string s;
    cin >> T;
    while(T--) {
        output = 0;
        int temp = 0;
        cin >> n;
        cin >> s;

        for(int i = 1 ; i <= s.length() ; i++) {
            int digit = s.at(i-1) - '0';
            temp = temp + digit;
            if(temp < i) {
                output += (i - temp);
                temp = i;
            }
        }

        cout << "Case #" << casen++ << ": " << output << endl;
    }
    return 0;   
}
