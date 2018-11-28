#include <iostream>
#include <string>
#include <cctype>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <fstream>
#include <map>
#define out fout
#define in fin
using namespace std;

int main()
{
    ofstream out ("output.out");
    ifstream in ("input.in");
    int t;
    in >> t;
    for(int tt = 1; tt <= t; tt++) {
        int a, b, k, ans = 0;
        in >> a >> b >> k;
        for(int i = 0; i < a; i++) {
            for(int j = 0; j < b; j++) {
                if((i&j) < k) {
                    ans++;
                }
            }
        }
        out << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
