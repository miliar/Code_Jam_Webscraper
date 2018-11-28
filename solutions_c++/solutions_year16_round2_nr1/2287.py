#include <iostream>
#include <cstring>
using namespace std;

string numbers[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool digitCheck (bool (* boolmap)[10], int num) {
    while (num != 0) {
        int digit = num % 10;
        (*boolmap)[digit] = true;
        num = num / 10;
    }

    bool res = true;
    for (int i = 0; i < 10; i++) {
        res = res && (*boolmap)[i];
    }
    return res;
}

int main () {
    int T;
    string blank;
    cin >> T;
    getline(cin, blank);
    for (int t = 1; t <= T; t++) {
        int digitCount[10] = {0};
        int letterCount[26] = {0};
        string str;
        getline(cin, str);

        for (int i = 0; i < str.length(); i++) {
            letterCount[str[i]-'A']++;
        }

        for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;

        int Zcount = letterCount['Z'-'A'];
        digitCount[0] = Zcount;
        for (int i = 0; i < numbers[0].length(); i++) {
            letterCount[numbers[0].at(i)-'A'] -= Zcount;
        }

                for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;

        int Xcount = letterCount['X'-'A'];
        digitCount[6] = Xcount;
        for (int i = 0; i < numbers[6].length(); i++) {
            letterCount[numbers[6].at(i)-'A'] -= Xcount;
        }

                for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;

        int Scount = letterCount['S'-'A'];
        digitCount[7] = Scount;
        for (int i = 0; i < numbers[7].length(); i++) {
            letterCount[numbers[7].at(i)-'A'] -= Scount;
        }

                for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;

        int Vcount = letterCount['V'-'A'];
        digitCount[5] = Vcount;
        for (int i = 0; i < numbers[5].length(); i++) {
            letterCount[numbers[5].at(i)-'A'] -= Vcount;
        }

                for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;

        int Fcount = letterCount['F'-'A'];
        digitCount[4] = Fcount;
        for (int i = 0; i < numbers[4].length(); i++) {
            letterCount[numbers[4].at(i)-'A'] -= Fcount;
        }

        for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;
        int Rcount = letterCount['R'-'A'];
        digitCount[3] = Rcount;
        for (int i = 0; i < numbers[3].length(); i++) {
            letterCount[numbers[3].at(i)-'A'] -= Rcount;
        }

        for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;
        int Wcount = letterCount['W'-'A'];
        digitCount[2] = Wcount;
        for (int i = 0; i < numbers[2].length(); i++) {
            letterCount[numbers[2].at(i)-'A'] -= Wcount;
        }

        for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;
        int Gcount = letterCount['G'-'A'];
        digitCount[8] = Gcount;
        for (int i = 0; i < numbers[8].length(); i++) {
            letterCount[numbers[8].at(i)-'A'] -= Gcount;
        }

                for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;

        int Ocount = letterCount['O'-'A'];
        digitCount[1] = Ocount;
        for (int i = 0; i < numbers[1].length(); i++) {
            letterCount[numbers[1].at(i)-'A'] -= Ocount;
        }

        for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;

        int Ecount = letterCount['E'-'A'];
        digitCount[9] = Ecount;
        for (int i = 0; i < numbers[9].length(); i++) {
            letterCount[numbers[9].at(i)-'A'] -= Ecount;
        }

                for (int i = 0; i < 26; i++) {
            cerr<<letterCount[i]<<" ";
        }
        cerr<<endl;

        cout << "Case #" << t << ": ";
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < digitCount[i]; j++) {
                cout<<i;
            }
        }
        cout<<endl;

    }
    return 0;
}
