#include <bits/stdc++.h>


using namespace std;

int main() {
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int test, cnt=1;;
	scanf("%d",&test);
	while(test--) {
		int oc[15];
		memset(oc, 0, sizeof oc);
		long long n;
		scanf("%lld",&n);
		printf("Case #%d: ",cnt++);
		if(n==0) {
			printf("INSOMNIA\n");
		}
		else {
			int numb = 1, stat = 0;
			long long n2 = n;
			while(1) {
				long long temp = n2;
				while(temp) {
					oc[temp%10]=1;
					temp/=10;
				}
				for(int i=0;i<=9;i++) {
					if(oc[i]==0) {
						break;
					}
					if(i==9) {
						printf("%d\n",n2);
						stat = 1;
					}
				}
				if(stat) {
					break;
				}
				n2+=n;
				numb++;
			}
		}
	}
	
	
	return 0;
}
