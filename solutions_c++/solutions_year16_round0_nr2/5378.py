#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

ll mancouter;
void flip(string &side, int upto) {
    mancouter++;

    int i = 0;
    upto--;
    while(i < upto) {            
        char first  = (side[upto]=='+')?'-':'+';
        char second =  (side[i]=='+')?'-':'+';
        side[i]    = first;
        side[upto] = second;

        upto--;
        i++;
    }
    if(i == upto) {
        side[i] = (side[i]=='+')?'-':'+';
    }
}

int allPancakesSame(string side) {
    int i = 1;
    while(side[i] == side[i-1]) {
        i++;
    }

    return i;
}

int main() {
    ll T, N, i, j, k;
    string side;

    cin >> T;
    ll t = 1;
    while(t <= T) {
        cin >> side;

        mancouter = 0;
        int cnt;
        while((cnt = allPancakesSame(side)) != side.length()) {
            // cout << cnt << endl;
            flip(side, cnt);
            // cout << side << endl;
        }

        if(side[i] == '-')
            mancouter++;
        cout << "Case #" << t << ": " << mancouter << endl;
        t++;
    }

    return 0;
}