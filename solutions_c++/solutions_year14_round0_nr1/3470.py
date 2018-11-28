#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;
int T,t1,t2;
int a[20],b[20],have[20];

int main(){
	scanf("%d",&T);
	int ca=1;
	while(T--){
		scanf("%d",&t1);
		for (int i=1;i<=16;i++) scanf("%d",&a[i]);
		scanf("%d",&t2);
		for (int i=1;i<=16;i++) scanf("%d",&b[i]);
		memset(have,0,sizeof(have));
		for (int i=t1*4-3;i<=t1*4;i++) have[a[i]]++;
		for (int i=t2*4-3;i<=t2*4;i++) have[b[i]]++;
		int ans=0;
		int got=0;
		for (int i=1;i<=16;i++){
			if(have[i]==2) {ans++;got=i;}
		}
		printf("Case #%d: ",ca++);
		if(ans==1) printf("%d\n",got);
		if(ans==0) printf("Volunteer cheated!\n");
		if(ans>1) printf("Bad magician!\n");
	}
	return 0;
}
