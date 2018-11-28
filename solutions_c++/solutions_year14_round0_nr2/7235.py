//by jackyliuxx
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
using namespace std;

int main () {
	int t,k=1;
	scanf("%d",&t);
	while(t--){
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double ans=0,nc=2;
		while(1){
			if( X/nc > C/nc+X/(nc+F) ){
				ans+=C/nc;
				nc+=F;
			}
			else{
				ans+=X/nc;
				break;
			}
		}
		printf("Case #%d: %.7lf\n",k++,ans);
	}
}
