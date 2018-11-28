#include<stdio.h>
#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
#define ll long long int
using namespace std;
//char A[16];
long long int number,size,iter;
long long int base[9];

ll isPrime(ll num){

for(ll i =2;i<=(ll)sqrt(num);i++){
if(num%i==0){
 return i;
}

}
return -1;

}


ll base2(char A[],ll b, ll s){
 ll n=0,c=1,te;
//cout<<endl;
//cout<<"W: "<<endl;
 for(ll i=s-1;i>=0;i--){
  // cout<<A[i];
   if(A[i]=='1'){
    te=1;
    }else{
     te=0;  
   }
   n += te*c;
   c=c*b;
 }
//cout<<endl;
 return n;
}

void binary(char A[], ll n)
{//  static int rank;
    if(iter==0){
      return;
      }
    if(n < 1){
         for(ll i=0;i<9;i++){
          base[i]=0;
         }       
        if(A[0]=='1' && A[size-1]=='1'){
          // cout<<"inside Binary: "; 
         // printf("%s\n",A);
         ll check =0; 

          for(ll i=2;i<=10;i++){
              base[i-2] = base2(A,i,size); 
               ll temp=isPrime(base[i-2]);
              if(temp==-1){
               check=1;
                   
              }else{
                base[i-2] = temp;
              }
           // cout<<"Base:"<<i<<" "<<base[i-2]<<endl;        
          }
        if(check==0 && iter){
        iter--;
         A[size]='\0';
          //rank++;
        // cout<<"Case #"<<rank<<":"<<endl;
          cout<<A<<" ";
          for(ll i=2;i<=10;i++){
            cout<<base[i-2]<<" ";
          }
          cout<<endl;
        
        
       }
      }
   //  number++;
    }   
    else
    {
        A[n-1] = '0';
        binary(A,n-1);
        A[n-1] = '1';
     
        binary(A,n-1);
    }
}

int main(void)
{    
      static long long int rank; 
       ll t;
       cin>>t;
      while(t--){

         iter=0;
        ll n,j;
        cin>>n>>j;
         iter =j;
       char A[n];
        number=0;
        size = n;
       rank++;
       cout<<"Case #"<<rank<<":"<<endl;
	binary(A,n);
        }

	return 0;
}
