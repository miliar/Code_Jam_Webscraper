#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int k,T,i,n,sum,m;

bool t[11];

int main() {
//	freopen("A-large.in","r",stdin);
//	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (k=1;k<=T;k++) {
		scanf("%d",&n);
		printf("Case #%d: ",k);
		if (n==0) printf("INSOMNIA\n");
		else {
			sum=0;
			i=0;
			memset(t,0,sizeof(t));
			while (sum<10) {
				i++;
				m=n*i;
				while (m>0) {
					if (! t[m % 10]) {
						sum++;
						t[m % 10]=true;
					}
					m/=10;
				}
			}
			printf("%d\n",i*n);
		}
	}
	return 0;
}
