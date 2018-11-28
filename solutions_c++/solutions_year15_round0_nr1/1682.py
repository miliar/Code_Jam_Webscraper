#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");
    int T, smax, n, x;
    char c;
    fin >> T;
    for(int i=0; i < T; i++){
        fin >> smax;
        n = 0;
        x = 0;
        for(int j=0; j <= smax; j++){
            fin >> c;
            if(n < j){
                while(n!=j){ n++; x++; }
            }
            n += ((int)(c) - 48);
        }
        fout<<"Case #"<<i + 1<<": "<<x<<"\n";
    }
    return 0;
}
