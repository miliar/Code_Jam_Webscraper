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

int n,m,i,j,k,ttt,tt,s,a[100500],ans;
bool f[100500];

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		printf("Case #%d: ",tt);
		SC(n); SC(s);
		for (i=1; i<=n; i++){
			SC(a[i]);
			f[i]=0;
		}
		sort(a+1,a+n+1,greater<int>());
		ans=0;
		for (i=1; i<=n; i++){
			if (f[i]) continue;
			ans++;
			f[i]=1;
			k=0;
			for (j=i+1; j<=n; j++){
				if (!f[j] && (a[j]<=s-a[i])){
					k=j;
					break;
				}
			}
			if (k==0) continue;
			f[k]=1;
		}
		printf("%d\n",ans);
	}
	return 0;
}
