#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

//ifstream fin("input.txt");
//ofstream fout("output.txt");
istream &fin = cin;
ostream &fout = cout;

inline char other(char c){
    return c=='+' ? '-' : '+';
}

string s;

int solve(int last, char dest){
    if(last<0) return 0;
    else if(last==0){
        if(s[0]==dest) return 0;
        else return 1;
    }

    //last>=1
    while(last>=0 && s[last]==dest) --last;
    if(last<0) return 0;
    else return solve(last,other(dest))+1;
}


int main(){
    int T; fin>>T;

    for(int tc=1; tc<=T; ++tc){
        fin>>s;

        fout<<"Case #"<<tc<<": "<< solve(s.length()-1,'+') <<'\n';
    }
}
