//
//  main.cpp
//  StringLab
//
//  Created by Дмитрий Новик on 12.03.16.
//  Copyright © 2016 Дмитрий Новик. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

vector<int> digets(10, 0);

bool check() {
    for (int i = 0; i < 10; ++i) {
        if (digets[i] == 0)
            return true;
    }
    return false;
}

int main() {
    freopen("search1.out", "w", stdout);
    freopen("search1.in", "r", stdin);

    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        long long n;
        cin >> n;
        cout << "CASE #" << i + 1 << ": ";
        if (n == 0) {
            cout << "INSOMNIA\n";
            continue;
        }

        for (int j = 0; j < 10; ++j)
            digets[j] = 0;

        long long curr = 0;

        while (check()) {
            curr += n;
            long long tmp = curr;
            while (tmp > 0) {
                digets[tmp % 10] = 1;
                tmp /= 10;
            }
        }
        cout << curr << "\n";
    }


    return 0;
}
