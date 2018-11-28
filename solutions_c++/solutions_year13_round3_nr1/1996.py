// -*- compile-command: "g++ -o main -Wall -Wextra -g consonants.cpp" -*-
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <vector>
#include <utility>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <sstream>
#include <stack>
#define FOR(i,c) for(__typeof(c.begin()) i=c.begin();i!=c.end();++i)
using namespace std;

bool* convertToBinary( string str ) {
    char vowels[] = {'a', 'e', 'i', 'o', 'u' };
    size_t L = str.size();
    bool* result = new bool[L];
    for( size_t i = 0; i < L; i++ ) {
        bool isVowel = false;
        for( int j = 0; j < 5; j++ ) {
            if( str[i] == vowels[j] ) {
                result[i] = false;
                isVowel = true;
            }
        }
        if( !isVowel )
            result[i] = true;
    }

    return result;
}

int main() {
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++ ) {

        string input;
        int n;
        cin >> input >> n;

        int valid = 0;
        int notValid = 1;
        int result = 0;
        size_t L = input.size();

        int consonantLength = 0;

        bool* consonants = convertToBinary( input );

        vector<int> notValidFrom(L+n+10, 0);

        for(size_t i = 0; i<L; i++) {
            notValidFrom[i+n] = 1;
            notValid += notValidFrom[i];
            if( consonants[i] ) {
                consonantLength++;
                if( consonantLength >= n ) {
                    valid += notValid;
                    notValid = 0;
                }
                result += valid;

            } else {
                consonantLength = 0;
                result += valid;
            }
        }
        delete[] consonants;
        printf("Case #%d: %d\n", t, result);
    }
    return 0;
}
