#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <set>
#include <cmath>
#include <fstream>

using namespace std;

ifstream in("A-large.in");
ofstream out("Al.out");

void a() {
    string s;
    in >> s;
    vector<int> c(10);
    for (int i = 0; i < s.length(); i++) {
        switch (s[i]) {
            case 'Z': {
                c[0]++;
                break;
            }
            case 'O': {
                c[1]++;
                break;
            }
            case 'W': {
                c[2]++;
                break;
            }
            case 'H': {
                c[3]++;
                break;
            }
            case 'U': {
                c[4]++;
                break;
            }
            case 'V': {
                c[5]++;
                break;
            }
            case 'X': {
                c[6]++;
                break;
            }
            case 'S': {
                c[7]++;
                break;
            }
            case 'I': {
                c[8]++;
                break;
            }
            case 'N': {
                c[9]++;
                break;
            }
        }
    }
    c[1] -= c[0]+c[2]+c[4];
    c[7] -= c[6];
    c[5] -= c[7];
    c[9] -= c[7]+c[1];
    c[9] /= 2;
    c[8] -= c[5]+c[9]+c[6];
    c[3] -= c[8];
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < c[i]; j++)
            out << i;
}

int main() {
    int n;
    in >> n;
    for (int i = 0; i < n; i++) {
        out << "Case #" << i+1 << ": ";
        a();
        out << endl;
    }
}
