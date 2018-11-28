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

int main(/*int argc, const char * argv[]*/) {

    freopen("A-large.in",  "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T = 0;
    int N = 0;

    string inputString;

    cin >> T;

//    cout << "Ci sono " << T << " casi da risolvere " << std::endl;

    for ( int caseT = 0; caseT < T; ++caseT ) {
        cin >> N;             // shyniness level
        char inputString[N];  // room configuration
        cin >> inputString;

        int required = 0;
        int sum = 0;

        for ( int k = 0; k < N+1; ++k ) {
            int value = inputString[k] - '0';

            if ( value != '0' ) {
                required += (sum + required < k) ? k - (sum + required) : 0;
            }

            sum += value;
        }

        cout << "Case #" << (caseT + 1) << ": " << required << std::endl;
    }


    fclose(stdin);
    fclose(stdout);

    return 0;
}

