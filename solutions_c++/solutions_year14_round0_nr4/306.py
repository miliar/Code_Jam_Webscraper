#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;

int n,m,i,j,k,ttt,tt,d,f[100500],t;
long long ans1,ans2;
double a[100500],b[100500];

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		SC(n);
		for (i=1; i<=n; i++)
			scanf("%lf",&a[i]);
		for (i=1; i<=n; i++)
			scanf("%lf",&b[i]);
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);
		d=0;
		for (i=n; i-d>0; i--){
			while (i-d>0 && b[i-d]>a[i]) d++;
		}
		ans1=n-d;
		ans2=0;
		for (i=1; i<=n; i++) f[i]=0;
		for (i=n; i>=1; i--){
			t=0;
			for (j=1; j<=n; j++)
				if (b[j]>a[i] && f[j]==0){
					t=j;
					break;
				}
			if (t){
				f[t]=1;
				continue;
			}
			for (j=1; j<=n; j++)
				if (f[j]==0){
					t=j;
					break;
				}
			f[t]=1;
			ans2++;
		}
		printf("Case #%d: %lld %lld\n",tt,ans1,ans2);
	}
	return 0;
}
