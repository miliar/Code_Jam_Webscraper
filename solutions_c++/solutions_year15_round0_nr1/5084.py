#include <iostream>
#include <queue>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <climits>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

#define fori(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define ford(i, a, b) for(int (i) = (a)-1; (i) >= (b); --(i))
#define test(t) while((t)--)
#define MP make_pair
#define mod 1000000007

int main() {
    ifstream read;
    ofstream write;
    read.open ("A-large.in");
    //read.open ("a.in");
    write.open ("a.out");
    int t, ccase = 1;
    read >> t;
    while (ccase <= t) {
        int smax;
        read >> smax;
        string data;
        read >> data;
        int cstand = 0, required = 0, size = data.size();
        cstand = int(data.at(0)-'0');
        fori (i, 1, size) {
            //cout << cstand << "  kk " << endl;
            if (cstand < i) {
                //cout << i << endl;
                required += (i - cstand);
                cstand += (i - cstand);
            }
            cstand += int(data.at(i)-'0');
        }
        write << "Case #" << ccase << ": " << required << endl;
        ccase++;
    }
    return 0;
}
