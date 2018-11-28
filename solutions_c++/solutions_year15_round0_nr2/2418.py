//
// Created by Morteza on 2015-04-11.
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int calc(int i, int j) {

//    if (i <= j )
//        return 0;
//    else if( i == 1 && j == 0)
//        return 1;
//    else if (i > j) {
//        return calc(i / 2, j) + calc(ceil(i / 2.0), j) + 1;
//    }
//    return 0;
//    cout << floor((i-1)/j) << endl;
    return floor((i-1)/j);
}


int main(int argc, const char *argv[]) {

    ios_base::sync_with_stdio(false);

    int num_cases, num_diners, max_k;

    cin >> num_cases;

    for (int i = 0; i < num_cases; ++i) {
        cin >> num_diners;
        vector<int> diners;
        for (int j = 0; j < num_diners; ++j) {
            int pancakes = 0;
            cin >> pancakes;
            diners.push_back(pancakes);
        }
        max_k = *max_element(diners.begin(), diners.end());

        int min_minutes = 1000;

        for (int k = 1; k <= max_k; ++k) {
            int total_temp = k;
            for (int j = 0; j < num_diners; ++j) {
//                cout << "diner : " << diners[j] << " - " << calc(diners[j], k) << endl;
                total_temp += calc(diners[j], k);
            }
//            cout << "total : " << k << " " << total_temp << endl;
            min_minutes = min(min_minutes, total_temp);
        }

        cout << "Case #" << i + 1 << ": " << min_minutes << endl;

    }

    return 0;
}