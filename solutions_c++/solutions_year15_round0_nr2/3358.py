#include <stdio.h>
#include <iostream>
#include<algorithm>
using namespace std;
int main (){
int ans[2000];
int a[2000];
 int t;
   cin>>t;
  int n;
   for(int t1=1;t1<=t;t1++)
  {
     cin>>n;
    int an=0;
    for(int i=0;i<n;i++)
    {
      cin>>a[i];
      an=max(an,a[i]);
    }
   int an1=an;
        for(int i = 1 ; i <= an1 ; i++) {  
          int  su = i ;  
            for(int j = 0 ; j < n ; j++) {  
                if( a[j] > i ) {  
                    if( a[j]%i == 0 )  
                        su += (a[j]/i-1) ;  
                    else  
                        su += (a[j]/i) ;  
                }  
            }  
            an1 = min(an1,su) ;  
        } 
      cout<<"Case #"<<t1<<": "<<an1<<endl;
   }
 }
