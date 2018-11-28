#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main()
{
  freopen("in.in","rate",stdin);
  freopen("out.out","w",stdout);
  
  int TC;
  cin>>TC;
  for(int test_case=1;test_case<=TC;test_case++){
	  double C,X,F;
	  cin>>C>>F>>X;
	  int z=1;
	  int y=z;
	  z=y;
	  if(z==1) z=2;
	  double time_till_now=0;
	  double current_cookies=0;
	  double rate=2.0000000;
	  
	  while(current_cookies<=X){
		  if(current_cookies>=X) break;
		  double time_with_purchase = (X-current_cookies+C)/(F+rate);
		  double time_without_purchase = (X-current_cookies)/rate;
		 
		  if (current_cookies<C){
			  current_cookies=min(X,C);
			  time_till_now+=min(X,C)/rate;
			 }
		  else if(time_without_purchase<=time_with_purchase){
			 time_till_now+=(X-current_cookies)/rate;
			 current_cookies+=X-current_cookies;
		  }
		  else{
			  current_cookies-=C;
			  rate+=F;
		  }
		}
	  printf("Case #%d: ",test_case);;
	  printf("%0.7lf\n",time_till_now);
	 }	
  return 0;
}
