#include <bits/stdc++.h>
using namespace std;

int main()
{
   int t,j=1;
   cin>>t;
   while(t--)
   {

       string str,cstr;
       cin>>str;
       int len=str.size();
       int k=0;
       cstr=str[0];

     for(int i=1;i<len;i++)
       {
          if(cstr[k]<= str[i])
           cstr=str[i]+cstr;
           else
            cstr=cstr+str[i];


       } cout<<"Case #"<<j<<": "<<cstr<<endl;

j++;

   }
    return 0;
}
