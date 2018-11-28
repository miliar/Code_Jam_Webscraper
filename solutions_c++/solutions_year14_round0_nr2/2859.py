#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Bout.txt","w",stdout);
	int tcas,cas;
	while(~scanf("%d",&tcas)){
		for(cas=0;cas<tcas;cas++){
			double c,f,x,nowf,nowc;
			scanf("%lf%lf%lf",&c,&f,&x);
			nowf=2;
			if(x<=c){
				printf("Case #%d: %.7lf\n",cas+1,x/nowf);}
			else{
				nowc=0;
				nowf-=f;
				do{
					nowf+=f;
					nowc+=c/nowf;
				}while((x-c)/nowf>x/(nowf+f));
				nowc+=(x-c)/nowf;
				printf("Case #%d: %.7lf\n",cas+1,nowc);
			}
		}
	}
	return 0;
} 
/*
Input 
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762
*/