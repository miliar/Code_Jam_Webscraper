#include<cstdio>
using namespace std;
 
int main() {
//	freopen("q2.txt","r",stdin);
	freopen("a2.txt","w",stdout);
	int t=0,i,k=0;
	double c,f,x,q;
	scanf("%d",&t);
 
	while(t--) {
		k++;
		q = 2;
		double temp_time=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		double total_time = x/2;
		while(1){
			temp_time = temp_time + c/q;
			q = q+f;
			if(total_time>(temp_time+x/q)) {
				total_time = temp_time+x/q;
			}
			else
			break;
		}
		printf("Case #%d: %0.7lf\n",k,total_time);
	}
	return 0;
}
