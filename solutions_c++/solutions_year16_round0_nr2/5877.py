#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>

using namespace std;


int main(){

     int t;

     scanf("%d", &t);

     int teste=1;

     for(int i=0;i<t;i++){


         string sinais;
         cin>>sinais;
         int sin= 1;
         int resp=0;

         for(int i= sinais.size()-1;i>=0;i--){
            if(sin==1 and sinais[i]=='-'){
                sin=-1;
                resp++;
            }

            if(sin==-1 and sinais[i]=='+'){
                sin=1;
                resp++;
            }

         }
        printf("Case #%d: %d\n", teste, resp);
        teste++;
     }

    return 0;
}
