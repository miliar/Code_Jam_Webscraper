//by jackyliuxx
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
using namespace std;

int main () {
	int t,n,x,a[10100],tw[10100],k=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&n,&x);
		int i;
		for(i=0;i<n;i++)
			scanf("%d",a+i);
		sort(a,a+n);
		int j,ans=0;
		for(i=0,j=n-1;i<j;j--){
			if(a[i]+a[j]<=x){
				ans++;
				i++;
			}
			else
				ans++;
		}
		if(i==j)
			ans++;
		printf("Case #%d: %d\n",k++,ans);
	}
}
