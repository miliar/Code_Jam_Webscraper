#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string.h>

using namespace std;

int pancakes(vector<int> vec, int max) {
    int minutes, altmin;
    minutes = max;

    for (int i = 1; i <= max; i++) {
        altmin = i;
        for (auto &d : vec) {
            if (d > i) {
                if(d%i == 0)
                    altmin += (d/i-1);
                else
                    altmin += (d/i);
            }
        }
        minutes = min(altmin, minutes);
    }
    return minutes;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T, D;
    cin >> T;
    ofstream myfile;
    myfile.open ("pancakes.txt");
    for (int i = 0; i < T; i++) {
        cin >> D;
        vector<int> vec;
        int max = 0;
        while (D--) {
            int input;
            cin >> input;
            if (input > max)
                max = input;
            vec.push_back(input);
        }
        myfile << "Case #" << i+1 << ": " << pancakes(vec, max) << endl;
    }
    myfile.close();
    return 0;
}
