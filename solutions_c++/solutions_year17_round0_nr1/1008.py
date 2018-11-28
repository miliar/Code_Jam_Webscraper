#define __LOCAL__
//#define __CUSTOM_INPUT__
//#define __DEBUG__
//#define __VERBOSE__
//#define __NO_OUTPUT__

#ifdef __DEBUG__
#define debugStream cout
#else
#define debugStream if(false) cout
#endif

#ifdef __VERBOSE__
#define verboseStream cout
#else
#define verboseStream if(false) cout
#endif

#ifdef __NO_OUTPUT__
#define outputStream if(false) cout
#else
#define outputStream cout
#endif

#ifndef __LOCAL__
#define inputStream cin
#endif

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <list>
#include <limits>
#include <algorithm>
#include <utility>
#include <array>
#include <unordered_map>
#include <map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef long long ull;

int t;
vector<string> s;
vector<int> k;

void solve(int caseNumber, string s, int k) {
    outputStream << "Case #" << caseNumber << ": ";
    int flips = 0;
    for(int i=0; i<=s.size()-k; i++) {
        if(s[i] == '-') {
            flips++;
            for(int j=0; j<k; j++) {
                if(s[i+j] == '-') {
                    s[i+j] = '+';
                } else {
                    s[i+j] = '-';
                }
            }
        }
    }
    bool failed = false;
    for(int i=s.size()-k; i<s.size(); i++) {
        if(s[i] == '-') {
            failed = true;
            break;
        }
    }
    if(failed) {
        outputStream << "IMPOSSIBLE";
    } else {
        outputStream << flips;
    }
    outputStream << endl;
}

int main(int argc, char** argv) {

#ifdef __LOCAL__
    string inputFilename = "input.txt";
    if(argc > 1) {
        inputFilename = argv[1];
    }
    ifstream inputStream = ifstream(inputFilename);
#endif

#ifdef __CUSTOM_INPUT__
    t = 100;
    s.resize(t);
    k.resize(t);
    s[0] = "+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--+--++-++--";
    for(int i=0; i<t; i++) {
        s[i] = s[0];
        k[i] = 500 + i;
    }
#else
    inputStream >> t;
    s.resize(t);
    k.resize(t);
    for(int i=0; i<t; i++) {
        inputStream >> s[i] >> k[i];
    }
#endif

    for(int i=0; i<t; i++) {
        solve(i+1, s[i], k[i]);
    }

}