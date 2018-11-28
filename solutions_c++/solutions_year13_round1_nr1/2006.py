#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(void){

ifstream fin ("A-small-attempt0.in");
ofstream fout("output.txt");

int T;
unsigned long long int r, t;


fin >> T;

for(int i=0; i<T; i++){
    fin >> r >> t;

    unsigned long long int blackradius, resultingarea;

    int count = 0;
    while(true){

        blackradius = (r+1);

        resultingarea = (blackradius*blackradius) - (r*r);

        if(resultingarea <= t){
            count++;
            t -= resultingarea;
            r+=2;
        }else{
            break;
        }
    }

    fout << "Case #" << (i+1) << ": " << count;

    if(i != (T-1)){
        fout << endl;
    }

}

return 0;
}
