#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <complex>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cfloat>
#include <ctime>

using namespace std;

typedef pair<int,int> point;

typedef signed char int8_t;
typedef unsigned char uint8_t;
typedef signed short int16_t;
typedef unsigned short uint16_t;
typedef signed int int32_t;
typedef unsigned int uint32_t;

void flip(size_t pos, string &S) {
    vector<char> temp;

    for(size_t i = 0; i <= pos; ++i) {
        char c = S[i];
        if(c == '+') {//flip
            temp.push_back('-');
        } else {
            temp.push_back('+');
        }
    }
    for(size_t i = 0; i <= pos; ++i) {
        char c = temp.back();
        S[i] = c;
        temp.pop_back();
    }
}

void solve(uint32_t t, string &S) {

    size_t count = 0;
    while(true) {
        size_t check = S.find_first_of('-');
        if(check == string::npos) {
            break;
        }
        if(S[0] == '+') {
            size_t pos_minus = S.find_last_of('-');
            size_t pos_plus = S.find_last_of('+', pos_minus);
            flip(pos_plus, S);
        } else {
            size_t pos_minus = S.find_last_of('-');
            flip(pos_minus, S);
        }
        //printf("%s\n", S.c_str());
        count++;
    }

    printf("Case #%d: %lu\n", t, count);
}


int main() {
    uint32_t T;

    cin >> T;
    for(uint32_t t = 0; t < T; ++t) {
        string S;
        cin >> S;
        solve(t+1, S);
    }

    return 0;
}
