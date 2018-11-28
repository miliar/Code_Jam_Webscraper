#include<iostream>
#include <cmath>

using namespace std;

int main(){
  
int t;
int A=0,p=0, odp=0,k=0,n=0,s=0;
static int T[10];
static int S[1200001];
static int L[4];
    
  cin >> t;
  for(int i=0; i<t; i++){
  

      cin >> A;
   if(A==0){cout << "Case #" << i+1 << ": " << "INSOMNIA"<< '\n' ;}
   else{
      k=0;p=0; odp=0; n=0; s=0;
      while(A!=0){ //wykreslamy cyfry, ktore wystepuja we wczytanej liczbie
          p=A%10;
          T[p]=1; 
          S[k]=p;
          L[k]=S[k];
          A=A/10; 
          k++;   
      }
      odp=0;
      s=k;
      for(int j=0; j<10; j++){ //sprawdza czy byly juz wszystkie cyfry
          if(T[j]!=1){break;}
          if(j==9 and T[j]==1){odp=1;}
          }
          
      while(odp==0 and S[1199999]==0){
          for(int j=0; j<s; j++){
              S[j]+=L[j];
              
              if(S[j]>9){S[j+1]=S[j+1]+S[j]/10; S[j]=S[j]-(S[j]/10)*10; if(j==s-1) {s++;}}
              
              n=S[j];
              T[n]=1;
          
          }    
              for(int j=0; j<10; j++){ //sprawdza czy byly juz wszystkie cyfry
                    if(T[j]!=1){break;}
                     // cout << T[j] << ' ';
                    if(j==9 and T[j]==1){odp=1;}
                 }
              
           }   
      cout << "Case #" << i+1 << ": " ;
      if(odp==1){
          for(int j=s-1; j>=0; j--){
              cout << S[j] ;
          }
          cout << '\n';
      }
      
      for(int m=0; m<s; m++){
          S[m]=0;}
      for(int m=0; m<10; m++){T[m]=0;}
      for(int m=0; m<4; m++){L[m]=0;}
      
  }}
    
return 0;}


