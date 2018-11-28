#include <iostream>
#include <cmath>
#include <vector>
#include <climits>
#include <string>
#include <stack>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define x first
#define y second

using namespace std;

int main()
{
    freopen ("in", "r", stdin);
    freopen ("out", "w", stdout);
    int T;
    cin >> T;

    for(int test = 1; test <= T; test++) {

        int maxshy;
        cin >> maxshy;

        int invited = 0;
        int stands = 0;

        for (int i = 0; i <= maxshy; i++) {
            char buf;
            int a;
            cin >> buf;
            a = buf - '0';

            if (stands < i) {
                invited += i - stands;
                stands = i;
            }

            stands += a;
        }

        cout << "Case #" << test << ": " << invited << endl;
    }

    return 0;
}

