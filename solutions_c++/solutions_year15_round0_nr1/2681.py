#include <iostream>
#include <stdint.h>
using namespace std;
 
int main() {
int T,S,A,x;
 
char B[1001];
int t[1001];
int SC[1001];
 
 
ios_base::sync_with_stdio(false);
 
    cin >> T;
    for(int i = 0; i < T; i++) {
       cin >> S;
       cin >> B;
       x = 0;
       A = 0;
       for (int j=0; j<S+1; j++){
    t[j] = B[j] - '0';
    x=x+t[j];  
    SC[j]=x;      
    if(SC[j]<j+1) {A = A+j+1-SC[j];
        x=x+j+1-SC[j];
    }  
           
       }  
    cout << "Case #" << i+1 <<": " << A << "\n";      
           
       }
return 0;
}
