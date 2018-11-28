#include <iostream>
#include <fstream>
#include <string>
#define GW fout << "Case #"<< i+1 <<": " << "GABRIEL" << endl
#define RW fout << "Case #"<< i+1 <<": " << "RICHARD" << endl
using namespace std;
int main(int argc, const char * argv[]) {
    ifstream fin("D-small-attempt0.in.txt");
    ofstream fout("D-small-attempt0.out.txt");
    int T, x, r, c;
    fin >> T;
    for (int i=0; i<T; i++) {
        fin >> x >> r >> c;
        int tmp = r * c;
        if (x == 1)
            GW;
        
        if (x == 2){
            if (tmp % 2 == 0)
                GW;
            else
                RW;
        }
        
        if (x == 3) {
            if (tmp == 6 or tmp == 9 or tmp == 12)
                GW;
            else
                RW;
        }
        
        if (x == 4) {
            if (tmp == 12 or tmp == 16)
                GW;
            else
                RW;
            
        }
    }
    fin.close();
    fout.close();    
}

