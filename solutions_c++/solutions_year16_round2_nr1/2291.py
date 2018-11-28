#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int main () {
    ifstream in ("1.in");
    ofstream out ("1.out");

    int testcases;
    in >> testcases;
    for (int t = 1; t <= testcases; ++t) {
        out << "Case #" << t <<": ";
        string str;
        in >> str;
        map<char, int> db;
        int sol[10];
        for (int i=0; i<str.length(); i++) {
            db[str[i]]++;
        }
        sol[6]=db['X'];
        sol[7]=db['S']-sol[6];
        sol[5]=db['V']-sol[7];
        sol[4]=db['U'];
        sol[2]=db['W'];
        sol[0]=db['Z'];
        sol[3]=db['R']-sol[0]-sol[4];
        sol[8]=db['T']-sol[2]-sol[3];
        sol[1]=db['O']-sol[0]-sol[2]-sol[4];
        sol[9]=db['I']-sol[5]-sol[6]-sol[8];
        for(int i=0;i<10;++i)
            for (int j=0;j<sol[i];j++)
                out<<i;
        out <<endl;
    }
}

