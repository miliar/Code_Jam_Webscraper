#include <iostream>
#include <cmath>

using namespace std;

bool isPalin(unsigned long num){
    unsigned long  n = num;
    unsigned long rev = 0;
    while(num > 0){
        unsigned long dig = num % 10;
        rev = rev * 10 + dig;
        num /= 10;
    }
    return n==rev;
}

int main(void){

    int T;
    unsigned long A, B, from, to;

    cin >> T;

    for(int i=1;i<=T;i++){
        cin >> A >> B;
        int count = 0;
        from = (unsigned long )sqrt(A);
        to = (unsigned long )sqrt(B);
        if(from*from < A)from+=1;
        if(to*to > B)to-=1;
        //cout << from << " " << to << endl;
        for(unsigned long j=from; j<=to;j++){

            if(isPalin(j*j) && isPalin(j)){
                count++;
            }
        }
        cout << "Case #" << i << ": " << count << endl;
    }

    return 0;
}

