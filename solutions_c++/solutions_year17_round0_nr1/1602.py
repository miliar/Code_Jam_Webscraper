#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

int T;

const int maxn = 1005;

char s[maxn];


int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> T;
	int cas = 0;
	while(T--){
		scanf("%s",s + 1);
		int n = strlen(s + 1);
		int k;
		scanf("%d",&k);
		int ans = 0;
		for(int i = 1;i <= n - k + 1;i++){
			if(s[i] == '-'){
				ans++;
				for(int j = i;j < i + k;j++){
					if(s[j] == '+'){
						s[j] = '-';
					}else{
						s[j] = '+';
					}
				}
			}
		}
		bool flag = true;
		for(int i = n - k + 2;i <= n;i++){
			if(s[i] == '-') flag = false;
		}
		printf("Case #%d: ",++cas);
		if(flag){
			printf("%d\n",ans);
		}else{
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
