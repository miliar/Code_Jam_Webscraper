#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int T;
    int N;
    int i,j,k,testN,nt;
    int a[10]={3,0,0,0,0,0,0,0,0,0};
    int nag[10]={0, 1, 2, 3, 4, 5, 6, 7, 8, 9};


     cin >> T;
     int p[T];

     if(T<1 || T>100){
        return 0;
     }

for(k=0;k<T;k++){
   cin >> p[k];
}


for(k=0;k<T;k++){

     N = p[k];



 if(N==0)
      {
          cout << "Case #1: INSOMNIA " << endl;

      }

 else {

    testN = N;
     i=1;

     while(a[0]!=nag[0]||a[1]!=nag[1]||a[2]!=nag[2]||a[3]!=nag[3]||a[4]!=nag[4]||a[5]!=nag[5]||a[6]!=nag[6]||a[7]!=nag[7]||a[8]!=nag[8]||a[9]!=nag[9]){

         N = testN*i;

         while(N){


             if(N%10 == 0){
               a[0]=0;
              }
             else if(N%10 == 1)
               {a[1]=1;}

             else if(N%10 == 2)
               {
                a[2]=2;
               }
             else if(N%10 == 3)
               {
                a[3]=3;
               }
             else if(N%10 == 4)
               {
                a[4]=4;
               }
             else if(N%10 == 5)
               {
                a[5]=5;
               }
             else if(N%10 == 6)
               {
                a[6]=6;
               }
             else if(N%10 == 7)
               {
                a[7]=7;
               }
             else if(N%10 == 8)
               {
                a[8]=8;
               }
             else if(N%10 == 9)
               {
                 a[9]=9;
               }


             if(N<=9){
               break;
               }

             N /= 10;


       }

     i=i+1;

}

a[0]=3,a[1]=0,a[2]=0,a[3]=0,a[4]=0,a[5]=0,a[6]=0,a[7]=0,a[8]=0,a[9]=0;

cout << "Case #"<<k+1<<": " << (i-1)*testN << endl;

 }

}


}
