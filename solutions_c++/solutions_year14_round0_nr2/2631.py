#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <ctime>
#include <cmath>
#include <algorithm>
using namespace std;
double C,F,X,get,tt;
int T;
int main(){
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&T);
	for (int test=1;test<=T;test++){
		printf("Case #%d: ",test);
		scanf("%lf%lf%lf",&C,&F,&X);
		get=2;tt=0;
		while (true){
			double t1=X/get;
			double t2=C/get+X/(get+F);
			if (t1<t2){
				tt+=X/get;
				break;
			}else{
				tt+=C/get;
				get+=F;
			}
		}
		printf("%.7lf\n",tt);
	}
}
