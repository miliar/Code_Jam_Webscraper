#include <iostream>
#include <math.h>

using namespace std;
bool coinjam = true;

inline bool IsPrime(unsigned long long num){
    if(num == 0)
        return true;
    
    for(int i = 2; i <= sqrt(num); i++)
        if(num % i == 0)
           return false;
    
    return true;
}

inline unsigned long long bolumBul(unsigned long long sayi){
    
    for (int c = 2; c < sayi; c++) {
        if (sayi % c == 0) {
            return c;
        }
    }
    
    return 1;
}

inline void findDivisors(string array){
    unsigned long long sayim;
    
    for (int p = 2; p <= 10; p++) {
        sayim = stoull(array,NULL,p);
        if (p == 10) {
            cout << bolumBul(sayim) << endl;
        } else {
            cout << bolumBul(sayim) << " ";
        }
    }
}

int main() {
    
    int t,n,j;
    int miktar = 0;
    unsigned long long sayim = 0;
    cin >> t >> n >> j;
    string arr = "1000000000000001";
    
    cout << "Case #1:" << endl;
    
    for (int a = 14; a > 0; a--) {
        for (int b = a; b > 0; b--) {
            
            arr[b] = '1';
            
            for (int x = 2; x <= 10; x++) {
                sayim = stoull(arr,NULL,x);
                
                if (IsPrime(sayim)) {
                    coinjam = false;
                    break;
                }
            }
            
            if (coinjam) {
                cout << arr << " ";
                findDivisors(arr);
                miktar++;
                
                if (miktar == j) {
                    return 0;
                }
            }
            
            arr[b] = '0';
            coinjam = true;
            
        }
        
        arr[a] = '1';
    }

    return 0;
}
