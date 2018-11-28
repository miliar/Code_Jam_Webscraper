#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <iomanip>
#include <cstdio>

using namespace std;

typedef long double ld;

int tests;
int num_test;
ld c, f, x;

int main(int argc, char const* argv[]){
    cin >> tests;

    for (int i = 0; i < tests; i++) {
        cin >> c >> f >> x;

        ld actual_cook = 0;
        ld total_time = 0;
        ld cook_per_sec = 2;
        while (actual_cook < x){
            if ( ((c / cook_per_sec) + (x / (cook_per_sec + f))) < (x / cook_per_sec) ){
                total_time +=  (c / cook_per_sec);
                cook_per_sec += f;
                actual_cook = 0;
            }
            else {
                total_time += (x / cook_per_sec);
                actual_cook = x;
            }

        }

        cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << total_time << endl;
    }

    return 0;
}
