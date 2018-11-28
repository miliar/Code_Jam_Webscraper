#include <iostream>
#include <cstdio>

using namespace std;

double init  = 2.0;
double c,f,x;

double with(int time)
{
  double t=0.0;
  for(int i=0;i<time;i++)
    {
      t+=(c/init);
      init+=f;
    }
  t+=x/init;
  return t;
}


int main()
{
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
    {
      cin>>c>>f>>x;
      double time = 2000.0;
      for(int j=0;j<2000;j++)
	{
	  init = 2.0;
	  double tmp=with(j);
	  if(tmp<time)
	    time = tmp;
	}
      cout<<"Case #"<<i<<": ";
      printf("%.7lf\n",time);
    }
  return 0;
}
