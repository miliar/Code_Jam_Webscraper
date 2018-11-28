#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

int got[20];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int N,n,cas=0;
	scanf("%d",&N);
	while	(N--){
		scanf("%d",&n);
		cas++;
		printf("Case #%d: ",cas);
		memset(got,0,sizeof got);
		if (n==0) puts("INSOMNIA");
		else{
			int i,j;
			for	(i=n,j=10;;i+=n){
				int te=i;
				while	(te>0){
					if	(!got[te%10]){
						got[te%10]++;
						j--;
					}
					te/=10;
				}
				if (j==0)	break;
			}
			printf("%d\n",i);
		}
	}
}
