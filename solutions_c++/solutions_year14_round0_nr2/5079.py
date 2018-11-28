/*Input 
 	
Output 
 
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762
*/

#include <sstream>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdint>

#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <set>

#include <string>

#include <stdint.h>
#include <limits>

using namespace std;
typedef pair<int, int> pii;

int main() {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int a1[4][4], a2[4][4];
    int N;
    string row;
    const double gap = 10e-6;
    cin >> N;
    int i = 0;
    double ret = 0.0;
    while (i++ < N) {
        ret = 0.0;
        double cost, farm, tar;
        cin >> cost >> farm >> tar;
        double rate = 2.0;
        while (true) {
            if (cost / rate + tar / (rate + farm) < tar / rate) {
                double next_t = cost / rate;
                rate += farm;
                ret += next_t;
            }  else {
                ret += tar / rate;
                break;
            }
        }
        printf("Case #%d: %lf\n", i, ret);
        //        cout << "Case #" <<  i << ": " << ret << endl;
    }
}


