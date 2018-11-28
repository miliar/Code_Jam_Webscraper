#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <stdio.h>

using namespace std;

int main() {
    ifstream fin("/Users/usamaelnily/Desktop/in.txt");
    ofstream fout("/Users/usamaelnily/Desktop/out.txt");
    int cs, ts;
    fin >> cs;
    ts = cs;
    while(cs--) {
        long double t = 0, r = 2, C, F, X, thres;
        fin >> C >> F >> X;
        thres = ((F * X) / C) - F;
        while(r < thres) {
            t += C/r;
            r += F;
        }
        t += X/r;
        fout << setiosflags(ios::fixed) << setprecision(7) << "Case #" << ts - cs << ": " << t << endl;
    }
    return 0;
}