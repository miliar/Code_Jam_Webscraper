//In the name of GOd

#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
    {
      double a,b,c;
      cin>>a>>b>>c;
      double s=2,time=0;
      //1:50>40   2:25>24.1666666667
      int y=0;
      while(c/s>a/s+c/(s+b))
	{
	  //	  cerr<<"s:"<<s<<endl;
	  time+=a/s;
	  s+=b;
	}
      time+=c/s;
      printf("Case #%d: ",i);
      printf("%.8lf\n",time);
    }
  return 0;
}
