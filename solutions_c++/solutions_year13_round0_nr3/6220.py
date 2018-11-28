#include <cstdio>
#include <iostream>
#include <cmath>


using namespace std;

bool pal(int n){
    if(n>100){
        if (n/100==n%10)
            return true;
    }
    if(n>10 and n<100){
        if(n/10 == n%10)
            return true;
    }
    if(n<10)
        return true;
    return false; 
}


int cuadrado(int n){
    int i=1;
    while(true){
        if(i*i >= n)
            return i;
    i++;
    }
    return 0;
}


int main(){
   //freopen("cin.in","r",stdin);
   int v[33];
   for(int i=1; i<33; i++){
     v[i]=i*i;
   }
   int T,A,B;
   cin >> T;
   int test=1;
   while(test<=T){
     cin >> A>>B;
     //cin >> B;
     int n = cuadrado(A);
     //printf("n: %d\n",n);
     int vals=0;
     while(n*n <= B){
        if( pal(n) and pal(n*n) ){
            //printf("val: %d\n",n);
            vals++;
        }
        n++;
     }
     
     printf("Case #%d: %d\n",test,vals);
     test++;
   }
      
   
    
}
