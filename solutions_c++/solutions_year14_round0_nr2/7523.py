#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int main(){
  int T;
  double c,f,x;
  cin >> T;
  for(int test=0;test<T;test++){
    cin >> c;
    cin >> f;
    cin >> x;
    double time =0;
    double rate = 2.;
    bool cont=1;
    while(cont==1){
      if(x/rate>c/rate+x/(rate+f)){
	time+=c/rate;
	rate+=f;
      }
      else{
	double time1 = time+x/rate;
	double time2 = 0;
	while(time+time2<time1){
	  time2+=c/rate;
	  rate+=f;
	  if(time+time2+x/rate<time1){
	    time1=time+time2+x/rate;
	  }
	}
	cont =0;
	printf("Case #%d: %.8lf",test+1,time1);
	cout << '\n';
      }
    }
  }
  return 0;
}
	
	  