#include <iostream>
#include <map>
#include <vector>
#include <bitset>
#include <string>
#include <algorithm>

using namespace std;



bool done(vector<bool> &v) {
    bool d = true;

    for (int i = 0; i < v.size(); ++i) {
        d &= v[i];
    }

    return d;
}


int doit() {
    vector<bool> pancakes;

    string line;

    while (true) {
        getline(cin, line);

        if (line.length() > 0) {
            break;
        }
    }

    for (int j = 0; j < line.length(); ++j) {
        char c = line[j];

        if (c == '-') {
            pancakes.push_back(false);
        } else if (c == '+'){
            pancakes.push_back(true);
        } else {
            break;
        }
    }

//    cout << "got " << pancakes.size() << " pancakes" << endl;
//    int last = pancakes.size() - 1;

    int flips = 0;

    while (true) {
        if (done(pancakes)) {
            break;
        }

//        int same = 0;

        bool val = pancakes[0];

        int j;
        for (j = 1; j < pancakes.size(); ++j) {
            if (pancakes[j] != val) {
//                j--;
                break;
            }
        }

        reverse(pancakes.begin(), pancakes.begin() + j);

        // flip'em
        for (int i = 0; i < j; ++i) {
            pancakes[i] = !pancakes[i];
        }

        flips++;





//        if (pancakes.size() <= 0) {
//            break;
//        }
//
//        int last = pancakes.size() - 1;
//
//        if (!pancakes[last]) {
////            cout << "flipping at " << last << endl;
//            flips++;
//
//            pancakes.pop_back();
//
//
//
////            last--; // don't remove or endless loop
//        } else {
//            pancakes.pop_back();
////            last--;
//        }

    }

    return flips;
}

int main() {
    int cases;

    cin >> cases;

    for (int i = 0; i < cases; ++i) {
        printf("Case #%d: %d\n", i+1, doit());
    }

    return 0;
}