
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>

#define FOR(a,b,c) for(int (a)=(b);(a)<=(c);(a)++)
#define FORT(a,b,c) for(int (a)=(b);(a)>=(c);(a)--)

using namespace std;

typedef long long Lint;

const Lint mod = 1e9;


int main(){
	
	int TEST;
	
	double Cookie,F,X;
	
	scanf(" %d",&TEST);
	
	FOR(test,1,TEST){
		
		scanf("%lf %lf %lf",&Cookie,&F,&X);
		
		double res=1e9;
		
		double cur=0;
		double f=2;
		
		int x=X;
		
		res=min(res,cur+X/f);
		
		FOR(i,1,x){
			cur+=Cookie/f;
			f+=F;
			res=min(res,cur+X/f);
		}
		
		printf("Case #%d: %.7lf\n",test,res);
		
	}
	
	return 0;
	
}
