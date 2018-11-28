#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <utility>
using namespace std;

typedef long long ll;

int arr1[5][5], arr2[5][5];
map<int, int> mp;

int main(void) {
    int t, n, m;
    freopen("input.in", "r", stdin);
    freopen("output.out", "w+", stdout);
    cin >> t;
    for (int test = 1; test <= t; test++) {
        mp.clear();
        cin >> n;
        n--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> arr1[i][j];
                if (i == n) mp[arr1[i][j]]++;
            }
        }
        cin >> m;
        m--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> arr2[i][j];
                if (i == m) mp[arr2[i][j]]++;
            }
        }

        int cnt = 0, val;
        for (map<int, int>::iterator it = mp.begin(); it != mp.end(); it++)
            if (it->second == 2)
                val = it->first, cnt++;

        if (cnt == 1)
            cout << "Case #" << test << ": " << val << "\n";
        else if (cnt > 1)
            cout << "Case #" << test << ": Bad magician!" << "\n";
        else
            cout << "Case #" << test << ": Volunteer cheated!" << "\n";
    }
    return 0;
}