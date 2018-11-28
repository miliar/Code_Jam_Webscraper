#include <iostream>
#include <cmath>
#include <list>
#include <vector>

using namespace std;

bool esPali (int a);
int main(){
    unsigned int t, a, b, num, r1, li, ls, cont;
    float rc1;
    vector<int> cuad;
    cin>>t;
    for ( int i=1; i<=t; i++){
        
        num = 0; cont = 0;
        cin>>a>>b;
        r1 = sqrt(a); 
        rc1 = sqrt(a);
        
        if ( rc1 - r1 == 0)
           li = r1;   
        else li = r1+1;
        
        ls = sqrt(b); 
        num = ls-li +1;
        
        for (int j = li; j<=ls; j++){
            if ( esPali(j)){
                if ( esPali(j*j) ){ 
                   cont++;   
                   }
            }
        }
        cout<<"Case #"<<i<<": "<<cont<<endl;
    }
}

bool esPali (int a){
     bool b = false;
     
     unsigned int dig = (int) log10(a)+1;
     
     if ( dig == 1)
        b = true;
     else if ( dig == 2){
             if ( a/10 == a%10)
                b = true;
          }
     else if ( dig == 3){
          if ( a/100 == a%10)
             b = true;
     }         
         
     return b;
}

