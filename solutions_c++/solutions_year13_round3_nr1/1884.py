#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>

using namespace std;

int main()
{
   int t,flag,last,k,m,i,j,n,sum;
   string s;
   cin>>t;
   
   for(k=1;k<=t;k++)
   {
      cin>>s;
      cin>>n;
      sum = 0;
      last = -1;
      for(i=0;i<s.length()-n+1;i++)
      {
         flag = 0;
         
         for(j=0;j<n;j++)
         if(s[i+j]=='a'||s[i+j]=='e'||s[i+j]=='i'||s[i+j]=='o'||s[i+j]=='u')
         {
            flag = 1;
            break;
         }
         
         if(flag==0)
         {
            if(last == -1)
            m = i;
            
            else
            {
               m = i - last - 1;
            }
            
            last = i;
            sum+=(m+1)*(s.length()-i-n+1);
         }
      }
      
      cout<<"Case #"<<k<<": "<<sum<<"\n";
   }
   

}
