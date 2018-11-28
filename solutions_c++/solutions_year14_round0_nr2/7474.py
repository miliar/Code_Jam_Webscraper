//============================================================================
// Name        : testGCJ1.cpp
// Author      : Takatera Toshiki
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
using namespace std;
int kaisu;
double F,C,X,cookie=2.0,ans;
int main(){
	scanf("%d",&kaisu);
	for(int i=1;i<=kaisu;i++){
		ans=0.0;
		cookie=2.0;
		scanf("%lf %lf %lf",&C,&F,&X);
		while(1){
			double a=X/cookie,b=X/(cookie+F)+C/cookie,c=C/cookie;
			if(a<=b){
				ans+=a;
				break;
			}else{
				ans+=c;
				cookie+=F;
			}
		}
		printf("\nCase #%d: ",i);
		printf("%.7lf",ans);

	}
	return 0;
}
