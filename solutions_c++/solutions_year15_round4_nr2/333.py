#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<string>
using namespace std;
int n;
double V,X;
double rate[200], temp[200];
void work()
{
  cin >> n >> V >> X;
  for(int i =0; i < n;i++)cin >> rate[i] >> temp[i];
  if(n==1){
    if(fabs(temp[0] - X) < 1e-10){
      printf("%.8lf\n", V/rate[0]);
    }
    else
      printf("IMPOSSIBLE\n");
  }
  if(n==2){
    if (max(temp[0],temp[1]) < X- 1e-10)
      printf("IMPOSSIBLE\n");
    else if(min(temp[0],temp[1]) > X+1e-10)
      printf("IMPOSSIBLE\n");
    else if (fabs(temp[0]-temp[1]) < 1e-10 && fabs(temp[0]-X) < 1e-10){
      printf("%.8lf\n", V/(rate[0]+rate[1]));
    }
    else {
      double t1 = (X*V- temp[1]*V)/(temp[0]-temp[1])/rate[0];
      double t2= (X*V-temp[0]*V)/(temp[1]-temp[0])/rate[1];
      printf("%.8lf\n", max(t1,t2));
    }
  }
}
int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <=T;i++){
    printf("Case #%d: ", i);
    work();
  }

}
