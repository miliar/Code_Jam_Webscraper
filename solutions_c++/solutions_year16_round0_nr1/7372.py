#include <iostream>
using namespace std;

int main() {
    int t,v=1;
    cin>>t;
    while(t--)
    {
	int s1=0,s=0,n,k,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,y=0,o=1;
long num,n1;
cin>>num;
z:
  n=num*(o++);
  n1=n;
  while(n!=0)
  {
  k=n%10;
  n=n/10;
  if(k==0)
  {
  a++;
  }
  if(k==1)
  {
  b++;
  }
  if(k==2)
  {
  c++;
  }
  if(k==3)
  {
  d++;
  }
  if(k==4)
  {
  e++;
  }
  if(k==5)
  {
  f++;
  }
  if(k==6)
  {
  g++;
  }
  if(k==7)
  {
  h++;
  }
  if(k==8)
  {
  i++;
  }
  if(k==9)
  {
  j++;
  }
  }
  s1=s;
  s=a+b+c+d+e+f+g+h+i+j;
  if((a>0)&&(b>0)&&(c>0)&&(d>0)&&(e>0)&&(f>0)&&(g>0)&&(h>0)&&(i>0)&&(j>0))
  cout<<"Case #"<<v++<<": "<<n1<<endl;
  else if(s1==s)
  {
      y++;
      if(y>=5)
  cout<<"Case #"<<v++<<": "<<"INSOMNIA"<<endl;
  
      else if(y<5)
      goto z;
  }
      else
  goto z;
  
      }
  return 0;
}
