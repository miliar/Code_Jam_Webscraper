#include <iostream>

#define N_MAX 200

using namespace std;

bool reg[10];

void regist(long int N){
 while(N){
  reg[N%10] = true;
  N/=10;
 }
}

bool done(){
 short l =0;
 for(int i=0;i<10;i++){
  l+=reg[i];
 }
 return l==10;
}

void init(){
 for(int i=0;i<10;i++)
   reg[i] = 0; 
}

int main(){
 int T,t;
 long N,n;
 cin >> T;
 t = T;
 while(T--){
   cin >> N;
   n = N;
   init();
   if(N==0){
     cout << "Case #" << t-(T) << ": INSOMNIA" << endl;
   }else{
     while(!done()){
      regist(N);
      N+=n;
     }
     cout << "Case #" << t-T << ": " << N-n << endl;
   }
   
 }
 return 0;
}
