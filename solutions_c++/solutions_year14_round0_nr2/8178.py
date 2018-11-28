#include <iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main() {
double c,f,x,r,time;
int t;
scanf("%d",&t);
int s=1;
while(t--){
	scanf("%lf%lf%lf",&c,&f,&x);
	time=0;
	r=2;
	
	while((x/r) > ((c/r)+ (x/(r+f)))){
		time+= c/r;
		r+=f;
		}
	time+= x/r;
	printf("Case #%d: %.10lf\n", s,time);
	s++;
	}
}