#include <iostream>
#include <string>
#include <fstream>

using namespace std;
using Int = unsigned long long;

int main(){
    ofstream out("output.txt");
    ifstream in("input.txt");
    Int T,K,C,S;
    in >> T;
    for (Int iT = 1; iT <= T; ++iT){
        in >> K >> C >> S;
        out <<"Case #"<<iT<<": ";
        if (C == 1){
            if (S < K)
                out <<"IMPOSSIBLE";
            else
                for (Int ip = 1; ip <= K; ++ip)
                    out <<ip <<" ";
            out << endl;
        }
        else{
            if (S < K-1)
                out << "IMPOSSIBLE";
            else
                for (Int ip = 2; ip <= K; ++ip)
                    out << ip << " ";
                if (K == 1)
                    out << 1;
            out << endl;
        }
    }

    return 0;
}
