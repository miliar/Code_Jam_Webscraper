#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <string>

using namespace std;

unsigned int letter[26];
unsigned int number[10];

void count(string S){
    for (unsigned int i = 0; i < 26; i++) {
        letter[i] = 0;
    }
    for (unsigned int i = 0; i < 10; i++) {
        number[i] = 0;
    }

    for (unsigned int i = 0; i < S.length(); i++) {
        letter[S[i]-'A']++;
    }

    //ZERO
    number[0] = letter['Z'-'A'];
    letter['Z'-'A'] -= number[0];
    letter['E'-'A'] -= number[0];
    letter['R'-'A'] -= number[0];
    letter['O'-'A'] -= number[0];

    //TWO
    number[2] = letter['W'-'A'];
    letter['T'-'A'] -= number[2];
    letter['W'-'A'] -= number[2];
    letter['O'-'A'] -= number[2];

    //SIX
    number[6] = letter['X'-'A'];
    letter['S'-'A'] -= number[6];
    letter['I'-'A'] -= number[6];
    letter['X'-'A'] -= number[6];

    //EIGHT
    number[8] = letter['G'-'A'];
    letter['E'-'A'] -= number[8];
    letter['I'-'A'] -= number[8];
    letter['G'-'A'] -= number[8];
    letter['H'-'A'] -= number[8];
    letter['T'-'A'] -= number[8];

    //THREE
    number[3] = letter['H'-'A'];
    letter['T'-'A'] -= number[3];
    letter['H'-'A'] -= number[3];
    letter['R'-'A'] -= number[3];
    letter['E'-'A'] -= number[3];
    letter['E'-'A'] -= number[3];

    //FOUR
    number[4] = letter['R'-'A'];
    letter['F'-'A'] -= number[4];
    letter['O'-'A'] -= number[4];
    letter['U'-'A'] -= number[4];
    letter['R'-'A'] -= number[4];

    //ONE
    number[1] = letter['O'-'A'];
    letter['O'-'A'] -= number[1];
    letter['N'-'A'] -= number[1];
    letter['E'-'A'] -= number[1];

    //FIVE
    number[5] = letter['F'-'A'];
    letter['F'-'A'] -= number[5];
    letter['I'-'A'] -= number[5];
    letter['V'-'A'] -= number[5];
    letter['E'-'A'] -= number[5];

    //SEVEN
    number[7] = letter['V'-'A'];
    letter['S'-'A'] -= number[7];
    letter['E'-'A'] -= number[7];
    letter['V'-'A'] -= number[7];
    letter['E'-'A'] -= number[7];
    letter['N'-'A'] -= number[7];

    //NINE
    number[9] = letter['E'-'A'];
    //letter['O'-'A'] -= number[9];



    return;
}


int main()
{
    ifstream in ("A-large.in");
    ofstream out ("output.out");
    string S;
    unsigned long long int T;
    //unsigned long long int time, n, timeUp, timeDown;

    if(in.is_open()){
        in >> T;
        for (unsigned int i = 1; i <= T; i++){
            in >> S;
            count(S);
            out << "Case #" << i << ": ";

            for (unsigned int i = 0; i < 10; i++) {
                for (unsigned int j = 0; j < number[i]; j++) {
                    out << i;
                }
            }

            out << endl;
        }
        in.close();
    }
    out.close();
    return 0;
}
