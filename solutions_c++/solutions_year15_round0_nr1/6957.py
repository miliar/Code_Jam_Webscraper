#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cstdlib>
#include <string>
using namespace std;

int main(void) {

ifstream fin ("A-large.in");
ofstream fout ("A-large.out");

int T;
fin >> T;

for(int i=0; i<T; i++) {

    int a = 0;
    int f = 0;
    int t = 0;
    string c;
    fin >> t;
    fin >> c;
    for(int s=0; s<=t; s++) {
        int si = (int) c[s]-'0';
        if(s==0 && si==0) {
            a+=1;
            f++;
        }
        //cout << "s" << s << "a" << a;
        while(si!=0 && s>a) {
            a++;
            f++;
        }
        a+=si;
    }

    fout << "Case #"<< (i+1) << ": " << f;
    if(i!=T-1)
        fout << endl;
}


return 0;
}
