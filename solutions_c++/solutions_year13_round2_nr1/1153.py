//
//  main.cpp
//  JAMROUNDB1
//
//  Created by Loick Michard on 04/05/13.
//  Copyright (c) 2013 Loick Michard. All rights reserved.
//

// cout << fixed << setprecision(0) << sum;

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <iomanip>


using namespace std;

int main() {
    freopen("/Users/loickmichard/Documents/Dev/JAM/JAMROUNDB1/JAMROUNDB1/input1.txt", "r", stdin);
    freopen("/Users/loickmichard/Documents/Dev/JAM/JAMROUNDB1/JAMROUNDB1/output1.txt", "w", stdout);

    int nb;
	cin >> nb;
    for (int i = 0; i < nb; i++) {
        long long int A, N;
        
        cin >> A >> N;
        std::vector<long long int> mobs;
        for (int k = 0; k < N; ++k) {
            long long int tmp;
            cin >> tmp;
            mobs.push_back(tmp);
        }
        sort(mobs.begin(), mobs.end());
        long long int total = 0;
        long long int maxi = -1;
        for (long long int k = 0; k < N && (maxi == -1 || total < maxi); ++k) {
            if (A > mobs[k]) {
                A += mobs[k];
            }
            else {
                if (maxi == -1 || N - k + total < maxi)
                    maxi = N - k + total;
                A += (A - 1);
                total += 1;
                k -= 1;
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (maxi != -1)
            cout << min(maxi, total);
        else
            cout << total;
        cout << endl;
    }
    return 0;
}

