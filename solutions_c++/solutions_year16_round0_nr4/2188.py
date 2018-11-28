#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    fstream in("D-small-attempt1.in", ios::in);
    fstream out("fractiles.out", ios::out);
    int t, k, c, s;
    in >> t;
    for(int cas = 1; cas <= t; cas++) {
        in >> k >> c >> s;
        out << "Case #" << cas << ": ";
        for(int i = 1; i <= k; i++) {
            out << i << " ";
        }
        out << endl;
    }
    return 0;
}
