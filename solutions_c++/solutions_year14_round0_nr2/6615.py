#include <iostream>
#include <cstdio>

using namespace std;

int main(){
  int N;
  cin >> N;

  for(int i=1;i<=N;++i){
	double cost, farm, goal;
	cin >> cost >> farm >> goal;

	double ret = goal / 2.0;
	for(int n=1;;++n){
	  double time = 0;
	  for(int j=0;j<=n-1;++j){
		time += cost / (2.0 + j * farm);
	  }
	  time += goal / (2.0 + n * farm);

	  if(ret < time){
		break;
	  }else{
		ret = time;
	  }
	}

	printf("Case #%d: %.7lf\n", i, ret);
  }

  return 0;
}
