#include <iostream>


using namespace std;

int main(int argc, char **argv) {
    int max_tc, tc = 1;
    cin >> max_tc;

    while(max_tc--) {
        long long r, t;
        cin >> r >> t;

        long long old_size = 0;
        long long size = 0;
        long long cnt = 1, r2 = r+1;
        for (cnt = 0; size <= t; cnt++, r2+=2) {
            size += 2*r2 - 1;
        }

        cout << "Case #" << tc++ << ": " << (cnt-1) << endl;
    }

    return 0;
}