#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;


int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, sMax;
    string aud;
    cin >> t;
    for(int c = 1; c <= t; c++){
        cin >> sMax >> aud;
        int res = 0;
        int cnt = 0;
        for(int i = 0; i <= sMax; i++){
            int audI = aud[i] - '0';
            if(cnt < i){
                res += (i - cnt);
                cnt += (i - cnt);
            }
            cnt += audI;
        }

        cout << "Case #" << c << ": " << res << endl;
    }
    return 0;
}