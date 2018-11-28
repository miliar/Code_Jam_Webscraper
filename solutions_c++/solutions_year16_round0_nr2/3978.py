//
// Created by adinata on 09/04/16.
//

// FLIPPING THE STACK
// Given ---++-, how to make it ++++++ by only flipping stack with minimum number?
// 1, Greedy, Flip All `-` from top, then with all `+` and neighboring continuous `-` flip it again and flip (2 step)
// Does it optimal?
// 2, Bruteforce, 2^100 space maximum, using BFS, check for every stack flip. Stop when you found.
// 3 Heuristic, using greedy, get the pattern, maybe count every neighboring +-.
// I think greedy is optimal, not suboptimal.
// We can check it by creating brute force and then check it with greedy whether it's worked or not.
// 

#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;


int solveLength1(char* s) {
    return (s[0] == '+') ? 0 : 1;
}

char doFlip(char s) {
    return s == '+' ? '-' : '+';
}

int solveOther(int len, char* s) {
    bool accepted = false;
    int flip = 0;
    while (!accepted) {
        int head = 0;
        int tail = 1;
        while (tail < len && s[head] == s[tail]) {
            tail++;
        }
        if (tail == len) {
            accepted = true;
            break;
        } else {
            flip += 1;
            for (int i = head; i < tail; i++) {
                s[i] = doFlip(s[i]);
            }
        }

    }

    if (s[0] == '+') {
        return flip;
    } else {
        return flip + 1;
    }
}

void solve(int tc) {
    int ans;
    char s[100];
    scanf("%s\n", s);
    int len = strlen(s);
    if (len == 1) {
        ans = solveLength1(s);
    } else {
        ans = solveOther(len, s);
    }
    printf("Case #%d: %d\n", tc, ans);
}

int main() {
    int TC;
    scanf("%d", &TC);
    for (int i=1; i<=TC; i++) {
        solve(i);
    }
}