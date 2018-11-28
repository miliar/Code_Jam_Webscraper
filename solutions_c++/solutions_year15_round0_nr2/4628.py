#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int time (vector<int> plate) {

//    for (int i = 0; i < plate.size(); i++) {
//        cout << plate[i] << " ";
//    }
//    cout << endl;

    int high = 0;
        vector<int> highIndex;

        for (int i = 0; i < plate.size(); i++) {
            if (plate[i] > high) {
                highIndex.clear();
                high = plate[i];
                highIndex.push_back(i);
            } else if (plate[i] == high) {
                highIndex.push_back(i);
            }
        }
//
        if (high <= 1) {
            return high;
        }

////        for (int i = 0; i < highIndex.size(); i++) {
////        cout << highIndex[i] << " ";
////    }
////    cout << endl;
//
//        //if (highIndex.size() < high / 2) {
            if (high == 9 ) {
                int low = high;
                vector <int> temp = plate;
                for (int i = 0; i < highIndex.size(); i++) {
                    plate[highIndex[i]] = (high + 1)/2;
                    plate.push_back(high/2);

                }

                low = min (low,(int)highIndex.size() + time (plate));

                plate = temp;
                for (int i = 0; i < highIndex.size(); i++) {
                    plate[highIndex[i]] = 3;
                    plate.push_back(3);
                    plate.push_back(3);
                }

                return min (low, 2 * (int)highIndex.size() + time (plate));

            }

            for (int i = 0; i < highIndex.size(); i++) {
                plate[highIndex[i]] = (high + 1)/2;
                plate.push_back(high/2);

            }

            return min (high, (int)highIndex.size() + time (plate));
//        } else {
//            return high;
//        }
}

int main () {
    freopen ("B-small-attempt3.in","r",stdin);
    freopen ("B-small-attempt3.out","w",stdout);
    int t;
    cin >> t;

    for (int a = 1; a <= t; a++) {

        int p;
        cin >> p;
        vector<int> plate(p);
        for (int i = 0; i < p; i++) {
            cin >> plate[i];
        }

        cout << "Case #" << a << ": " << time(plate) << endl;

    }

    return 0;
}
