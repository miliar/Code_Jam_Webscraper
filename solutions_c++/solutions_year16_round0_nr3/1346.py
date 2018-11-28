#include <bits/stdc++.h>
using namespace std;
long long val2, val3, val4, val5, val6, val7, val8, val9, val10;
int primes[500];
bool isPrime(long long a){
    for(long long i = 2; i <= sqrt(a); i++){
        if(a%i == 0)
            return false;
    }
    return true;
}
long long power(int a, int b, int mod){
    long long result = 1;
    for(int i = 1; i <= b; i++)
        result = ((result)%mod*(a)%mod)%mod;
    return result;
}
bool base2(int n){
    for(int j = 0; j < 200; j++){
        long long res = 1 + power(2, 31, primes[j]);
        for(int i = 0; i <=30; i++){
            if((1<<i)&n)
                res += power(2, i+1, primes[j]);
        }
        if(!(res%primes[j])){
            val2 = primes[j];
            return true;    
        }
    }
    return false;
}
bool base3(int n){
    for(int j = 0; j < 200; j++){
        long long res = 1 + power(3, 31, primes[j]);
        for(int i = 0; i <=30; i++){
            if((1<<i)&n)
                res += power(3, i+1, primes[j]);
        }
        if(!(res%primes[j])){
            val3 = primes[j];
            return true;    
        }
    }
    return false;
}
bool base4(int n){
    for(int j = 0; j < 200; j++){
        long long res = 1 + power(4, 31, primes[j]);
        for(int i = 0; i <=30; i++){
            if((1<<i)&n)
                res += power(4, i+1, primes[j]);
        }
        if(!(res%primes[j])){
            val4 = primes[j];
            return true;    
        }
    }
    return false;
}
bool base5(int n){
    for(int j = 0; j < 200; j++){
        long long res = 1 + power(5, 31, primes[j]);
        for(int i = 0; i <=30; i++){
            if((1<<i)&n)
                res += power(5, i+1, primes[j]);
        }
        if(!(res%primes[j])){
            val5 = primes[j];
            return true;    
        }
    }
    return false;
}
bool base6(int n){
    for(int j = 0; j < 200; j++){
        long long res = 1 + power(6, 31, primes[j]);
        for(int i = 0; i <=30; i++){
            if((1<<i)&n)
                res += power(6, i+1, primes[j]);
        }
        if(!(res%primes[j])){
            val6 = primes[j];
            return true;    
        }
    }
    return false;
}
bool base7(int n){
    for(int j = 0; j < 200; j++){
        long long res = 1 + power(7, 31, primes[j]);
        for(int i = 0; i <=30; i++){
            if((1<<i)&n)
                res += power(7, i+1, primes[j]);
        }
        if(!(res%primes[j])){
            val7 = primes[j];
            return true;    
        }
    }
    return false;
}
bool base8(int n){
    for(int j = 0; j < 200; j++){
        long long res = 1 + power(8, 31, primes[j]);
        for(int i = 0; i <=30; i++){
            if((1<<i)&n)
                res += power(8, i+1, primes[j]);
        }
        if(!(res%primes[j])){
            val8 = primes[j];
            return true;    
        }
    }
    return false;
}
bool base9(int n){
    for(int j = 0; j < 200; j++){
        long long res = 1 + power(9, 31, primes[j]);
        for(int i = 0; i <=30; i++){
            if((1<<i)&n)
                res += power(9, i+1, primes[j]);
        }
        if(!(res%primes[j])){
            val9 = primes[j];
            return true;    
        }
    }
    return false;
}
bool base10(int n){
    for(int j = 0; j < 200; j++){
        long long res = 1 + power(10, 31, primes[j]);
        for(int i = 0; i <=30; i++){
            if((1<<i)&n)
                res += power(10, i+1, primes[j]);
        }
        if(!(res%primes[j])){
            val10 = primes[j];
            return true;    
        }
    }
    return false;
}
void print(int a){
    for(int i = 29; i >= 0; i--){
        if((1<<i)&a)
            cout<<1;
        else
            cout<<0;
    }

}
int main()
{
    long long t, n, j, ans = 0, k = 0;
    for(int i = 2; i <= 1223; i++){
        if(isPrime(i))
            primes[k++] = i;
    }
    cin>>t;
    for(int test = 1; test <= t; test++){
        cin>>n>>j;
        cout<<"Case #"<<test<<":"<<endl;
        for(int i = 0; i <= 1073741824; i++){
            if(base2(i) && base3(i) && base4(i) && base5(i) && base6(i) && base7(i) && base8(i) && base9(i) && base10(i)){
                ans++;
                cout<<1;
                print(i);
                cout<<"1 "<<val2<<" "<<val3<<" "<<val4<<" "<<val5<<" "<<val6<<" "<<val7<<" "<<val8<<" "<<val9<<" "<<val10<<endl;
            }
            if(ans == 500)
                break;
        }
    }
}