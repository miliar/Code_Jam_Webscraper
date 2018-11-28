#include <iostream>
#include <conio.h>
#include <fstream>
#include <cmath>

using namespace std;
int a[100];
int lenght(int n){
    int c = 0;
    while (n>0){
        n = n /10;
        c++;
    }
    return c;
}

bool isPaladin(int n){
    int len = lenght(n);
    int n1 = n;
    for(int i = 0; i < len; i++){
        a[len - i -1] = n1%10;
        n1 = n1/10;
    }
    for(int i = 0; i < len/2; i++){
        if(a[i] != a[len - 1 - i])
            return false;
    }
    return true;
}


int T, A , B;

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    for(int ti = 0; ti < T; ti++){
        cin >> A >> B;
        int a = ceil(sqrt(A));
        int b = sqrt(B);
        //cout << a << " " << b << endl;
        int c = 0;
        for(int i = a; i <=b; i++){
            if(isPaladin(i) && isPaladin(i*i)){
                c++;
            }
        }
        cout  <<"Case #"<< ti+1 << ": " << c << endl;
    }
    return 0;
}
