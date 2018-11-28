#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define LL long long

bool bit[12];
bool test(LL tmp){
	while (tmp){
		int k=tmp%10;
		bit[k]=true;
		tmp/=10;
	}
	for (int i=0;i<=9;i++)
		if (!bit[i]) return false;
	return true;
}

int main(){
	int cases,n;
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%d",&n);
		printf("Case #%d: ",cas);
		if (n==0){
			puts("INSOMNIA");
			continue;
		}

		memset(bit,false,sizeof(bit));
		LL ans=0;
		for (bool flag=false;!flag;){
			ans=ans+n;
			flag=test(ans);
		}
		printf("%lld\n",ans);
	}
	return 0;
}