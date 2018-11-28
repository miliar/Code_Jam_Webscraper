//
//  main.cpp
//
//  Google Code Jam 2k16 - Round 1B - Problem A
//
//  I regret everything seen here, but maybe I'll (re)learn some things.

#include <iostream>
#include <vector>
#include <string>
// #include <cmath>

using namespace std;
// hell of global variables goes here!

static const string digits[10] = {
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"
};

void countup(string s, int *lc) {
    for (int q=0; q<26; q++) {
        lc[q] = 0;
    }
    for (int q=0; q<s.size(); q++) {
        lc[s[q] - 'A']++;
    }
    
    return;
}

int countdown(int *lc, int digit, char c) {
    int dc = lc[c - 'A'];
    
    for (int q=0; q<digits[digit].size(); q++) {
        int i = digits[digit][q] - 'A';
        lc[i] = lc[i] - dc;
        if (lc[i] < 0) {cout << "crap"; exit(EXIT_FAILURE);}
    }
    
    return dc;
}

int maxcount(int *lc, int digit) {
    int mdc = 2000;
    int testcount[26];
    string testme = digits[digit];
    
    for (int p=0; p<26; p++) testcount[p] = 0;
    
    for (int q=0; q<testme.size(); q++) {
        int i = testme[q] - 'A';
        testcount[i]++;
    }
    
    for (int q=0; q<testme.size(); q++) {
        int i = testme[q] - 'A';
        
        int max = lc[i] / testcount[i];
        
        if (max < mdc) mdc = max;
    }
    
    for (int q=0; q<testme.size(); q++) {
        int i = testme[q] - 'A';
        
        lc[i] = lc[i] - mdc;
        
    }
    
    return mdc;
}

int main(int argc, const char * argv[]) {
    int cases, current;
    
    int found;
    string lettersin;
    
    int lcin[26];
    int digitcounts[10];
    
    cin >> cases;
    for (current=1; current<=cases; ++current) {
        cout << "Case #" << current << ": ";
        
        cin >> lettersin;
        
        countup(lettersin, lcin);
        found = 0;
        
        for (int q=0; q<10; q++) digitcounts[q] = 0;
        
        digitcounts[0] = countdown(lcin, 0, 'Z');
        digitcounts[2] = countdown(lcin, 2, 'W');
        digitcounts[4] = countdown(lcin, 4, 'U');
        digitcounts[6] = countdown(lcin, 6, 'X');
        digitcounts[8] = countdown(lcin, 8, 'G');
        
        // hell of special cases ended up moot?  oh well
        digitcounts[7] = maxcount(lcin, 7);
        digitcounts[5] = maxcount(lcin, 5);
        digitcounts[3] = maxcount(lcin, 3);
        digitcounts[9] = maxcount(lcin, 9);
        digitcounts[1] = maxcount(lcin, 1);
        
        for (int q=0; q<10; q++) {
            for (int t=0; t<digitcounts[q]; t++) cout << q;
        }
        
        cout << endl;
    }
}











