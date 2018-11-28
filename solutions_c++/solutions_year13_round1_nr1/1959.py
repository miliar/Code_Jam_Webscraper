
#include <iostream>
#include <string>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <cmath>
using namespace std;

int main(int argc, const char * argv[])
{

    int T;
    cin >> T;
    for(int testcase=1;testcase<=T;testcase++) {
        unsigned long t,r;
        cin >> r >> t;

        unsigned long i;
        unsigned long count=0;
        for(i=r;i<=ULONG_MAX;i+=2) {
            unsigned long paint = 2*i+1;
            if(t<paint) {
                //cout << "less at " << count  << " pait " << t << endl;
                break;
            }
            else {
                t-=paint;
                count++;
            }
        }
        cout << "Case #" << testcase << ": " << count << endl;
    }
    return 0;
}

