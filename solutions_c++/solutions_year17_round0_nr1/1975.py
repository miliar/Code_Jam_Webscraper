#include<iostream>
#include<string>
using namespace std;

void flip(string &s, int st, int l) {
    for (int i = st; i < st + l; i++) {
        if (s[i] == '-')
            s[i] = '+';
        else
            s[i] = '-';
    }
}

int main()
{
    int t;
    cin >> t;
    for (int cs = 1; cs <= t; cs++) {
        string s;
        int k;
        cin >> s >> k;
        int count = 0;
        int last = s.length() - k + 1;
        for (int i = 0; i < last; i++) {
            if (s[i] == '-') {
                count++;
                flip(s, i, k);
            }
        }

        bool p = true;
        for (int i = last; i < s.length(); i++) {
            if (s[i] == '-') {
                p = false;
                break;
            }
        }

        if (p) {
            cout << "Case #" << cs << ": " << count << endl;
        } else {
            cout << "Case #" << cs << ": IMPOSSIBLE" << endl;
        }
    }
}


