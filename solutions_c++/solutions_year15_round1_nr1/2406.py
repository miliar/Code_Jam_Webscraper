#include <iostream>
#include <stdint.h>
using namespace std;
 
int main() {
int T,N;
 int A=0;
 int C=0;
 int X=0;
 int D=0;
int B[1001];

 
 
ios_base::sync_with_stdio(false);
 
    cin >> T;
    for(int i = 0; i < T; i++) {
       cin >> N;
       A=0;
       C=0;
       D=0;
    for (int s=0; s<1001; s++){
    B[s]=0;}
       for (int j=0; j<N; j++){
      
    cin >> B[j]; 
       }
       if (B[1]<B[2]){C=B[1]-B[2];}
       else {C=0;}
        for(int k=0;k<N-1 ;k++){
        X=B[k]-B[k+1];
        if(B[k]>=B[k+1]){
        A=A+B[k]-B[k+1];
        
        if (C<X){C=X;}
        }
        
       
       }

    cout << "Case #" << i+1 <<": " << A << ' ' ; 
      for(int k=0;k<N-1 ;k++){
      if (B[k]>=C){
        D=D+C;        
        }
        if(B[k]<C){D=D+B[k];}
        
        }
        cout << D <<"\n";
       }
return 0;
}
