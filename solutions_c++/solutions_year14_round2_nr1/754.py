#include <bits/stdc++.h>
using namespace std;
int tcs, n, cl[105][105];
char str[105][105], comp[105][105];
int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		scanf("%i", &n);
		memset(str, 0, sizeof str);
		memset(comp, 0, sizeof comp);
		bool ok = 1;
		int ans = 0, bs = 1;
		for(int i=0;i<n;i++){
			scanf("%s", str[i]);
			comp[i][0] = str[i][0];
			cl[i][0] = 1;
			int icmp = 1;
			for(int j=1;j<strlen(str[i]);j++){
				if(str[i][j] == str[i][j-1]) {cl[i][icmp - 1]++; continue;}
				cl[i][icmp] = 1;
				comp[i][icmp] = str[i][j];
				icmp++;
			}
			bs = icmp;
			if(strcmp(comp[i], comp[0]) != 0) ok = 0;
		}
		if(ok == 0){
			printf("Case #%i: Fegla Won\n", tc);
			continue;
		}
		for(int i=0;i<bs;i++){
			int ms = 1<<30;
			for(int j=0;j<n;j++){
				ms = min(ms, cl[j][i]);
			}
			//printf("%i\n", s/n);
			for(int j=0;j<n;j++){
				ans += cl[j][i] - ms;
			}
		}
		printf("Case #%i: %i\n", tc, ans);
	}
}