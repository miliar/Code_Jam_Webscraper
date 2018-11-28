#include <iostream>
#include <math.h>

using namespace std;

int main() {
    
    int t, total, cnt, flag;
    unsigned long int sheep, n, number;
    cin >> t;
    
    for (int i = 1; i <= t; ++i) {
        
        cin >> n;
        
        sheep = n;
        
        total = 0;
        flag = 0;
        cnt = 1;
        while (total < 1023) {
            number = sheep;
            do {
                total |= 1 << (number % 10);
                number /= 10;
            } while (number != 0);
            sheep += n;
            cnt++;
            
            if (cnt > 1000000) {
                cout << "Case #" << i << ": " << "INSOMNIA" << endl;
                flag = 1;
                break;
            }
        }
        
        if (!flag) {
            cout << "Case #" << i << ": " << sheep-n << endl;
        }
    }
}