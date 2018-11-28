#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

int build(int,int);

int main()
{
    int tests, counts=1, k, c, s;
    ifstream fin("D-small-attempt0.in");
    ofstream fout("data.out",std::ofstream::trunc);
    fin >> tests;
    while(!fin.eof()&&tests){
        fin >> k >> c >> s;
        tests--;
        string result="";
        cout << "Case #"<< counts << ":";
        fout << "Case #"<< counts << ":";
        if(s<k){
            cout << " IMPOSSIBLE";
            fout << " IMPOSSIBLE";
        } else {
            for(int i=1; i<=s; i++){
                cout << " " << i;
                fout << " " << i;
            }
        }
        counts++;
        if(tests){
            cout << endl;
            fout << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;;
}
