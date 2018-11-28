#include <iostream>
#include <cstdio>
#define NAME "b-large"
using namespace std;
int T;
int main(){
	freopen(NAME".in","rt",stdin);
	freopen(NAME".out","wt",stdout);
	cin>>T;
	for(int I=1;I<=T;I++) {
		printf("Case #%d: ",I);
		long double c,f,x;
		cin>>c>>f>>x;
		long double v=2;
		long double t=0;
		while(1){
			if(x/v > c/v+x/(v+f)) {
				t+=c/v; 
				v+=f;
			} else {
				t+=x/v;
				break;
			}
		}
		printf("%0.7lf\n",(double)t);
	}
	return 0;
}