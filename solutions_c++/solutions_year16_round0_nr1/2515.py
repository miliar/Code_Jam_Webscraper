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
long long int a,b,n,m ,ram[10000],k[10],sum,c,i,p,j,t,r,v,z;
   
long long     int  flag=0;
               
  cin>>t;
    v=0;
    while(t--){
        v=v+1;
      cin>>m;
        if(m!=0){   
       set < long long int> s1;
        j=0;
          i=1;
          while(s1.size()<10){
             
            c=p=i*m;
           i=i+1;
             
          while(c>0) {
         r = c%10;
          s1.insert(r);
                
          c/=10; 
                 }
              
             }
        cout<<"Case #"<<v<<": "<<p<<"\n";
        }
        if(m==0){
            cout<<"Case #"<<v<<": INSOMNIA\n";
        }
        
    }
    
    return 0;
    
}