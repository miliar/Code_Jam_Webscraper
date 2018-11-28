#include<math.h>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
long t,T,a,b,rev,n,i,count=0,dig,num;
ifstream in("a.txt");
ofstream out("b.txt");
in>>T;
for(t=1;t<=T;t++)
{
    count=0;
in>>a>>b;
for(num=a;num<=b;num++)
{
    i=num;
     n = i;
 rev = 0;
 while (i > 0)
 {
      dig = i % 10;
      rev = rev * 10 + dig;
      i = i / 10;
 }
 i=n;
if (n==rev&&sqrt(n)*sqrt(n)==n)
{
n=sqrt(n);
cout<<n<<" ";
i=n;
rev = 0;
 while (i > 0)
 {
      dig = i % 10;
      rev = rev * 10 + dig;
      i = i / 10;
}
if (n==rev) count++;
}
}
out<<"Case #"<<t<<": "<<count<<"\n";
}

}
