#include <iostream>
#include <string>
#include <cmath>
#include <boost/multiprecision/cpp_int.hpp>
#define ull uint128_t
using namespace std;
using namespace boost::multiprecision;

ull D[10];

ull divisor(ull number) {
    for(ull i=2; i<=10000; i++) {
        if (number % i == 0)
            return i;
    }
    return -1;
}

int main() {
    int N, J; cin >> N >> N >> J;
    cout << "Case #1:" << endl;
    
    int answers = 0;
    for(ull i=0; i<(1<<(N-2)); i++) {
        int ok = 0;
        ull display;
        
        for(int base=2; base<=10; base++) {
            ull number = 1;
            ull mult = base;
            ull x = i;
            for(int j=0;j<N-2;j++) {
                if (x%2) number+=mult;
                x/=2;
                mult *= base;
            }
            number+=mult;
            
            if (base==10) display=number;
            
            ull div = divisor(number);
            if (div == -1) break;

            D[base] = div;
            ok++;
        }
        
        if (ok == 9) {
            cout << display;
            
            for(int j=2; j<=10; j++) {
                cout << " " << D[j];
            }
            
            cout << endl;
            
            if (++answers >= J) break;
        }
    
    }


}
