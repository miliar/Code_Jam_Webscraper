#include <iostream>
#include <map>
#include <algorithm>
#include <string>
using namespace std;

int searchForZero(map<char, int>& charCounts){
    if(charCounts.count('Z') !=0) {
        int zCount = charCounts['Z'];
        charCounts['Z'] = 0;
        charCounts['E'] -=zCount;
        charCounts['R'] -=zCount;
        charCounts['O'] -=zCount;
        return zCount;
    }
    return 0;
}

int searchForOne(map<char, int>& charCounts){
    //this search is non deterministic, just trying
    if(charCounts.count('O')&&charCounts.count('N')&&charCounts.count('E')) {
        int oneCount = min(charCounts['O'],min(charCounts['N'],charCounts['E']));
        charCounts['O'] -=oneCount;
        charCounts['N'] -=oneCount;
        charCounts['E'] -=oneCount;
        return oneCount;
    }
    return 0;
}

int searchForTwo(map<char, int>& charCounts){
    if(charCounts.count('W') !=0) {
        int wCount = charCounts['W'];
        charCounts['W'] = 0;
        charCounts['T'] -=wCount;
        charCounts['O'] -=wCount;
        return wCount;
    }
    return 0;
}

int searchForThree(map<char, int>& charCounts){
    if(charCounts.count('T')&&charCounts.count('H')&&charCounts.count('R')&&charCounts.count('E')) {
        int threeCount = min(charCounts['T'],min(charCounts['H'],min(charCounts['R'],charCounts['E']/2)));
        charCounts['T'] -=threeCount;
        charCounts['H'] -=threeCount;
        charCounts['R'] -=threeCount;
        charCounts['E'] -=threeCount*2;
        return threeCount;
    }
    return 0;
}

int searchForFour(map<char, int>& charCounts){
    if(charCounts.count('U') !=0) {
        int uCount = charCounts['U'];
        charCounts['U'] = 0;
        charCounts['F'] -=uCount;
        charCounts['O'] -=uCount;
        charCounts['R'] -=uCount;
        return uCount;
    }
    return 0;
}

int searchForFive(map<char, int>& charCounts){
    if(charCounts.count('F')&&charCounts.count('I')&&charCounts.count('V')&&charCounts.count('E')) {
        int fiveCount = min(charCounts['F'],min(charCounts['I'],min(charCounts['V'],charCounts['E'])));
        charCounts['F'] -=fiveCount;
        charCounts['I'] -=fiveCount;
        charCounts['V'] -=fiveCount;
        charCounts['E'] -=fiveCount;
        return fiveCount;
    }
    return 0;
}

int searchForSix(map<char, int>& charCounts){
    if(charCounts.count('X') !=0) {
        int xCount = charCounts['X'];
        charCounts['X'] = 0;
        charCounts['S'] -=xCount;
        charCounts['I'] -=xCount;
        return xCount;
    }
    return 0;
}

int searchForSeven(map<char, int>& charCounts){
    if(charCounts.count('S')&&charCounts.count('E')&&charCounts.count('V')&&charCounts.count('N')) {
        int sevenCount = min(charCounts['S'],min(charCounts['V'],min(charCounts['E']/2,charCounts['N'])));
        charCounts['S'] -=sevenCount;
        charCounts['E'] -=sevenCount*2;
        charCounts['V'] -=sevenCount;
        charCounts['N'] -=sevenCount;
        return sevenCount;
    }
    return 0;
}

int searchForEight(map<char, int>& charCounts){
    if(charCounts.count('G') !=0) {
        int gCount = charCounts['G'];
        charCounts['G'] = 0;
        charCounts['E'] -=gCount;
        charCounts['I'] -=gCount;
        charCounts['T'] -=gCount;
        charCounts['H'] -=gCount;
        return gCount;
    }
    return 0;
}

int searchForNine(map<char, int>& charCounts){
    if(charCounts.count('N')&&charCounts.count('I')&&charCounts.count('E')) {
        int nineCount = min(charCounts['I'],min(charCounts['N']/2,charCounts['E']));
        charCounts['N'] -=nineCount*2;
        charCounts['I'] -=nineCount;
        charCounts['E'] -=nineCount;
        return nineCount;
    }
    return 0;
}

int main() {

    int caseCount, length;
    cin >> caseCount;

    string inputs[caseCount];
    for (int caseNumber = 0; caseNumber < caseCount; ++caseNumber) {
        cin >> inputs[caseNumber];
    }
    //cout << "case count is " << caseCount << endl;
    map<char,int> characterCounts;
    for (int caseNumber = 0; caseNumber < caseCount; ++caseNumber) {
        for (int position = 0; position < inputs[caseNumber].length(); ++position) {
            if(characterCounts.count(inputs[caseNumber].at(position)) != 0) {
                characterCounts[inputs[caseNumber].at(position)] += 1;
            } else {
                characterCounts[inputs[caseNumber].at(position)] = 1;
            }
        }

        //start searching for numbers
        int zero, one, two, three, four, five, six, seven, eight, nine;
        zero = searchForZero(characterCounts);
        two = searchForTwo(characterCounts);
        four = searchForFour(characterCounts);
        one = searchForOne(characterCounts);
        six = searchForSix(characterCounts);
        three = searchForThree(characterCounts);
        eight = searchForEight(characterCounts);
        five = searchForFive(characterCounts);
        seven = searchForSeven(characterCounts);
        nine = searchForNine(characterCounts);

        cout << "Case #" << caseNumber+1 << ": ";
        for (int i = 0; i <zero; ++i) {
            cout << "0";
        }
        for (int i = 0; i <one; ++i) {
            cout << "1";
        }
        for (int i = 0; i <two; ++i) {
            cout << "2";
        }
        for (int i = 0; i <three; ++i) {
            cout << "3";
        }
        for (int i = 0; i <four; ++i) {
            cout << "4";
        }
        for (int i = 0; i <five; ++i) {
            cout << "5";
        }
        for (int i = 0; i <six; ++i) {
            cout << "6";
        }
        for (int i = 0; i <seven; ++i) {
            cout << "7";
        }
        for (int i = 0; i <eight; ++i) {
            cout << "8";
        }
        for (int i = 0; i <nine; ++i) {
            cout << "9";
        }
        if(caseNumber+1 != caseCount)
            cout << endl;

    }
    return 0;
}

/*
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER

 */