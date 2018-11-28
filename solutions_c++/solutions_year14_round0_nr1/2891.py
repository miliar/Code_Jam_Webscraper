/* 
 * File:   main.cpp
 * Author: bacho
 *
 * Created on April 12, 2014, 11:45 AM
 */

#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

ifstream ifs("a.in");
ofstream ofs("a.out");

void copy(int a[4], int b[4]) {
    for (int i = 0; i < 4; i++)
        b[i] = a[i];
}

string chack(int row1[4], int row2[4]) {
    int ans = 0;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (row1[i] == row2[j]) {
                if (ans != 0) return "Bad magician!";
                ans = row1[i];
            }
    if (ans == 0) return "Volunteer cheated!";
    stringstream ss;
    ss << ans;
    return ss.str();
}

int main() {
    int t, i = 1;
    ifs>>t;
    while (t--) {
        int r, k = 2;
        int row1[4], row2[4];
        while (k--) {
            ifs>>r;
            for (int j = 1; j < 5; j++) {
                int c[4];
                ifs >> c[0] >> c[1] >> c[2] >> c[3];
                if (j == r)
                    if (k == 1)copy(c, row1);
                    else copy(c, row2);
            }
        }
        ofs << "Case #" << i << ": " << chack(row1, row2) << "\n";
        i++;
    }
    return 0;
}

