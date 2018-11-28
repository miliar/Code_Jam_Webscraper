#include <stdio.h>
#include<iostream>
using namespace std;

int main(void) {
	// your code goes here
	int t,jj;
	scanf("%d",&t);
	double c,f,x,g,cnt;
	for(jj=1;jj<=t;jj++){
			cnt=0;
			cin>>c>>f>>x;
			g=(double)2;
			double t1=0,t2,t=0;
			t1=c/g;
			t2=x/g;
				
				while(t1+(x/(g+f))<t2){
					cnt+=t1;
					g=g+f;
					t1= c/g;
					t2=x/g;
				}
				
			cnt+=(x/g);
			
			printf("Case #%d: %.7lf\n",jj,cnt);
	}
	return 0;
}
