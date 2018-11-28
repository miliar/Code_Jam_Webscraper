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

string solve(const string &S) {
    deque<char> tmp;
    char c = S[0];
    tmp.push_back(c);
    for(size_t i = 1; i < S.length(); ++i) {
        if(tmp[0] <= S[i]) {
            tmp.push_front(S[i]);
        } else {
            tmp.push_back(S[i]);
        }
    }
    string ret;
    for(size_t i = 0; i < tmp.size(); ++i) {
        ret.push_back(tmp[i]);
    }
    return ret;
}

int main() {
    
    size_t T;
    cin >> T;
    for(size_t t = 0; t < T; ++t) {
        string S;
        cin >> S;
        //printf("%s\n", S.c_str());
        string ret = solve(S);
        printf("Case #%lu: %s\n", t+1, ret.c_str());
    }

    return 0;
}
