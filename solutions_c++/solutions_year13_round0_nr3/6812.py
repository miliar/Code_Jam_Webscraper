#include<iostream>
#include<math.h>
#include<conio.h>
#include<stdio.h>

using namespace std;

int main(){
        int t,n,i,j,r,k,count,caseno=0,l;
        cin>>t;
        l=t;
        int a[t],b[t],c[t];
        do{
               cin>>a[caseno]>>b[caseno];
               count=0;
         //      cout<<"\na="<<a<<"\tb="<<b<<"\tcount"<<count;
               for(i=a[caseno];i<=b[caseno];i++){
                                 n=i;
                            //     cout<<"\nn="<<n;
                                 r=0;
                                 while(n!=0){
                                             j=n%10;
                                             r=(r*10)+j;
                                             n=n/10;
                                         }
                          //               cout<<"\tr="<<r;
                                 if(i==r){
                                          k=sqrt(i);
                        //                  cout<<"\nk="<<k;
                                          r=0;
                                          while(k!=0){
                                             j=k%10;
                                             r=(r*10)+j;
                                             k=k/10;
                                             }
                      //                       cout<<"\tr="<<r;
                                          if(sqrt(i)==r){
                                              //     cout<<"\n"<<i<<"\n--> It is a fair and square palindrome !!"<<endl;
                                                   count++;
                                                   }
                                          }
                           //      cout<<"\ncount="<<count;
               c[caseno]=count;                  }
               t--;
               caseno++;
               }while(t>0);
               for(i=0;i<l;i++){
                                cout<<"Case #"<<i+1<<": "<<c[i]<<endl;
               
                                }
//getch();        
//system("PAUSE");
  
    }
