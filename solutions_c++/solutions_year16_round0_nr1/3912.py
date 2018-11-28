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


void solve(uint32_t t, uint32_t N) {
    uint32_t flag_count = 0;
    vector<bool> flags(10, false);
    uint64_t current, prev;
    int32_t i = 0;
    while(true) {
        i++;
        current = N * i;
        if(prev == current) {
            break;
        }
        prev = current;
        uint64_t m = current;
        while(m > 0) {
            uint64_t x = m % 10;
            if(!flags[x]) {
                flags[x] = true;
                flag_count++;
                //printf("%llu\n", x);
            }
            if(flag_count == 10) {
                break;
            }
            m /= 10;
        }
        if(flag_count == 10) {
            break;
        }
    }
    if(flag_count != 10) {
        printf("Case #%d: INSOMNIA\n", t);
    } else {
        printf("Case #%d: %llu\n", t, current);
    }
}


int main() {
    
    uint32_t T, N;

    cin >> T;

    for(int t = 0; t < T; ++t) {
        cin >> N;
        
        solve(t+1, N);
    }

    return 0;
}

