#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;
double farm[100005];
int main()
{
	int cs,i=0,j;
	double c,f,x,r,t;

	cin>>cs;
	while(cs--){
		cin>>c>>f>>x;
		r = 2.0;
		t = 0.0;
		for(j=0;j<100005;j++) {
			farm[j] = t + x/r;
			t += c/r;
			r += f;
			if(j && farm[j]>farm[j-1]) break;
		}
		printf("Case #%d: %.7lf\n",++i,farm[j-1]);
	}
	return 0;
}
