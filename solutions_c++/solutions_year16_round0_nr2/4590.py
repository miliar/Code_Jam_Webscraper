#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int tc = 0; tc < T; tc++) {
        cout << "Case #" << tc+1 << ": ";
        string s;
        cin >> s;
        int cnt = 0;
        for (int i = 0; i < (int)s.size()-1; i++) {
            if (s[i] == '+' && s[i+1] == '-') {
                cnt++;
            }
        }
        cout << cnt*2 + (s[0] == '-') << endl;
    }
    return 0;
}
