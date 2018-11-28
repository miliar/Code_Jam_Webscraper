#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>



#define For(i,n) for(int i(0),_n(n);i<_n;++i)

using namespace std;

bool isPal(int num) {
    int n, digit, rev = 0;
    n = num;
    do {
        digit = num%10;
        rev = (rev*10) + digit;
        num = num/10;
    } while (num!=0);

    if(n == rev) return true;
    else return false;
}


int main(int argc, char const *argv[]) {
    long long T;
    fstream f("in.in");
    f >> T;
    For(t,T) {
        long long A,B;
        long cnt = 0;
        f >> A;
        f >> B;
        for(int i=A; i<=B; ++i) {
            if(isPal(i)) {
                double sq = sqrt(i);
                double f = sq - floor(sq);
                if(f==0 && isPal(sq)) cnt++;
            }
        }

        cout << "Case #"<<t+1<< ": "<< cnt << endl;

    }
    f.close();
    return 0;
}
