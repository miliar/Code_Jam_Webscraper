#include <math.h>
#include <iostream>
using namespace std;

int t,n,r1,n1,n2,n3,n4,r2;

int main () 
{
   cin>>t;
   for(int k=1;k<=t;k++){
       cin>>r1;
       int tab[4],tab2[4];
       int temp=1;
       while(temp<=4){
           cin>>n1;
           cin>>n2;
           cin>>n3;
           cin>>n4;
           if(temp==r1){
              tab[0]=n1;
              tab[1]=n2;
              tab[2]=n3;
              tab[3]=n4;
           }
           temp++;
       }
       cin>>r2;
       temp=1;
       while(temp<=4){
           cin>>n1;
           cin>>n2;
           cin>>n3;
           cin>>n4;
           if(temp==r2){
              tab2[0]=n1;
              tab2[1]=n2;
              tab2[2]=n3;
              tab2[3]=n4;
           }
           temp++;
       }
       int mem,counter=0;
       for(int i=0;i<=3;i++){
           for(int j=0;j<=3;j++){
               if(tab[i]==tab2[j]){
                   counter++;
                   mem=tab[i];
               }
           }
       }
       if(counter>1){
           cout<<"Case #" << k << ": Bad magician!"<<endl;
        }
        else if(counter==0){
            cout<<"Case #" << k << ": Volunteer cheated!"<<endl;
        }
        else if(counter==1){
            cout<<"Case #" << k << ": "<<mem<<endl;
        }
    }
    }