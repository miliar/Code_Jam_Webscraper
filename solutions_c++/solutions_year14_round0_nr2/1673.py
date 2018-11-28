#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#define ll long long

using namespace std;

int main()
{
  int T;
  cin >> T;
  int tc = 1;
  while(T--){
    double C, F, X;
    //cin >> C >> F >> X;
    scanf("%lf %lf %lf",&C,&F,&X);
    double time=0;
    if(C >= X){
      time += X/2;
    }
    else{
        ll farms;
	double tmp = X/C - 2/F - 1;
	farms = ceil(tmp);
	if(farms < 0)
	  farms = 0;
	for(ll i = 0; i < farms; ++i){
	  time += C/(i*F + 2);
	}
	time += X/(farms*F + 2);
    }
    //cout << "Case #" << tc++ << ": " << time << endl;
    printf("Case #%d: %0.7lf\n",tc++,time);
  }
  return 0;
}
