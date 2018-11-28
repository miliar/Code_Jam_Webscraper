
#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;
using namespace boost::multiprecision;


using Int = int128_t;
const Int T = 1;
const int N = 32;
const Int J = 500;
const int minBase = 2;
const int maxBase = 10;
bool bits[N];
Int divs[maxBase+1];
ofstream out("output.txt");

void fillBits(Int Number){
    for (int i = 1; i < N-1; ++i){
        bits[i] = bool(Number % 2);
        Number /= 2;
    }
}

void print(){
    for (int i = 0; i < N; ++i){
        out << bits[i];
        //cout << bits[i];
    }
    //cout << endl;
    out <<" ";
    for (int ibase = minBase; ibase <= maxBase; ++ibase){
        out << divs[ibase] <<" ";
    }
    out << endl;
}

Int to(Int base){
    Int res = 0;
    Int power = 1;
    for (int i = N-1; i >= 0; --i){
        if (bits[i]){
            res += power;
        }
        power *= base;
    }
    cout<<"to "<<base<<" is "<<res<<endl;
    return res;
}

Int divisor(const Int Number){
    Int maxi = 100;
    for (Int i = 2; i < maxi; ++i){
        if (Number % i == 0)
            return i;
    }
    return 0;
}

void solve(){
    memset(bits, 0, sizeof(bool)*N);
    bits[0] = bits[N-1] = 1;
    Int maxi = 1 << 14;
    //cout<<"maxi "<<maxi<<endl;
    for (Int i = 0,j = 0; j != J; ++i){
        fillBits(i);

        //printBits();
        //cout<<to<3>()<<endl;
        int ibase = minBase;
        for (; ibase <= maxBase; ++ibase){
            Int div = divisor(to(ibase));
            if (div){
                divs[ibase] = div;
            }
            else{
                break;
            }
        }
        if (ibase == maxBase+1){
            print();
            ++j;
        }
    }
}

int main(){
    out << "Case #1:" << endl;
    solve();


    cout << "Hello world!" << endl;
    return 0;
}
