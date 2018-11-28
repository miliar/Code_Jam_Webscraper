#include <iostream>
using namespace std;
#include<cstdio>
int main() {
	int t;
	scanf("%d",&t);
	int n=t;
	while(t--)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double* p=new double[100000];
		int d=0;
		p[0]=x/2;
		d++;
		bool check=true;
		while(check)
		{
			double temp=p[d-1]-(x/((d-1)*f+2));
			p[d]=temp+(c/(f*(d-1)+2))+x/(d*f+2);
			if(p[d]>p[d-1]){
			check=false;}
			else d++;

		}
		printf("Case #%d: %.7lf\n",n-t,p[d-1]);
	}
	return 0;
}
