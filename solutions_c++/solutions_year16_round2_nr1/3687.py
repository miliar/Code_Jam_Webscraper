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

string table[] = {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

size_t chomp(const string &s) {
    for(int i = 0; i < s.length(); ++i) {
        if(s[i] == '\n') {
            return i;
        }
    }
    return s.length();
}

bool rcsv(const string &s, const vector<bool> &mark, vector<size_t> &ret_stack) {

    size_t count = 0;
    for(size_t i = 0; i < mark.size(); ++i) {
        if(!mark[i]) {
            count++;
        }
    }
    if(count == s.length()) {
        return true;
    }

    for(size_t i = 0; i < 10; ++i) {

        vector<bool> tmp(mark);
        size_t count = 0;
        for(size_t j = 0; j < table[i].length(); ++j) {
            for(size_t pos = 0; pos < s.length(); ++pos) {
                if(table[i][j] == s[pos] && tmp[pos]) {
                    //printf("%c", s[pos]);
                    tmp[pos] = false;
                    count++;
                    break;
                }
            }
        }
        //printf(" ");
        if(count == table[i].length()) {
            ret_stack.push_back(i);
            if(rcsv(s, tmp, ret_stack)) {
                return true;
            }
            ret_stack.pop_back();
        }
    }
    return false;
}

void solve(size_t t, const string &s) {

    vector<bool> mark(s.length(), true);
    vector<size_t> ret_stack;

    rcsv(s, mark, ret_stack);

    printf("Case #%ld: ",t);
    for(size_t i = 0; i < 10; ++i) {
        for(size_t j = 0; j < ret_stack.size(); ++j) {
            if(ret_stack[j] == i) {
                printf("%ld", i);
            }
        }
    }
    printf("\n");
}

int main() {
    
    size_t T = 0;
    cin >> T;
    for(size_t t = 0; t < T; ++t) {
        string str;
        cin >> str;
        string str2(str, 0, chomp(str));
        solve(t+1, str2);
    }

    return 0;
}
