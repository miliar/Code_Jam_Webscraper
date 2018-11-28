#include <cstdio>
#include <string>
using namespace std;

int main(){
	int T;
	double a,b,k;
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
			int count=0;
			scanf("%lf%lf%lf",&a,&b,&k);
			if (b<a){
				double tmp=a;
				a=b;
				b=tmp;
			}
			for (int x=0;x<a;x++){
				for (int y=x;y<b;y++){
//					printf("%d %d\n",x,y);
					if ( (x & y) < k){
						count++;
						if (x!=y&&y<a&&x<b)
							count++;
					}
				}
			}
			printf("Case #%d: %d\n", i,count);
	}
}