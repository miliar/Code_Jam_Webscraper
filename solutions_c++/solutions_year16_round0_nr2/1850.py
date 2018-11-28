#include <iostream>
#include <fstream>

using namespace std;
using Int = long long;

Int solve(const string& str){
    Int rot = 0;
    for (Int j = 0; j < str.size()-1; ++j){
        if (str[j] != str[j+1]){
            ++rot;
        }
    }
    if (str[str.size()-1] == '-')
        ++rot;

    return rot;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    Int T;
    in >> T;
    string str;
    for (Int iT = 1; iT <= T; ++iT){
        in >> str;
        out << "Case #"<<iT<<": "<<solve(str)<<endl;
    }
    return 0;
}
