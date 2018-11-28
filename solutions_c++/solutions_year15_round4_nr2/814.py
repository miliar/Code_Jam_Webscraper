#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;
#define ll long long
#define pii pair<int,int>
const double eps = 1e-8;
int sgn(double x){
	if(fabs(x) < eps) return 0;
	return x > 0 ? 1 : -1;
}

void SetIO(){
	char in[] = "B-small-attempt2.in";
	char out[] = "B-small-attempt2.out";
	freopen(in,"r",stdin);
	freopen(out,"w",stdout);
}
int T;
double v,x;
int n;
double r[1010] , c[1010];

int main(){
	SetIO();
	scanf("%d",&T);
	for(int re=1;re<=T;++re){
		scanf("%d%lf%lf",&n,&v,&x);
		for(int i=1;i<=n;++i)
			scanf("%lf%lf",r + i , c + i);
		printf("Case #%d: ",re);
		if(n == 1){
			if(sgn(c[1] - x) == 0){
				printf("%.8lf\n",v / r[1]);
			}
			else puts("IMPOSSIBLE");
		}
		else if(n == 2){
			if(sgn(c[1] - c[2]) == 0){
				if(sgn(c[1] - x) == 0){
					printf("%.8lf\n",v / (r[1]+r[2]));
				}
				else puts("IMPOSSIBLE");
			}
			else if(sgn(c[1] - x) == 0){
				printf("%.8lf\n",v / r[1]);
			}
			else if(sgn(c[2] - x) == 0){
				printf("%.8lf\n",v / r[2]);
			}
			else if(sgn(c[1] - x) < 0 && sgn(c[2] - x) < 0){
				puts("IMPOSSIBLE");
			}
			else if(sgn(c[1] - x) > 0 && sgn(c[2] - x) > 0){
				puts("IMPOSSIBLE");
			}
			else{
				double v1 = v * (x - c[2]) / (c[1] - c[2]);
				double v2 = v - v1;
				printf("%.8lf\n",max(v1/r[1] , v2/r[2]));
			}
		}
	}
	return 0;
}
