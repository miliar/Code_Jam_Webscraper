#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

char m[40015];
long long length;

char multiply(char a, char b)
{
    bool zn = 0;
    char ans;

    if (a >= 'a' && b < 'a' || b >= 'a' && a < 'a') zn = 1; // отрицательно

    if (a < 'a')a += 'a'-'A';
    if (b < 'a')b += 'a'-'A';

    ans = 'a';

    if (a == 'a') ans = b;
    if (b == 'a') ans = a;

    if (a == b && a != 'a') ans = 'A';

    if (a == 'i' && b == 'j') ans = 'k';
    if (a == 'j' && b == 'i') ans = 'K';

    if (a == 'i' && b == 'k') ans = 'J';
    if (a == 'k' && b == 'i') ans = 'j';

    if (a == 'j' && b == 'k') ans = 'i';
    if (a == 'k' && b == 'j') ans = 'I';

    if (zn) {
        if (ans < 'a') ans += 'a'-'A';
        else ans -= 'a'-'A';
    }

    return ans;
}

char divide (char a, char b)                // a * ans == b
{
    bool zn = 0;
    char ans;
    if (a >= 'a' && b < 'a' || b >= 'a' && a < 'a') zn = 1; // отрицательно

    if (a < 'a')a += 'a'-'A';
    if (b < 'a')b += 'a'-'A';

    if (a == 'a') ans = b;
    if (a != 'a' && b == 'a') ans = a - 'a' + 'A';
    if (a == b) ans = 'a';
    if (a == 'i' && b == 'k') ans = 'j';
    if (a == 'i' && b == 'j') ans = 'K';
    if (a == 'j' && b == 'k') ans = 'I';
    if (a == 'j' && b == 'i') ans = 'k';
    if (a == 'k' && b == 'j') ans = 'i';
    if (a == 'k' && b == 'i') ans = 'J';

    if (zn) {
        if (ans < 'a') ans += 'a'-'A';
        else ans -= 'a'-'A';
    }

    return ans;
}

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    //*
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        long long l, x;
        cin >> l >> x;
        length = l * x;

        string str;
        cin >> str;
        str += str;
        str += str;

        for (int i = 0; i < str.size(); i++) {

            if (i == 0) m[i] = str[i];
            else {
                m[i] = multiply(m[i-1], str[i]);
            }
        }

        long long mod = (length-1) % (4*l);   // not sure
        int cycle_cnt = 0;
        bool ans = false;

        for (int i = 0; i < str.size() && i < length && !ans; i++) {
            if (m[i] == 'i') {
                for (int j = i+1; cycle_cnt < 3  && cycle_cnt * str.size() + j < length && !ans; j++) {       // TL
                    if (j == str.size()) {
                        j = 0;
                        cycle_cnt++;
                    }

                    if (divide(m[i], m[j]) == 'j') {

                        if (j < mod) {
                            if (divide(m[j], m[mod]) == 'k') ans = true;
                        }
                        else {
                            char a = divide(m[j], m[str.size()-1]);
                            char b = m[mod];
                            if (multiply(a, b) == 'k') ans = true;
                        }
                    }
                }
            }
        }

        cout << "Case #" << test << ": ";
        if (ans)cout << "YES";
        else cout << "NO";
        cout << endl;
        //*/
    }

    return 0;
}

