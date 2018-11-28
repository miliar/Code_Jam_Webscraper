#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#define MAXN 1005

using namespace std;

const double err = 1e-5;
double naomi[MAXN], ken[MAXN];

int compare_doube(double x, double y){
	if( fabs(x-y) < err )return 0;
	else if(x-y<0)return -1;
	else return 1;
}
int cmp(const void *_a, const void *_b){
	double x = *(double *)_a;
	double y = *(double *)_b;
	return compare_doube(x,y);
}

int main(){
	freopen("D-small-attempt1.in","r",stdin);
	freopen("out.out", "w", stdout);
	int test;
	scanf("%d",&test);
	for(int tt=1;tt<=test;tt++){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%lf",&naomi[i]);
		}
		for(int i=0;i<n;i++){
			scanf("%lf",&ken[i]);
		}
		qsort(ken,n,sizeof(double),cmp);
		int maxi = 0;
		int mini = 0;
		while(1) {
			int rez = 0;
			int rez2 = 0;
			for(int i=0;i<n;i++){
				if(compare_doube(naomi[i],ken[i])>=0){
					rez++;
				}
				if(compare_doube(naomi[i],ken[i])<=0){
					rez2++;
				}
			}
			maxi = max(maxi, rez);
			mini = max(mini, rez2);
			if(!next_permutation(ken,ken+n)){
				break;
			}
		}
		mini = n-mini;
		printf("Case #%d: %d %d\n",tt, maxi, mini);
	}
	return 0;
}