#include <cstdio>

using namespace std;

double c,f,x;
int main(){
	int t,i,j;
	double acum,t1,t2,r;
	scanf("%d",&t);
	for(int cas=1; cas<=t; ++cas){
		scanf("%lf%lf%lf",&c,&f,&x);		
		acum = 0,r=2.0;
		while(true){
			t1 = x/r;
			t2 = c/r + x/(r+f);
			if(t1<t2){ acum+=t1; break; }
			else{
				acum+=c/r;
				r+=f;
			}
		}
		printf("Case #%d: %.7lf\n",cas,acum);
	}
	return 0;
}