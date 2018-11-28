#include<stdio.h>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>

using namespace std;

int main(){
	int t,n;
	double c,f,x,tt,rt,vt,minl,cs,tmp;
	cin >> t;
	n=t;
	while(t--){
		cin >> c >> f >> x;
		tt=vt=cs=tmp=(double)0;
		rt=(double)2;
		minl=(double)100006;

		cs=x/rt;

		while(cs <= minl){
			minl=cs;
			cs=tmp;
			cs+=(c/rt);
			rt+=f;
			tmp=cs;
			vt+=c;
			cs+=(x/rt);
		}

		printf("Case #%d: %.7f\n",n-t,minl);
	}
	return 0;
}




