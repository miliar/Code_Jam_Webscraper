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

    freopen("D-small-attempt0.in",  "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T = 0;
    int x = 0;
    int r = 0;
    int c = 0;
    bool gab = false;
    string answer = "";

    cin >> T;

    for ( int caseT = 0; caseT < T; ++caseT ) {
        cin >> x >> r >> c;

//        cout << x << " " << r << " " << c << "\n";

        gab = false;

        if ( x == 1 )
            gab = true;

        if ( x == 2 )
            if ( (r * c) % 2 == 0 )
                gab = true;

        if ( x == 3 )
            if ( (r * c) % 3 == 0 && r > 1 && c > 1 )
                gab = true;

        if ( x == 4 )
            if ( (r == 4 && c == 3) || (r == 3 && c == 4) || (r == 4 && c == 4) )
                gab = true;


        answer = gab ? "GABRIEL" : "RICHARD";

        cout << "Case #" << (caseT + 1) << ": " << answer << std::endl;
    }


    fclose(stdin);
    fclose(stdout);

    return 0;
}

