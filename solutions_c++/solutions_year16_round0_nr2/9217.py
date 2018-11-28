
#include<bits/stdc++.h>
using namespace std;
int main(void)
{
long long int i,n,z[100000],b,j,t,q=0,k=0,x=0;

cin>>t;
char s[1000000];
while(t--)
{x++;
cin>>s;
 p=0;
k=0;
n=strlen(s);
for(i=0;i<n;i++)
  {
  if(s[i]=='+')
     z[i]=1;
   else
      z[i]=0;
     }     
          i=n-1;k=0;
          while(i>=0)
             {//k=0;
             if(z[i]==0)
                {   k++;
                for(j=i;j>=0;j--)
                   {
                   if(z[j]==0)
                      z[j]=1;
                    else
                       z[j]=0;       
 
                   }
                }
             i--;
}
 
cout<<"Case #"<<x<<": "<<k<<"\n";  
}
 
return 0;
}