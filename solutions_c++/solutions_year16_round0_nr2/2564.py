#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<cstring>
#include<stdlib.h>
#include <bits/stdc++.h>
 
using namespace std;
  
int main() {
long long int a,b,n,m ,sum,c,i,p,j,t,r,v,z,k;
   char C[101];
long long     int  flag=0;
               
  cin>>t;
    p=0;
    while(t--){
        p=p+1;
      cin>>C;
        k=strlen(C);
        flag=0;
        c=0;
        for(i=k-1;i>=0;i--){
            if(C[i]=='-'){
                flag=1;
                c=c+1;
                while(C[i-1]=='-'){
                    i=i-1;
                }
                
            }
            if(flag==1 && C[i]=='+'){
                c=c+1;
                while(C[i-1]=='+'){
                    i=i-1;
                }
            }
        }
        cout<<"Case #"<<p<<": "<<c<<"\n";
            
       
    }
    
    return 0;
    
}