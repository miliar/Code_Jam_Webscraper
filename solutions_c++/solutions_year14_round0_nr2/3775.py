#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int t,q;
	double c,f,x,p1,p2,p3,d,sum;
	freopen("B-large.in","r",stdin);
	freopen("jam2_out.txt","w",stdout);
	scanf("%d",&t);
	q=1;
	while(t--){
		scanf("%lf%lf%lf",&c,&f,&x);
		d=2.0;
		p1=x/d;
		p2=c/d;
		p3=x/(d+f);
		sum=0.0;
		while(p1>p2+p3){
			sum+=(p2);
			d=d+f;
			p1=x/d;
			p2=c/d;
			p3=x/(d+f);
		}
		sum+=p1;
		printf("Case #%d: %0.7lf\n",q++,sum);
	}
	return 0;
}
