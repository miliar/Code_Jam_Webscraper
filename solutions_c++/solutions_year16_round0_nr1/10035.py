#include <bits/stdc++.h>

using namespace std;

bool digits[10];

bool check(){
    for(int i = 0; i < 10; i++)
        if(digits[i] == false)return false;
    return true;
}

void one(unsigned long long n){
    if(n <= 9){
        digits[n] = true;
        return;
    }
    if(check() == true) return;
    digits[n%10] = true;
    one(n/10);
}

int main()
{
    
    int t, q;
    cin >> t;
    
    q = t;
    
    while(t--){
        unsigned long long n;
        cin >> n;
        
        if(n == 0){
            cout << "Case #" << q-t << ": INSOMNIA" << endl;
        }
        else {
            for(int i = 0; i < 10; i++)
                digits[i] = false;
                
            int k;
            for(k = 1; check() == false; k++)
                one(n*k);
            
            cout << "Case #" << q-t << ": " << n*(k-1) << endl;
        }
    }
    
    return 0;
}
