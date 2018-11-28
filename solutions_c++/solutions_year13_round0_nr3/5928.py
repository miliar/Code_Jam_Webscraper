#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <algorithm>

#define maxn 1000

using namespace std;

int arr[maxn + 10];

void pregen()
{
    int sq = sqrt(maxn), count = 0, temp = 0;
    string s1, s2;

    for(int i = 1; i * i <= maxn; i++){
        stringstream ss;
        ss << i;
        s1 = ss.str();
        s2 = s1;
        reverse(s2.begin(), s2.end());

        if(s1 != s2) continue;

        stringstream ss1;
        int ii = i * i;
        ss1 << ii;
        s1 = ss1.str();
        s2 = s1;
        reverse(s2.begin(), s2.end());

        if(s1 == s2){arr[ii] = (++count);}
    }

    for(int i = 1; i <= maxn; i++){
        temp = max(temp, arr[i]);
        arr[i] = temp;
    }
}

int main()
{
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.out", "w", stdout);
    pregen();
    int t, a, b;

    cin >> t;

    for(int i = 1; i <= t; i++){
        cin >> a >> b;
        cout << "Case #" << i << ": " << arr[b] - arr[a - 1] << endl;
    }

    return 0;
}
