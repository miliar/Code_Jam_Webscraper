#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    string s;
    cin >> t;

    for(int c = 1 ; c <= t ; c++) {
        cin >> s;
        int cnt = 0;
        if(s[s.length() - 1] == '-')
            cnt++;
        for(int i = 0 ; i < s.length() - 1 ; i++)
            if(s[i] != s[i + 1])
                cnt++;
        cout << "Case #" << c << ": " << cnt << endl;
    }

    return 0;
}
