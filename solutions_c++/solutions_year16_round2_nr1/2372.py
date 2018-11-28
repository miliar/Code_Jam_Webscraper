#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main(){
    int T;
    ifstream in;
    in.open("c++/code_jam/A.in");
    ofstream out;
    out.open("c++/code_jam/A.txt");
    in >> T;

    for(int t=0; t<T; ++t){
        string S;
        in >> S;
        map<char, int> m;
        for (unsigned int i=0; i<S.size(); ++i){
            ++m[S[i]];
        }
        int tt[10]={};
        int f=m['X'];
        tt[6]=f;
          m['S']-=f; m['I']-=f;
        f=m['Z']; m['R']-=f; m['O']-=f; tt[0]=f;
        f=m['W']; m['T']-=f; m['O']-=f;            tt[2]=f;
        f=m['U']; m['F']-=f; m['O']-=f; m['R']-=f; tt[4]=f;
        f=m['R']; m['T']-=f; m['H']-=f; m['E']-=2*f; tt[3]=f;
        f=m['F']; m['I']-=f; m['V']-=f; m['E']-=f; tt[5]=f;
        f=m['O']; m['N']-=f; m['E']-=f; tt[1]=f;
        f=m['S']; m['N']-=f; tt[7]=f;
        tt[8]=m['T'];
        tt[9]=m['N']/2;
        out << "Case #" << t+1 << ": ";
        for (int i=0; i<10; ++i){
            for(int k=0; k<tt[i]; ++k) out << i;
        }
        out << "\n";
    }
}
