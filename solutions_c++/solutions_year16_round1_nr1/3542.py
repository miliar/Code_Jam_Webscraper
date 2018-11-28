#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        string s, temp;
        cin >> s;
        temp += s[0];
        for(int i = 1; i < s.length(); i++) {
            if(s[i] >= temp[0]) {
                temp = s[i] + temp;
            }
            else {
                temp += s[i];
            }
        }
        cout << "Case #" << t << ": " << temp << "\n";
    }
    return 0;
}
