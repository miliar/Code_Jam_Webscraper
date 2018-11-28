#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int T, N, J, nCase;
ll pows[11][16];
ll ac[11];

ll mulmod(ll a, ll b, ll mod){

    ll x = 0,y = a % mod;

    while (b > 0){
        if (b % 2 == 1)
            x = (x + y) % mod;

        y = (y * 2) % mod;
        b /= 2;
    }
    return x % mod;
}

ll modulo(ll base, ll exponent, ll mod){
    
    ll x = 1;
    ll y = base;

    while (exponent > 0){
        if (exponent % 2 == 1) x = (x * y) % mod;

        y = (y * y) % mod;
        exponent = exponent / 2;
    }
    return x % mod;
}

bool Miller(ll p,int iteration){

    if (p < 2)
        return false;

    if (p != 2 && p % 2==0)
        return false;

    ll s = p - 1;

    while (s % 2 == 0)
        s /= 2;

    for (int i = 0; i < iteration; i++){

        ll a = rand() % (p - 1) + 1, temp = s;
        ll mod = modulo(a, temp, p);

        while (temp != p - 1 && mod != 1 && mod != p - 1){
            mod = mulmod(mod, mod, p);
            temp *= 2;
        }

        if (mod != p - 1 && temp % 2 == 0)
            return false;
    }

    return true;

}

bool isPrime( ll num ){
    if( num <= 2 ) return true;
    if( num % 2 == 0 ) return false;
    for( ll i = 3; i < 1000; i += 2LL )
        if( num % i == 0 ) return false;
    return true;
}

bool check(){
    //cout << "inicio check" << endl;
    for( int i = 2; i < 11; i++ ){
        if( isPrime(ac[i]) ) return false;
    }
    //cout << "fin check" << endl;
    return true;
}

ll getDivisor( int i ){
    //cout << "\ndivisor de " << ac[i] << endl;
    //cout << "inicio divisor" << endl;
    if( ac[i] % 2 == 0 ){/*cout << "\n" << ac[i] << " div por " << 2 << endl; */return 2LL;}
    for( ll k = 3 ; ; k += 2LL )
        if( ac[i] % k == 0 ){/*cout << "\n" << ac[i] << " div por " << k << endl; */return k;}
    return -1;
}

void printJam( string &num ){
    //cout << "inicio print" << endl;
    cout << num << "1";
    for( int i = 2; i < 11; i++ ){
        //cout << "antes divisor" << endl;
        cout << " " << getDivisor(i);
        //cout << "despues divisor" << endl;
    }
    cout << endl;
    //cout << "fin print" << endl;
}

void solve( int i, string &num ){

    //cout << i << " " << num << endl;
    if( i == 0 ){
        if( check() ){
            J--;
            printJam( num );
        }
        return;
    }

    num.push_back('0');
    //cout << "i: " << i << endl;
    //cout << "num: " << num << endl;
    solve( i-1, num );
    if( !J ) return;

    for( int k = 2; k < 11; k++ ){
        ac[k] += pows[k][i];
    }

    num[ num.length() - 1 ] = '1';

    //cout << "i: " << i << endl;
    //cout << "num: " << num << endl;
    solve( i-1, num );
    if( !J ) return;
    num = num.substr(0, num.length()-1);
    for( int k = 2; k < 11; k++ ){
        ac[k] -= pows[k][i];
    }
}

int main(){

    for( int i = 2; i < 11; i++ ) pows[i][0] = 1LL;
    for( ll i = 2; i < 11L; i++ )
        for( int j = 1; j < 16; j++  )
            pows[i][j] = pows[i][j-1] * i;

    /*for( int i = 0; i < 11; i++ ){
        for( int j = 0; j < 16; j++  ){
            cout << pows[i][j] << " ";
        }
        cout << endl;
    }*/


    cin >> T;

    while( T-- ){
        cin >> N >> J;
        cout << "Case #" << ++nCase << ":\n";
        for( int i = 2; i < 11; i++ ) ac[i] = 1LL + pows[i][N-1];
        string num = "1";
        solve(N-2, num);
    }
    /*int iteration = 5;
    ll num;

    cout<<"Enter integer to test primality: ";
    cin>>num;

    if (Miller(num, iteration))
        cout<<num<<" is prime"<<endl;

    else
        cout<<num<<" is not prime"<<endl;

    return 0;*/
}