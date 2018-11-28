#include<iostream>
#include<vector>
#include<map>
#include<list>
#include<cstdio>
#include<climits>
#include<algorithm>
#include<string>
#include<cmath>
#include<cstdlib>
#include<string.h>
using namespace std;

typedef long double ld;
typedef long long ll;

int main(){
	long double C,F,X,tym,rate;
	int t,x;
	scanf("%d",&t);
	for(x=1;x<=t;x++){
		printf("Case #%d: ",x);
		scanf("%llf%llf%llf",&C,&F,&X);
		//printf("%llf %llf %llf",C,F,X);
		tym=0.0;
		rate=2.0;
		while(X!=0.0){
			if(X/rate>(X/(rate+F))+(C/rate)){
				tym+=C/rate;
				rate=rate+F;
			}
			else{
				tym+=X/rate;
				X=0.0;
			}//cout<<tym<<endl;
		}
		printf("%.7llf\n",tym);
	}
	return 0;
}
