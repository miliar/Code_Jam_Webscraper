#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <iostream>

using namespace std;
int S[10];
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("b.out.txt","w",stdout);
	
	int T,cas;
	scanf("%d",&T);
	for(cas = 1; cas <= T; cas++){
		double c,f,x,ans,now = 0.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		double k = 2.0;
		ans = x / k;
		while(true){
			now += (c / k);
			k += f;
			if(x / k + now >= ans){
				break;
			}
			ans = x / k + now;
		}
		printf("Case #%d: %.7lf\n",cas,ans);
		
	}
	return 0;
}