#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>


using namespace std;

int standingOvation(int smax, string s) {
    int i, total, result = 0;
    total = s[0] - '0';
    for (i = 1; i <= smax; ++i) {
        if (i > total) {
            result += i - total;
            total += i - total;
        }
        total += s[i] - '0';
    }
    return result;
}

int main()
{
    int i = 0, t, smax;
    string s;
    scanf("%d", &t);
    while (i < t) {
        cin >> smax >> s;
        printf("Case #%d: %d\n", ++i, standingOvation(smax, s));
    }
}
