#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <math.h>
#include <vector>
#include <memory>
#include <map>
#include <queue>
#include <set>
#include <iterator>
#include <algorithm>
#include <functional>
#include <time.h>
#include <fstream>
#include <sstream>

using namespace std;


int main() {

    freopen("A-small-attempt0.in",  "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int T = 0;
    int R = 0;
    int C = 0;
    int W = 0;

    cin >> T;

    for ( int caseT = 0; caseT < T; ++caseT ) {
        cin >> R >> C >> W;
        int answer = 0;
        int first  = 0;
        int second = 0;

        if ( C == W ) {
            answer = W;
        } else {
            first = C / W;
            second = ( C % W == 0 ) ? W - 1 : W;
            answer = (first + second) * R;
        }

        cout << "Case #" << (caseT + 1) << ": " << answer << std::endl;
    }


    fclose(stdin);
    fclose(stdout);

    return 0;
}
