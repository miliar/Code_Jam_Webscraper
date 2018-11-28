#include<bits/stdc++.h>
using namespace std;
int main()
{
   int t,T, i, j;
   cin>>T;
   for(t=1; t<=T; t++)
   {
       int count=0;
       char S[1000];
       cin>>S;
       int n=strlen(S);
       
       if(n==1 && S[i]=='-')
       count=1;
       
       else if(n==1 && S[i]=='+')
       count=0;
       
       else{
       for(j=1; j<n; j++)
       {
           if(S[j-1]!=S[j])
           {
               for(i=0; i<j; i++)
               S[i]=S[j];
               count++;
           }
       }
       if(S[j-1]=='-')
       count++;
       }
       cout<<"Case #"<<t<<": "<<count<<endl;
    }
 return 0;
}
           
              
         
