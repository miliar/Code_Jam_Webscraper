// Problem B. Cookie Clicker Alpha_big.cpp : 定义控制台应用程序的入口点。
//

#include<cstdio>
#include<cmath>
using namespace std;
int main(){
	int T;
	double sum ,b;
	double X,C,F;
	//freopen("B-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%lf %lf %lf",&C,&F,&X);
		double tmp = (double)(X-C)*F/C;
		b = 2;
		sum = 0;
		while(b<tmp){
			sum += C / b;
			b += F;
		}
		sum += X / b;
		printf("%.7lf\n",sum);
	}
	return 0;
}