#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int getAllTheSame(char * s, int size, char sign) {
    if (size == 1) {
        return s[0] == sign ? 0 : 1;
    }
    int flip = 0;
    flip += getAllTheSame(s, size - 1, s[size-1]);
    if (s[size-1] != sign) {
        return flip + 1;
    }
    return flip;
}

int main()
{
    //ifstream fin("input.in");
    //ifstream fin("B-small-attempt2.in");
    ifstream fin("B-large.in");
    ofstream fout("output.out");

    if (!fin.is_open()) cout << "input.in open fail" << endl;
    if (!fout.is_open()) cout << "output.out open fail" << endl;

    int numCase;
    fin >> numCase;

    int c;
    long flip;
    string str;
    for (c = 0; c < numCase; c++)
    {
        fin >> str;
        char s[str.length() + 1];
        str.copy(s, str.length(), 0);
        s[str.length()] = '\0';

        cout << str << endl;
        // str= "--+-";
        if (str.length() == 1) {
            cout << "Case #" << (c + 1) << ": " << (s[0] == '-' ? 1 : 0) << endl;
            fout << "Case #" << (c + 1) << ": " << (s[0] == '-' ? 1 : 0) << endl;
            continue;
        }

        long flip = getAllTheSame(s,str.length() -1, s[str.length()-1] );
        if (s[str.length()-1] == '-') {
            flip++;
        }


        cout << "Case #" << (c + 1) << ": " << flip << endl;
        fout << "Case #" << (c + 1) << ": " << flip << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
