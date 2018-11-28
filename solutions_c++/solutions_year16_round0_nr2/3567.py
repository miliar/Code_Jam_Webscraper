#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int sol = 0, last = 0;
        bool start = true, down = false;
        string s;
        cin >> s;
        s = s + '+';
        for (char c : s) {
            if (c == '+') {
                if (down) {
                    if (start)
                        sol++;
                    else
                        sol += 2;
                }
                down = false;
                start = false;
            } else
                down = true;
        }
        cout << "Case #" << t + 1 << ": " << sol << endl;
    }
    return 0;
}
