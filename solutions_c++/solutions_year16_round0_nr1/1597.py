#include <bitset>
#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char * argv[])
{
    if (argc != 2)
        return 0;
    
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    
    int T, N;
    int t, n, mul, d;
    bitset<10> digits;
    int d_count;
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> N;
        
        if (N == 0)
            fout << "Case #" << t << ": INSOMNIA" << endl;
        else {
            digits.reset();
            d_count = 0;
            mul = 0;
            
            while (d_count < 10) {
                mul++;
                n = N * mul;
                
                while (n > 0) {
                    d = n % 10;
                    
                    if (!digits[d]) {
                        digits.set(d);
                        d_count++;
                    }
                    
                    n /= 10;
                }
            }
            
            fout << "Case #" << t << ": " << N * mul << endl;
        }
    }
    
    
    return 0;
}
