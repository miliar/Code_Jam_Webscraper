#include<iostream>
#include<cstdio>
using namespace std;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; ++i){
		int x;
		scanf("%d",&x);
		printf("Case #%d: ", i+1);
		if(!x) {
			printf("INSOMNIA\n");
			continue;
		}
		int co=0;
		int a[20];
		for(int j=0; j<10; ++j) a[j]=0;
		int now=0;
		while(co<10) {
			now+=x;
			int t=now;
			while(t){
				if(!a[t%10]){a[t%10]=1;++co;}
				t/=10;
			}
		} 
		printf("%d\n",now);
	}
	
	return 0;
}
