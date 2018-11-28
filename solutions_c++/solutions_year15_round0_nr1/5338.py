#include<iostream>
#include<stdio.h>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<fstream>
#include<set>
 
using namespace std;
typedef long long int ll;
 
 
int main()
{
     freopen("0in.txt", "r", stdin);
    freopen("0out.txt", "w", stdout);
 
    ll tt2,t,i,s;
    int arr1[2000],res1,st1;
   
   cin>>tt2;
   for(t=1;t<=tt2;t++)
   {
         
           cin>>s;
           for(i=0;i<=s;i++)
           {
               scanf("%1d",&arr1[i]);  
           }
           
           //cout<<endl;
           res1 = 0;
           st1= 0;
           for(i=0;i<=s;i++)
           {
                   if(i==0)
                   {
                      st1 += arr1[i];
                   }
                   else
                   {
                            if(st1>=i)
                            {
                               st1 += arr1[i]; 
                                }
                                else
                                {
                                         res1 += i - st1;
                                         st1 += (i-st1) + arr1[i];
                                }
                   }
           }
           
           printf("Case #%d: %d\n",t,res1);
   }
     
 return 0;
}
