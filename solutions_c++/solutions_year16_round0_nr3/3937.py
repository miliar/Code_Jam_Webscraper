#include <iostream>
#include <fstream>
#include <string>
#include <climits>
#include <cmath>

using namespace std;
unsigned long n, base, b;
int divisor;

int main(int argc, const char * argv[]) {
    
    int divisores[11];
    int encontrados = 0;
    ofstream out("out.txt");
    
    out << "Case #1:\n";
    
    for (n = pow(2, 15) + 1; n < pow(2, 16); n+=2) {
        
        
        for (base = 2; base <= 10; base++) {
            
            b = 0;
            for (int bit = 0; bit < 16; bit++) {
                b += n & (1 << bit) ? pow(base, bit) : 0;
            }
            divisor = 2;
            while (divisor < b && divisor < 1000) {
                
                if (b % divisor == 0) {
                    //cout << n << " en base " << base << ": " << b << " tiene divisor " << divisor << "\n";
                    divisores[base] = divisor;
                    if (base == 10) {
                        
                        out << b;
                        for (int c = 2; c <= 10; c++) out << " " << divisores[c];
                        out << "\n";
                        encontrados++;
                        //cout << "Encontrados " << encontrados << "\n";
                    }
                    break;
                }
                divisor++;
            }
            if (divisor >= b || divisor >= 1000) { break; }
        }
        if (encontrados >= 50) break;
    }
    return 0;
}
