#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;


int main(){
	int t, a, b, k, i, j, cs=1;
	long long ans;


    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

	scanf(" %d",&t);
	while(t--) {
		scanf(" %d %d %d",&a,&b,&k);
		ans=0;
		for(i=0;i<a;i++) {
			for(j=0;j<b;j++) {
				if((i&j)<k) ans++;
			}
		}

		printf("Case #%d: %lld\n",cs,ans);
		cs++;

	}

	return 0;
}
