#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int main()
{

    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


   int t;
   cin>>t;

   for(int i=1;i<=t;i++)
   {
       int count=0,flag=0,k=0;
      string s;
      cin>>s;




      while(true)
      {
         flag=0;
       for(int j=0;j<s.size()-1;j++)
       {

           if(s[j]!=s[j+1])
           {
               k=j;
               flag=1;
               count++;
               break;
           }


       }

       if(flag==1)
       {


       for(int j=0;j<=k;j++)
       {
           if(s[j]=='+')
            s[j]='-';
           else
            s[j]='+';

       }

       }


       if(flag==0 && s[0]=='-')
       {

           count++;
           break;

       }

       if(flag==0 && s[0]=='+')
       {
           break;

       }









      }




      cout<<"Case #"<<i<<": "<<count<<"\n";







   }














    return 0;
}
