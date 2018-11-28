#include <iostream>
#include <algorithm>
#include <cstdio>
#include <math.h>

using namespace std;

int main()
{
    freopen("codej.out", "w", stdout);
    int T;
    cin >> T;
    for(int c = 1; c <= T; c++)
    {
        int n, q = 1;
        string S;
        cin >> n >> S;
        int viewers = 0, friends = 0;
        for(int i = 0; i < S.length(); i++)
        {
            int d;
            d = S[i] - '0';
            if(q == 1 && d != 0)
                if(i > viewers + friends)
                    friends += i - (viewers+friends);
            viewers += d;
            if(d == 0)  q = 1;
            else q = 0;
            if(viewers + friends > 10) break;
        }
        printf("Case #%d: %d\n", c,     friends);
    }
    return 0;
}
//this code was written when suPer hIgh :)==~~  6 5000031
