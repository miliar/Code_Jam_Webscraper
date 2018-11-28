#include <iostream>
#include <cstdio>
using namespace std;
#define READ                  freopen("input.txt", "r", stdin);
#define WRITE                 freopen("output.txt", "w", stdout);
void calculate(int num, int t){
     int arr[10]={0},i=1;
     int n=num,val;
     if(num==0){cout<<"Case #"<<t<<": INSOMNIA"<<endl;return;}
     while(1){
          val = n;
          while(n!=0){
               int rem=n%10;
               arr[rem]=1;
               n=n/10;
         }
         int flag=1;
         //cout<<val<<endl;
         for(int j=0;j<=9;j++){
              // cout<<arr[j]<<endl;
          if(arr[j]==0){
               flag=0;
               break;
          }
         }
         if(flag==1){
               cout<<"Case #"<<t<<": "<<val<<endl;
               return;
         }
         i++;
         n = i*num;
     }
}

int main(){
    READ;
     WRITE;
    int t,num;
    cin>>t;
    for(int i=1; i<=t; i++){
     cin>>num;
     calculate(num,i);
    }
     return 0;
}
