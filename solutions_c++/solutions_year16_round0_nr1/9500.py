#include <iostream>

using namespace std;

bool actualizar(bool dig[], long long n) {
    for (;n>0;n/=10) {
        dig[n%10]=1;
    } 
    for (int i=0; i<10; i++) {
        if (!dig[i]) return false;
    } return true;
}

void caso(int c){
    bool dig[10]; for (int i=0; i<10; i++) dig[i]=0;
    long long n=0, n0;
    cin >> n0;
    if (!n0) {
            cout << "Case #" << c << ": INSOMNIA" << endl;
        return;
    }
    for (int j=0;true;j++) {
        n+=n0;
        if (actualizar(dig, n)) {
            cout << "Case #" << c << ": " << n << endl;
            return;
        }
    }
}

int main(){
    int t;
    cin >> t;
    for (int i=0; i<t; i++) caso(i+1);
}     
