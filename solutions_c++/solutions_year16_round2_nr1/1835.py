#include <iostream>
using namespace std;

string names[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int char2num(char c) {
    return c - 'A';
}

string solve(const string& s)
{
    int numberParts[10];
    
    string number;
    
    int counts[26];
    for (int i=0; i<26; ++i) {
        counts[i] = 0;
    }

    for (int i=0; i<10; ++i) {
        numberParts[i] = 0;
    }
    
    for (int i=0; i<s.size(); ++i) {
        counts[char2num(s[i])]++;
    }
    
    numberParts[0] = counts[char2num('Z')];
    counts[char2num('Z')] -= numberParts[0];
    counts[char2num('E')] -= numberParts[0];
    counts[char2num('R')] -= numberParts[0];
    counts[char2num('O')] -= numberParts[0];

    numberParts[2] = counts[char2num('W')];
    counts[char2num('T')] -= numberParts[2];
    counts[char2num('W')] -= numberParts[2];
    counts[char2num('O')] -= numberParts[2];

    numberParts[4] = counts[char2num('U')];
    counts[char2num('F')] -= numberParts[4];
    counts[char2num('O')] -= numberParts[4];
    counts[char2num('U')] -= numberParts[4];
    counts[char2num('R')] -= numberParts[4];
    
    numberParts[6] = counts[char2num('X')];
    counts[char2num('S')] -= numberParts[6];
    counts[char2num('I')] -= numberParts[6];
    counts[char2num('X')] -= numberParts[6];

    numberParts[8] = counts[char2num('G')];
    counts[char2num('E')] -= numberParts[8];
    counts[char2num('I')] -= numberParts[8];
    counts[char2num('G')] -= numberParts[8];
    counts[char2num('H')] -= numberParts[8];
    counts[char2num('T')] -= numberParts[8];

    numberParts[5] = counts[char2num('F')];
    counts[char2num('F')] -= numberParts[5];
    counts[char2num('I')] -= numberParts[5];
    counts[char2num('V')] -= numberParts[5];
    counts[char2num('E')] -= numberParts[5];
    
    numberParts[1] = counts[char2num('O')];
    numberParts[3] = counts[char2num('H')];
    numberParts[7] = counts[char2num('S')];
    numberParts[9] = counts[char2num('I')];
    
    for (int i=0; i<10; ++i) {
        for (int j=0; j<numberParts[i]; ++j) {
            number.push_back(char(i+'0'));
        }
    }
    
    return number;
}

int main()
{
    int nCases;
    cin >> nCases;
    cin.ignore (1, '\n');
    for (int i=0; i<nCases; ++i) {
        string input;
        getline(cin, input);
        string result = solve(input);
        cout << "Case #" << i+1 << ": " << result << endl;
    }
    return 0;
}
