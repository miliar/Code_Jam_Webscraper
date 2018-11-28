#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


#define For(i,n) for(int i(0),_n(n);i<_n;++i)

using namespace std;

int main(int argc, char const *argv[]) {
    long long T;
    fstream f("in");
    f >> T;
    For(t,T) {
        long long r,tt;
        f >> r;
        f >> tt;

        long long radius = r;
        long long cnt = 0;

        while(tt >= 0) {
            tt -= 2*radius+1;
            radius += 2;
            cnt++;
        }


        cout << "Case #"<<t+1<< ": " << cnt-1 << endl;

        stop:;
    }
    f.close();
    return 0;
}
