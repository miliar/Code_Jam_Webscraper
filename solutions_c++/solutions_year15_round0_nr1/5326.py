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
typedef unsigned long long ull;
 
int main()
{
     freopen("0in.txt", "r", stdin);
     freopen("0out.txt", "w", stdout);
 
    ll tt,t,i,s;
    int arr[2000],res,st;
   scanf("%d",&tt);
   for(t=1;t<=tt;t++)
   {
           scanf("%d",&s);
           for(i=0;i<=s;i++)
           {
               scanf("%1d",&arr[i]);    
           }
           
           //cout<<endl;
           res = 0;
           st= 0;
           for(i=0;i<=s;i++)
           {
                   if(i==0)
                   {
                      st += arr[i];
                   }
                   else
                   {
                            if(st>=i)
                            {
                               st += arr[i];   
                                }
                                else
                                {
                                         res += i - st;
                                         st += (i-st) + arr[i];
                                }
                   }
           }
           
           printf("Case #%d: %d\n",t,res);
   }
     
 return 0;
}
