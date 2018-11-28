#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
long long int l0,lo,hi,x,z,y,a,b;
int c,t,zz;
int main()
{
  freopen("csmall.in","r",stdin);
  freopen("pan.out","w",stdout);
  cin>>t;
  for(zz=1;zz<=t;zz++)
  {
    cin>>lo>>hi;
    c=0;
    for(l0=sqrt(lo);l0<=sqrt(hi);l0++)
    {
      a=l0;
      b=0;
      while(a>0)
      {
        b=b*10+a%10;
        a/=10;
      }
      if(l0==b)
      {
        x=l0*l0;
        if(x>=lo&&x<=hi)
        {
          y=0;
          z=x;
          while(z>0)
          {
            y=y*10+z%10;
            z/=10;
          }
          if(x==y)
          {
            c++;
            //cout<<x<<endl;
          }
        }
      }
    }
    cout<<"Case #"<<zz<<": "<<c<<endl;
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
