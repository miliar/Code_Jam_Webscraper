#include <iostream>

using namespace std;

int main() {
    
    int t;
    int caseOrder = 1;
    long int carpim;
    long int n;
    int n2;
    int x;
    bool bitti = true;
    cin >> t;
    int array[10] = {0};
    int sayac = 0;
    
    while (t--) {
        cin >> n;
        carpim = n;
        
        if (n == 0) {
        
            cout << "Case #" << caseOrder++ << ": INSOMNIA" << endl;
            continue;
        
        } else {
            
            while (n) {
                
                n2 = n;
                
                while (n2) {
                    x = n2 % 10;
                    array[x]++;
                    n2 = n2/10;
                }
                
                n += carpim;
                
                for (int q = 0; q < 10; q++) {
                    if (array[q] > 0) {
                        ++sayac;
                    }
                }
                
                if (sayac == 10) {
                    bitti = true;
                    sayac = 0;
                    break;
                }
                
                sayac = 0;
            }
        }
        
        if (bitti == true) {
            cout << "Case #" << caseOrder++ << ": " << n-carpim << endl;
        }
        
        for (int q = 0; q < 10; q++) {
            array[q] = 0;
        }
    }

    return 0;
}
