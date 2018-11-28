#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <memory.h>
#include <time.h>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <vector>
#define N 111111
#define LL long long


using namespace std;

int T;

int main(){        
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T;
	for (int test=1;test<=T;test++){
		double speed=2.0,c,f,x;
		cin >> c >> f >> x;
		double ans=(x/speed),time=0;
		while (time+(c/speed)+(x/(speed+f))<ans){
			ans=time+(c/speed)+(x/(speed+f));
			time+=(c/speed);
			speed+=f;
		}
		printf("Case #%d: %.15lf\n",test,ans);
	}

	return 0;
}