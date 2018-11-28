#include <cstdio>

void run(int r) {
	long long int n;
	bool chk[10]={};
	char str[30]={};
	scanf("%lld",&n);
	long long int ans = 0;
	bool b;
	do {
		b = true;
		ans += n;
		int len;
		len = sprintf(str,"%lld",ans);
		for(int i=0;i<len;i++) {
			chk[str[i]-'0']=true;
		}
		for(int i=0;i<10;i++) {
			b&=chk[i];
		}
	}while(ans!=0 && !b);
	printf("Case #%d: ",r);
	if(ans==0) printf("INSOMNIA");
	else printf("%lld",ans);
	printf("\n");
}

int main() {
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
		run(i);
}