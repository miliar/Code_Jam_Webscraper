#include <iostream>
#include <string>
#include <vector>

using namespace std;

int n, tot, counter;

long long power(long long a, long long b) {
    if( b == 0 ) return 1;
    long long ret = power(a, b / 2);
    ret *= ret;
    
    if( b % 2 ) ret *= a;
    return ret;
}

long long isPrime(long long a) {
    for(long long i = 2; i * i <= a; i++) {
        if( a % i == 0 ) return i;
    }
    
    return a;
}

int f(string s) {
    vector<long long> v;
    for(int base = 2; base <= 10; base++) {
        long long cur = 0;
        for(int i = s.size() - 1; i >= 0; i--)
            cur += (s[i] == '1') * power(base, s.size() - 1 - i);
        
        long long res = isPrime(cur);
        if( res == cur ) return 0;
        
        v.push_back(res);
    }
    
    cout << s << " ";
    for(int i = 0; i < v.size(); i++)
        cout << v[i] << ((i == v.size() - 1) ? '\n' : ' ');
    return 1;
}

int check(int n) {
    string rep = "";
    for(int i = 15; i >= 0; i--) {
        rep += ((n & (1 << i)) ? "1" : "0");
    }
    if( rep[rep.size() - 1] != '1' ) return 0;
    return f(rep);
}


int main( void ) {
    cout << "Case #1:" << endl;
    int ans = 0;
    for(int i = (1 << 15); ans < 50 && i < (1 << 16); i++) {
        ans += check(i);
    }
}