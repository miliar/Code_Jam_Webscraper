#include <iostream>
using namespace std;

int main() {
 long n,perm,p,k,digit,test,i;
 bool a[10],flag=0;
 
  cin>>test;
  for(i=1;i<=test;i++)
  {
   cin>>n;
   if(n==0)
    cout<< "Case #"<<i<<": "<<"INSOMNIA"<<endl;
   else
   {
     flag=0;p=1;
   for(int j=0;j<=9;j++)
      a[j]=0;
 while(true)
 {
  perm=n*p;
  k=perm;
  while(k)
  {
   digit=k%10;
   a[digit]=1;
   k=k/10;
   }
   if(a[1]&a[2]&a[3]&a[4]&a[5]&a[6]&a[7]&a[8]&a[9]&a[0])
     { flag=1; break;}
      p=p+1;
   }
   if(flag) 
    cout<<"Case #"<<i<<": "<<perm<<endl;
 }
 }
	return 0;
}