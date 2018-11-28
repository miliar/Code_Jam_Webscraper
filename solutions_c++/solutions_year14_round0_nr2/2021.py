#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

double c,f,x,res,make;

int main() {
	int test,z,i,j;
	
	int tmp;

	freopen("B-large.in","r",stdin);
	freopen("b_large.txt","w",stdout);
	scanf("%d",&test);
	for ( z=1; z<=test; z++ ) {
		make=2.0;
		scanf("%lf %lf %lf",&c,&f,&x);

		res=x/2.0;

		double local=res,times=0;
		while(res>=local) {
			times=times+(c/make);
			make=make+f;

			local=times+(x/make);

			if ( res < local ) break;
			else {
				res=local;
			}
		}

		printf("Case #%d: %.7lf\n",z,res);
	}
}