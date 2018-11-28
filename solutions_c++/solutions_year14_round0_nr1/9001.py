#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
int T;
int n,m;
int a[4][4];
int b[4][4];
int i,j,k,p;
int count;
cin>>T;
for(i=0;i<T;i++){
   cin>>n;
   count=0;
   for(j=0;j<4;j++){
       for(k=0;k<4;k++){
           cin>>a[j][k];
       }
   }
   cin>>m;
   for(j=0;j<4;j++){
       for(k=0;k<4;k++){
           cin>>b[j][k];
       }
   }
   for(j=0;j<4;j++){
           for(k=0;k<4;k++){
       if(a[n-1][j]==b[m-1][k]){

               p=a[n-1][j];
           count++;

       }
   }
   }
   if(count==1){
     cout<<"Case #"<<i+1<<": "<< p <<endl;
   }
   if(count>1){
     cout<<"Case #"<<i+1<<": "<<" Bad magician!"<<endl;
   }
   if(count==0){
     cout<<"Case #"<<i+1<<": "<<" Volunteer cheated!"<<endl;
   }


}





}
