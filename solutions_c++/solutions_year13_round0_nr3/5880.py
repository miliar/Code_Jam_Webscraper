#include<iostream>
#include<math.h>
using namespace std;
bool isperfsq(int n)
{
     float p;
     int m;
p = sqrt(n) ;
m = p ;
if (p == m)
return true;
else
return false;
}
bool ispalindrome(int x) {
  if (x < 0) return false;
  int div = 1;
  while (x / div >= 10) {
    div *= 10;
  }        
  while (x != 0) {
    int l = x / div;
    int r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}
main()
{
      int i,a,b,k,c,t;
cin>>t;int j;
j=1;
while(j<=t)
{
cout<<"Case #"<<j<<": ";       
cin>>a>>b;
c=0;
for(i=a;i<=b;i++)
{
if(isperfsq(i))
{
k=sqrt(i);
if(ispalindrome(k) && ispalindrome(i))
c++;

}
}
cout<<c<<endl;
j++;
//system("pause");
}
}
