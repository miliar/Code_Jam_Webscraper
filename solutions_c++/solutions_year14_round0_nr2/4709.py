#include<cstdio>
#include<iostream>
using namespace std;
double get_val(int i,double C,double F,double X) {
	double s=0;
	int j=0;
	for(j=0;j<i;j++) {
		//print C/(2+j*F) 
		s=s+C/(2+j*F);
	}
	return X/(2+(i)*F)+s;
}
int main() {
	int T,N,j,i;
	double C,F,X,f1,f2;
	scanf("%d",&T);
	for(i=0;i<T;i++) {
		scanf("%lf%lf%lf",&C,&F,&X);
		//print C,F,X
		j=0;
		f1=0;
		f2=0;
		while(1) {
			f2=get_val(j,C,F,X);
			if(j!=0)
				if(f2>f1)
					break;
				else
					f1=f2;
			else
				f1=f2;
			j=j+1;
		}
		printf("Case #%d: %.7f\n",i+1,f1);
	}
	return 0;
}
