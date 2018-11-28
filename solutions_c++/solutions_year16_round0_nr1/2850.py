#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<vector>
using namespace std;
typedef long long LL;
int T, N, f[10], cnt;
int main(){
	freopen("A_in.txt", "r", stdin);
	freopen("A_out.txt", "w", stdout);
	scanf("%d", &T);
	for(int C = 1; C<=T; ++C){
		scanf("%d", &N);
		memset(f, 0, sizeof(f));
		cnt = 0;
		LL t = (LL)N;
		for(LL i=0; i<2333333333LL; i+=1LL){
			if(t == 0LL) break;
			for(LL j = t; j; j /= 10LL){
				int k = j % 10LL;
				if(!f[k]){
					f[k] = 1;
					cnt++;
				}
			}
			if(cnt>=10) break;
			t += (LL)N;
		}
		if(cnt>=10) printf("Case #%d: %lld\n", C, t);
		else printf("Case #%d: INSOMNIA\n", C);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
