#include<iostream>
using namespace std;
int check(int a[])
{ int i;
 for(i=0;i<=9;i++)
  if(a[i]==0)
  return 0;
return 1;
}

int main()
{ long long int j,t,p=0,n1,dig;
 cin>>t;
  for(j=1;j<=t;j++)
{ long long int n,i=0,flag=0; int a[10]={0};
   cin>>n; 
   if(n==0)
 { cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl; continue; }
 while(!flag)
 { i=i+1;
   n1=n*i; 
   while(n1)
   { dig=n1%10;
     a[dig]++;
     p=check(a); 
     if(p==1)
      { flag=1; break; }
    n1=n1/10;
   }
  if(flag==1)
  { cout<<"Case #"<<j<<": "<<n*i<<endl; continue; }

 }
}
}
 
    