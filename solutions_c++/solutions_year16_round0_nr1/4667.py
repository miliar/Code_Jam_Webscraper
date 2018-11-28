#include <iostream>
#include <fstream>
#include <string>
#include <climits>

using namespace std;

int num, numc, multi, numo;
int n, ns;
unsigned bits;

int main(int argc, const char * argv[]) {
    
    ifstream in("in.txt");
    ofstream out("out.txt");
    in >> ns;
    
    for (n = 0; n < ns; n++) {
        
        multi = 1;
        in >> numo;
        bits = 0;
        num = numo;
        while (numo != 0) {
            
            numc = num;
            do {
                bits |= 1 << (numc %10);
                numc /= 10;
                
            } while (numc != 0);
            if (bits == 0x03FF) break;
            multi++;
            num = numo * multi;
            if (num > INT_MAX / 2) { num = 0; break; }
        }
        
        out << "Case #" << n + 1 <<": ";
        if (num != 0)
            out << num << "\n";
        else
            out << "INSOMNIA" << "\n";
    }
    cout << "end";
    return 0;
}
