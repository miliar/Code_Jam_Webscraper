#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <math.h>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long
#define ld long double
#define chr unsigned char
#define uint unsigned int

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    int t;
    cin >> t;
    for (int q = 1; q <= t; ++q){
        string s;
        cin >> s;

        int n = s.length();

        int b = 1;
        for (int i = 1; i < n; ++i)
            b += (s[i] != s[i - 1]);

        cout << "Case #" << q << ": " << b - (s[n - 1] == '+') << endl;
    }


    fclose(stdout);
    return 0;
}
