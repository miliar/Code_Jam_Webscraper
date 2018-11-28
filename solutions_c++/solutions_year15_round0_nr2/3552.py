#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int t[1005];

int fun(int a,int n){
	int time=a;
	for(int i=0;i<n;++i){
		time+=(int)t[i]/a;
		if(t[i]%a==0)
			time--;
	}
	return time;
}

int main() {
	int q;
	scanf("%d", &q);
	for(int i=1;i<=q;++i){
		int n;
		scanf("%d", &n);
		for(int j=0;j<n;++j)
			scanf("%d", &t[j]);
		sort(t,t+n);
		int w1=1005;
		for(int j=1;j<=t[n-1];++j)
			w1=min(w1,fun(j,n));
		printf("Case #%d: %d\n", i, w1);
	}
	return 0;
}
