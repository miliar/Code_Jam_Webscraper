// B: Revenge of the Pancakes

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <queue>
#include <set>

using namespace std;

#define uint128_t unsigned __int128

unsigned int s_length;

uint128_t flopFirstNBits(uint128_t number, unsigned int N) {
    for (unsigned int i = 0; 2 * i < N; i++) {
        unsigned int j = N - i - 1;
        if (j == i) {
            number ^= ((uint128_t)1) << i;
        } else {
            number ^= (((number >> i) ^ 1) & 1) << j;
            number ^= ((number >> j) & 1) << i;
            number ^= (((number >> i) ^ 1) & 1) << j;
        }
    }
    return number;
}

unsigned long long minFlips(uint128_t original_pancakes) {
    queue< pair<unsigned long long, uint128_t> > queue;
    set<uint128_t> visited;
    queue.push(make_pair((unsigned long long)0, original_pancakes));

    while (!queue.empty()) {
        pair<unsigned long long, uint128_t> current = queue.front();
        queue.pop();

        if (0 == current.second) {
            return current.first;
        }

        for (unsigned int i = 1; i <= s_length; i++) {
            uint128_t pancakes = flopFirstNBits(current.second, i);
            if (0 == pancakes) {
                return current.first + 1;
            }
            if (visited.insert(pancakes).second) {
                queue.push(make_pair(current.first + 1, pancakes));
            }
        }
    }

    return -1;  // we should never get here; this casts into ULONGLONG_MAX
}

int main(int argc, char *argv[]) {
    unsigned int T;
    scanf("%d", &T);

    for (unsigned int cases = 0; cases < T; cases++) {
        char S[101];
        scanf("%s", S);
        s_length = strlen(S);
        uint128_t pancakes = 0;
        for (unsigned int i = 0; i < s_length; i++) {
            pancakes |= (uint128_t)(S[i] == '-') << i;
        }
        unsigned long long flips = minFlips(pancakes);

        printf("Case #%u: %llu\n", cases + 1, flips);
    }
}
