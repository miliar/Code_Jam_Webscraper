#include <iostream>
#include <cstring>
#include <vector>
// #include <algorithm>
#include <cassert>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

// typedef unsigned long long INT;
typedef long long INT;
typedef vector<INT> IntVec;
typedef vector<int> VINT;

void convertToIntVec(string line, IntVec &res) {;
    char *list =  strdup(line.c_str());
    char* next = strtok(list, " ");
    while (next) {
        res.push_back(atol(next));
        next = strtok(NULL, " ");
    }
    free(list);
}

bool isPalindrome(INT num) {
    int n = num;
    int rev = 0;
    while (num > 0)
    {
        int dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
    }
    if (n == rev) {
        return true;
    }
    return false;
}



INT getDigitNum(INT n) {
    INT num = 0;
    while ( n != 0 ) {
        n /= 10;
        ++num;
    }
    return num;
}


INT findFairWithIdx(INT index) {
    INT count = 0;
    INT number = 9;
    INT w = 0;

    INT half; 
    INT h = 1;
    INT res; 

    while (true) {
        if((w > 0) && (w%2 == 0)) {
            number *= 10;
        }
        w++;
        if(count + number > index) 
            break;

        count += number;
    }

    index -= count;

    for (int i = 0; i < (w-1) / 2; i++) { 
        h *= 10;
    }

    half = h + index;
    res = half;
    if((w%2) != 0) {
        half /= 10;
    }

    while(half != 0) {
        res = res * 10 + half % 10;
        half /= 10;
    }

    return res;
}

INT pow10(INT x) {
    INT res = 1;
    for (INT i = 0; i < x; ++i) {
        res *= 10;
    }
    return res;
}

void fairNums(INT s, INT e, IntVec &res) { // find all fair Numbers between start and end;
    // cout<< "s,: " <<  s << endl;
    INT sdn = getDigitNum(s);
    // cout<< "sdn: " <<  sdn << endl;
    // INT edn = getDigitNum(e);;
    INT startIdx = 0; 
    for (INT i = 1; i < sdn; ++i) {
        INT num = 9 * pow10((i - 1)/2);
        // cout<< "num: " <<  num << endl;
        startIdx += num;
    }
    // cout<< "startIdx: " <<  startIdx << endl;
    INT fairNum = 0;
    for (int idx = startIdx; fairNum <= e; ++idx) {
        fairNum = findFairWithIdx(idx);
        if ((fairNum >= s) && (fairNum <=e)) {
            res.push_back(fairNum);
        }
    }
}


INT fairAndSquareNum(INT start, INT end) {
    INT num = 0;
    INT sqrt_s = (INT) sqrt(start);
    INT sqrt_e = (INT) (sqrt(end) + 1);
    IntVec candiates;
    fairNums(sqrt_s, sqrt_e, candiates);
    for (int i = 0; i < candiates.size(); ++i) {
        INT c = candiates[i];
        INT square = (INT) c * c;
        if (isPalindrome(square) && (start <= square) && (square <= end)) {
            ++num;
        }
    }
    return num;
};

int main(int argc, char *argv[]) {
    // istream &in = cin;
    // ostream &out = cout;
    // in = &cin;
    // out = &cout;
    // ifstream inFile("tiny.in");
    ifstream inFile("C-small-attempt0.in");
    // ofstream outFile("result_large.txt");
    ofstream outFile("C-small-attempt0.out");
    istream &in = inFile;
    ostream &out = outFile;
    // ostream &out = cout;

    // INT res = find(10);
    // cout<< "res: " <<  res << endl;

    // cout << (isPalindrome(122) ? "YES" : "NO") << endl;;

    string line;
    getline(in, line);
    int T = atoi(line.c_str());
    // cout << "T: " <<  T << endl;
    for (int i = 0; i < T; ++i) {
        getline(in, line);
        IntVec interval;
        convertToIntVec(line, interval);
        // out << interval[0] << " " << interval[1] << endl;
        IntVec res;
        INT num = fairAndSquareNum(interval[0], interval[1]);
        // INT num = fairAndSquareNum(0, 1e14);
        out << "Case #" << i+1 << ": " << num << endl;

        // fairNums(interval[0], interval[1], res);
        // for (int j = 0; j < res.size(); ++j) {
        //     out << res[j] << " ";
        // }
        // cout << endl;
        // out << interval[0] << " " << interval[1] << endl;
        // int vSize = atoi(line.c_str());
        // IntVec list1;
        // getline(in, line);
        // convertToIntVec(line, list1);

        // IntVec list2;
        // getline(in, line);
        // convertToIntVec(line, list2);
        // INT sum = minScalar(list1, list2);
        // out << "Case #" << i+1 << ": " << sum << endl;
    }
    return 0;
}
