#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int T,n,tmp,point,point2;
	double na[1005],ke[1005];
	scanf("%d",&T);
	for(int z=1;z<=T;z++) {
		scanf("%d",&n);
		for(int a=0;a<n;a++) scanf("%lf",&na[a]);
		for(int a=0;a<n;a++) scanf("%lf",&ke[a]);
		sort(na,na+n);
		sort(ke,ke+n);
		tmp = 0;
		point = 0;
		for(int a=0;a<n;a++) {
			while(na[tmp]<ke[a]) {
				tmp++;
				if(tmp==n) break;
			}
			if(tmp==n) break;
			point++;
			tmp++;
			if(tmp==n) break;
		}
		tmp = 0;
		point2 = 0;
		for(int a=0;a<n;a++) {
			while(ke[tmp]<na[a]) {
				tmp++;
				point2++;
				if(tmp==n) break;
			}
			tmp++;
			if(tmp>=n) break;
		}
		printf("Case #%d: %d %d\n",z,point,point2);
	}
	return 0;
}
