#include <iostream>
#include <cmath>
#include <vector>
#include <stdlib.h>
#include <cstdio>
#include <ctime>
#include <map>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("panc_large.txt", "w", stdout);

    int T;
    cin >> T;

    for (int test = 1; test <= T; test++) {
        string pc;
        cin >> pc;
        int n = pc.length();

        int ptr = n-1;
        while (ptr >= 0 && pc[ptr] == '+') ptr--;

        int ans = 0;
        char sg = '-';
        while (ptr >= 0) {
            ans++;
            while (ptr >= 0 && pc[ptr] == sg) ptr--;
            if (sg == '+') sg = '-';
            else sg = '+';
        }
        printf("Case #%d: %d\n", test, ans);
    }

    return 0;
}

