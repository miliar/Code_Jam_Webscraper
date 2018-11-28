
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int MinMoves(const string& seq){
    string str;
    str+=seq[0];
    int ind = 0;
    for(int i=1; i<seq.size(); i++){
        if(seq[i] != str[ind]){
            str+=seq[i];
            ind++;
        }
    }
    for(; ind>=0; ind--){
        if(str[ind]!='+'){
            break;
        }
    }

    return (ind+1);
}

int main(){
    ifstream inp;
    inp.open("B-large.in");
    ofstream out;
    out.open("codejam_out.txt");
    int num_tests = 0;
    inp >> num_tests;
    for(int t =1; t<= num_tests; t++){
        string str;
        inp >> str;

        int moves = MinMoves(str);
        out << "Case #" << t << ": "<<moves<<"\n";
    }
    inp.close();
    out.close();
    return 0;
}
