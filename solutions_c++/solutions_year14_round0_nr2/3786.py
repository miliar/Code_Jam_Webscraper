#include<cstdio>
using namespace std;

int main()
{
  int tcase;
  scanf("%d",&tcase);
  double c,f,x,time,rate,curr,prev,t;
  for(int l=1;l<tcase+1;l++){
    time=0.0;
    rate = 2.0;
    scanf("%lf %lf %lf",&c,&f,&x);
    prev = x/rate;
    while(1){
      t = c/rate;
      rate+=f;
      curr = x/rate;
      if(t+curr > prev){
	time+=prev;
	break;
      }
      else {
	time+=t;
	prev = curr;
      }
    }
    printf("Case #%d: %.7f\n",l,time);
  }
}
