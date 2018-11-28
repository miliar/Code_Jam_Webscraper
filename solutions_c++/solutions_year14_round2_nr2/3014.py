#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


#define For(i,n) for(int i(0),_n(n);i<_n;++i)

using namespace std;


int main(int argc, char const *argv[]) {
    long long T;
    long long A,B,K;
    fstream f("in.in");
    f >> T;
    For (t, T) {
        long long cnt = 0;
        f >> A >> B >> K;
        For (i, A) {
            For (j, B) {
                if ((i & j) < K) ++cnt;
            }
        }
        cout << "Case #"<<t+1<< ": "<< cnt << endl;
    }
    f.close();
    return 0;
}
