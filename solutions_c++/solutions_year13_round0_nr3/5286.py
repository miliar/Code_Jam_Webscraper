#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>

#include <stdio.h>
using namespace std;

#define rep(i,m) for( i=0;i<m;i++)
#define rep2(i,x,m) for(i=x;i<m;i++)
#define T_Max  10000



int main ()
{
int i,T,num,A,B;
      
                 freopen("C-small-attempt0.in","rt",stdin);    
                 freopen("C-small-attempt0.out","wt",stdout);    
      
                 
				 cin>>T;    
    
    
//0, 1, 4, 9, 121, 484     
                  rep(i,T)    
                                                    
                  {    
cin>>A>>B;
num=0;
if(0>=A && 0<=B)num++;
if(1>=A && 1<=B)num++;
if(4>=A && 4<=B)num++;
if(9>=A && 9<=B)num++;
if(121>=A && 121<=B)num++;
if(484>=A && 484<=B)num++;

cout<<"Case #"<<i+1<<": "<<num<<endl;





				  }
    
       
  return 0;    
}    
    
    
    
