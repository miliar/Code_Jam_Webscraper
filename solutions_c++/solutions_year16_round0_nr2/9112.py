#include<bits/stdc++.h>
using namespace std;
int main()
{
long long int i,n,a[100000],b,j,t,ss=0,k=0,o=0;
char s[100000];
cin>>t;
while(t--)
{o++;
cin>>s;
 ss=0;
k=0;
n=strlen(s);
for(i=0;i<n;i++)
  {
  if(s[i]=='+')
     a[i]=1;
   else
      a[i]=0;
     }     
          i=n-1;k=0;
          while(i>=0)
             {//k=0;
             if(a[i]==0)
                {   k++;
                for(j=i;j>=0;j--)
                   {
                   if(a[j]==0)
                      a[j]=1;
                    else
                       a[j]=0;       
                        
                   }
                }
             i--;
}
     
cout<<"Case #"<<o<<": "<<k<<"\n";  
}
 
return 0;
}