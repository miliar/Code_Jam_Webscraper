#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
const int maxn = 1000001;
int ans[maxn];
int main() {
//	int maxt = 0;
	for(int n = 1; n < maxn; ++n) {
		char buff[1024];
		int chk[16];
		for(int x=0;x<10;++x) chk[x] = 0;
		int num = 0;
		int cnt = 0;
		for(int t = 1; t <= 100; ++t) {
//			maxt=max(maxt, t);
			num += n;
			sprintf(buff,"%d",num);
			for(int j = 0; j < strlen(buff);++j) {
				if(chk[buff[j]-'0'] == 0) {
					chk[buff[j]-'0'] = 1;
					cnt++;
					if(cnt == 10) {
						ans[n] = num;
						break;
					}
				}
			}
			if(cnt == 10) break;
		}
	}
//	printf("maxt = %d\n", maxt);
	int T, e = 0;
	scanf("%d",&T);
	while(T--) {
		int n;
		scanf("%d",&n);
		printf("Case #%d: ", ++e);
		if(ans[n] == 0) printf("INSOMNIA\n");
		else printf("%d\n", ans[n]);
	}
	return 0;
}
