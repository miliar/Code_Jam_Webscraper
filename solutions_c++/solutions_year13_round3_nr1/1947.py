/*Prashant Agrawal */
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <cstring>
#include <vector>
#include <map>
using namespace std;
int n;
bool checkvowel(char ch)
{
     if((ch=='a')||(ch=='e')||(ch=='i')||(ch=='o')||(ch=='u'))
     return true;
     else
     return false;
}
 
bool query(vector<char> &v)
{
     int i,j,k,c=0;
     for(i=0;i<v.size();i++)
     {
        c=k=0;
        for(j=i;(j<v.size())&&(k<n);j++,k++)
        
           if(!checkvowel(v[j]))
           c++;
           
           
        
        if(c==n)
        return true;
     }
     return false;
}
     
 
 
int main()
{
   
   char a[200];
   int x,k,len,c,t,ans,i,j;
   scanf("%d",&x);
   for(t=1;t<=x;t++)
   {
      scanf("%s",a);
      scanf("%d",&n);
      len=strlen(a);
      ans=0;
      for(i=0;i<len;i++)
      {
         vector<char> v;
         for( j=i;j<len;j++)
         {
            v.push_back(a[j]);
            if(query(v))
            ans++;
            
            
         }
      }
      printf("Case #%d: %d\n",t,ans);
   }
   return 0;
}
