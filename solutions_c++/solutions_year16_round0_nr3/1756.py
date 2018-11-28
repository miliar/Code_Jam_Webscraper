#include <iostream>

using namespace std;
typedef unsigned long long int ullint;

ullint intToBin(ullint x, ullint n) {
    
    ullint dec = 0;
    
    for(ullint b = 1 << n; b > 0; b >>= 1 ) {
        dec *= 10;
        if(b & x)
            dec += 1;
    }
    
    return dec;
}

ullint base(ullint x, int b) {
    ullint xb = 0;
    ullint p = 1;
    while(x > 0) {
        ullint q = x%10;
        xb += (q*p);
        p *= b;
        x /= 10;
    }
    
    return xb;
}

bool notPrime(ullint x) {
    
    for(int i = 2; i <= 10; i++) {
        ullint xb = base(x, i);
        
        bool prime = true;
        for(ullint k = 2; k < 100 && prime; k++) {
            if(xb % k == 0)
                prime = false;
        }

        if(prime)
            return false;
    }
    
    return true;
}

ullint div(ullint x, int b) {
    
    ullint xb = base(x, b);
    
    for(ullint k = 2; k < 100; k++)
        if(xb % k == 0)
            return k;
        
    return 0;
}

int main()
{
    int T, cont = 0;
    
    cin >> T;

    while(T--)
    {
        ullint n, j, x = 1, xmid, xsum, sum = 0;
        
        cin >> n >> j;
        
        for(ullint i = 0; i < n-1; i++)
            x *= 10;
        x++;
        
        cout << "Case #" << ++cont << ": " << endl;
        
        for(ullint i = 0 ; sum < j && i < 16384 ; i++) {
            xmid = intToBin(i, n) * 10;
            xsum = x + xmid;
            
            if(notPrime(xsum)) {
                cout << xsum << " ";
                for(int k = 2; k <= 10; k++)
                    cout << div(xsum, k) << " ";
                cout << endl;
                
                sum++;
            }
        }
        
    }
        
return 0;
}
