#include <iostream>
#include <stdio.h>
using namespace std;
bool DIG[10];
bool Checkall();
void Clearall();
bool Checkall(){
        for(int i=0 ;i<10;i++){
            if(DIG[i] == false){
                return false;
            }
        }
        return true;
    }
void Clearall(){
	for(int i = 0; i<10;i++){
		DIG[i] = false;
	}
}
int main() {
	int T;
    cin>>T;
    int B = T;
    int X,C,number,Y = 0,i = 0;
    while(T--){
          cin>>X;
          i = 0;
          Y = 0;
          //printf("\n%d with X = %d\n",(B-T),X);
          if(X > 0){
              while(Checkall() == false){
                 i++;
                 Y = i*X;
                 number = Y;
                 while (number > 0) {
                   DIG[number % 10] = true;
                   number = number / 10;
                 }

              }
              printf("\nCase #%d: %d",(B-T),Y);
              Clearall();
         }
        else{
           printf("\nCase #%d: INSOMNIA",(B-T));
        }
      
       }
		return 0;
}
