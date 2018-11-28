#include <iostream>
#include <fstream>
#include <limits>
#include <set>
#include <cmath>

using namespace std;
using Int = long long;
set<Int> Digits;

Int pow10(Int k){
    Int res = 1;
    for (int ik = 1; ik <= k; ++ik){
        res *= 10;
    }
    return res;
}

void toSet(Int N){
    //cout <<"toSet: "<<N<<endl;
    while (N){
        Int digit = N % 10;
        //cout<<"digit = "<<digit<<endl;
        Digits.insert(digit);
        N /= 10;
    }
}

Int solve(const Int N){
    if (N == 0) return -1;
    Int i = 0;
    while(Digits.size() != 10){
        ++i;
        toSet(N*i);
        if (N*i > (numeric_limits<Int>::max()-2e6)){
            Digits.clear();
            cout<<"WARNING: Int overflow! \n";
            return -1;
        }
    }
    Digits.clear();
    return N*i;
}

int main(){
    ifstream in("input.txt");
    ofstream out("output.txt");
    Int T, N;
    in >> T;
    for (Int iT = 1; iT <= T; ++iT){
        in >> N;
        out<<"Case #"<<iT<<": ";
        Int res = solve(N);
        if (res > 0)  out << res;
        else  out << "INSOMNIA";
        out << endl;
    }
    return 0;
}
