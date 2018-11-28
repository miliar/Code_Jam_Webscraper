#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <cmath>
using namespace std;

int a(int n) {
    if (n==0) return 0;
    vector<bool> asd(10, false);
    int notYet = 10;
    int i;
    for (i = 1; notYet>0; i++) {
        int a = 1;
        for (int j = 0; j < floor(log10(i*n))+1; j++) {
        if (!asd[(i*n/a) % 10]) {
            asd[(i*n/a) % 10] = true;
            notYet--;
        }
        a *= 10;
        }
    }
    return (--i)*n;
}

int main() {
    ifstream in("A-large.in");
    ofstream out("a_large.out");
    int n;
    in >> n;
    for (int i = 0; i < n; i++) {
        int k;
        in >> k;
        int asd = a(k);
        out << "Case #" << i+1 << ": " << ((asd==0)?"INSOMNIA":to_string(asd)) << endl;
    }
}
