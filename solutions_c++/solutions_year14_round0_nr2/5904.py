#include <iostream>
#include <set>
#include <stdio.h>
#include <stdlib.h>
 #include<math.h>

using namespace std;
const double initSpeed = 2.0;
int getTimes(double c, double f, double x)
{
    if(c >= x)
        return 0;
	double times = f * (x - c) / c - initSpeed;
	return ceil(times / f);

}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
  int cas;
  cin>>cas;

  for(int i = 1; i <= cas; i++)
  {
      double c, f, x;
	  cin>>c>>f>>x;
	  int times = getTimes(c, f, x);
	//  cout<<"time: "<<times<<endl;
	  double speed = initSpeed;
	  double ans = 0.0;
	  for(int j = 0; j < times; j++)
	  {
		  ans += c / speed;
		  speed += f;
	  }
	  ans += x / speed;
	  printf("Case #%d: %.7lf\n", i, ans);
  }
}
