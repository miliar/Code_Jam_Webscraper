#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    string s;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> s;
        cout << "Case #" << i + 1 << ": ";
        int len = s.size();
        char c[] = { '-', '+' };
        bool turn = true;
        int o = 0;
        for (int j = len - 1; j >=0 ; j--) {
            if (c[turn] == s[j]) {
                continue;
            } else {
                o ++;
                turn = !turn;
            }
        }

        cout << o << endl;
    }
    return 0;
}
