#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <limits>
#include <map>
#include <set>
#include <ctime>
#include <list>
#include <stack>
using namespace std;

int main() {
    ifstream fin("file.in");
    ofstream fout("file.out");

    int test, a, b, k;

    // Read
    fin >> test;
    for (int t = 1; t <= test; t++) {
        fin >> a >> b >> k;

        // Compute
        int nr = 0;
        for (int i = 0; i < a; i++)
            for (int j = 0; j < b; j++)
                if (i == j && i >= k)
                    continue;
                else {
                    int x = i & j;
                    if (x < k)
                        nr++;
                }

        // Print
        fout << "Case #" << t << ": " << nr << '\n';
    }
}
