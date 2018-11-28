#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t, counter;
    string s;
    char cur;

    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        cur = 0;
        counter = 0;

        cin >> s;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != cur) {
                cur = s[i];
                counter++;
            }
        }
        if (cur == '-')
            cout << "Case #" << tc << ": " << counter;
        else
            cout << "Case #" << tc << ": " << counter-1;
        cout << endl;
    }
}
