#include <iostream>
#include <string>
#include <fstream>
#include <set>
#include <cmath>
#include <map>
#include <vector>

using namespace std;


//"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
// Z -> ZERO
// W -> TWO
// U -> FOUR
// X -> SIX
// G -> EIGHT

// ONE, THREE, FIVE, SEVEN, NINE
// F -> FIVE
// O -> ONE
// S -> SEVEN
// T -> THREE
// N -> NINE

void GetDigits(map<char, int>& char_counts, map<int, int>& digit_counts) {
    // ZERO
    digit_counts[0] = char_counts['Z'];
    char_counts['Z'] = 0;
        char_counts['E'] -= digit_counts[0];
            char_counts['R'] -= digit_counts[0];
                char_counts['O'] -= digit_counts[0];

    // TWO
    digit_counts[2] = char_counts['W'];
    char_counts['W'] = 0;
        char_counts['T'] -= digit_counts[2];
            char_counts['O'] -= digit_counts[2];

    // FOUR
    digit_counts[4] = char_counts['U'];
    char_counts['U'] = 0;
        char_counts['O'] -= digit_counts[4];

        char_counts['F'] -= digit_counts[4];
            char_counts['R'] -= digit_counts[4];


    // SIX
    digit_counts[6] = char_counts['X'];
    char_counts['X'] = 0;
        char_counts['S'] -= digit_counts[6];
            char_counts['I'] -= digit_counts[6];

    // EIGHT
    digit_counts[8] = char_counts['G'];
    char_counts['G'] = 0;
        char_counts['E'] -= digit_counts[8];
            char_counts['I'] -= digit_counts[8];
                    char_counts['H'] -= digit_counts[8];
            char_counts['T'] -= digit_counts[8];


    //FIVE
    digit_counts[5] = char_counts['F'];
    char_counts['F'] = 0;
        char_counts['I'] -= digit_counts[5];
            char_counts['V'] -= digit_counts[5];
                    char_counts['E'] -= digit_counts[5];

    //ONE
    digit_counts[1] = char_counts['O'];
    char_counts['O'] = 0;
        char_counts['N'] -= digit_counts[1];
            char_counts['E'] -= digit_counts[1];

    // SEVEN
    digit_counts[7] = char_counts['S'];
    char_counts['S'] = 0;
        char_counts['E'] -= digit_counts[7];
            char_counts['V'] -= digit_counts[7];
                    char_counts['E'] -= digit_counts[7];
                     char_counts['N'] -= digit_counts[7];

    // THREE
    digit_counts[3] = char_counts['T'];
    char_counts['T'] = 0;
        char_counts['H'] -= digit_counts[3];
            char_counts['R'] -= digit_counts[3];
                    char_counts['E'] -= digit_counts[3];
            char_counts['E'] -= digit_counts[3];

    //NINE
    digit_counts[9] = char_counts['N'] / 2;
    char_counts['N'] = 0;
        char_counts['I'] -= digit_counts[9];
                    char_counts['E'] -= digit_counts[9];
}

int counter_cc = 0;
string GetPhone(const string& s) {
    counter_cc++;
    map<char, int> char_counts;
    for (char c : s) {
        char_counts[c]++;
    }
    map<int, int> digit_counts;
    string out;
    GetDigits(char_counts, digit_counts);
    for (auto dc : digit_counts) {
        for (int i = 0; i < dc.second; ++i) {
            out.push_back(dc.first + '0');
        }
    }
    for (auto c : char_counts) {
        if (c.second != 0) {
            cerr << c.first << "\t" << c.second << "\t"<< counter_cc<<endl;
        }
    }
    return out;
}

int main(int argc, char* argv[]) {
    /*cout << CheckFirstDigit(10, 32, 7)<<endl;
    return 0;*/
    if (argc != 2) {
        cerr << "Give file name\n";
        return -1;
    }
    string fn = argv[1];
    ifstream input;
    input.open(fn.c_str());
    fn = fn.append(".out.txt");
    ofstream output;
    output.open(fn);

    int T;
    input >> T;
    string S;

    for (int t = 1; t<= T; ++t) {
        output << "Case #" << t << ": ";
        input >> S;
        output <<  GetPhone(S) << endl;
    }


    output.close();
    input.close();
    return 0;
}