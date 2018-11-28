#include <iostream>
#include <fstream>
#include <string>
using namespace std;
//using Int = __int128_t;
using Int = long long;

string solve(const string& str){
    string res;
    res += str[0];
    for (Int i = 1; i < str.size(); ++i){
        if (str[i] >= res[0]){
            res = str[i] + res;
        }
        else{
            res += str[i];
        }
    }
    return res;
}

int main(){
    ifstream in("input.txt");
    ofstream out("output.txt");
    Int T;
    string str;
    in >> T;
    for (Int iT = 1; iT <= T; ++iT){
        in >> str;
        out<<"Case #"<<iT<<": "<<solve(str)<<endl;
    }

    return 0;
}
