// GJ 2014 B
// cookie clicker

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;


int N;
int cases;
double C,F,X;
double speed=2;	// speed
double buy, save;
double elapsed;


int main(){

	freopen("B-small-attempt00.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	cin >> N;
	cases=0;
	cin.ignore();
	while(N--){
		cases++;
		speed=2;
		elapsed=0;
		// input
		scanf("%lf %lf %lf",&C,&F,&X);

		while(1){
			buy = C/speed+(X/(speed+F));
			save = X/speed;
			//printf("%lf,%lf\n",buy,save);
			if(buy<save){
				elapsed+=C/speed;
				speed+=F;
			}else{
				elapsed+=X/speed;
				break;
			}
		}
		printf("Case #%d: %.7f\n",cases,elapsed);
	}


return 0;
}