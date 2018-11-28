#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(){
    ifstream input;
    string ff;
    cin >> ff;
    input.open(ff);
    ofstream out;
    out.open("c++/code_jam/gold.txt");
    int T;
    input >> T;
    for(int t=1; t<=T; ++t){
        long long k, c, s;
        input >> k >> c >> s;
        out << "Case #" << t << ": ";
        if (s==k){
            for (int j=1; j<=s; ++j) {
                out << j << " ";
            }
            out << "\n";
            continue;
        }
        if (k > s*c) {
            out << "IMPOSSIBLE\n";
            continue;
        }
        for (long long j=0; j< k; j+=c){
            long long h=1+ j* pow(k, c-1);
            for (long  long i=j+2; i<=min(c+j, k); ++i){
                h+= (i-1)* pow(k, ((c+j)-i));
            }
            out << h << " ";
        }
        out << "\n";


    }
}
