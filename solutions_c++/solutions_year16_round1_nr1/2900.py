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
int T;
char s[1024], ans[2048];
int main(){
	freopen("A_in.txt", "r", stdin);
	freopen("A_out.txt", "w", stdout);
	scanf("%d", &T);
	for(int C = 1; C<=T; ++C){
		scanf("%s", s);
		int len = strlen(s);
		int l = 1024, r = 1024;
		ans[l] = s[0];
		for(int i = 1; i < len; ++i)
			if(s[i] < ans[l])
				ans[++r] = s[i];
			else
				ans[--l] = s[i];
		printf("Case #%d: ", C);
		for(int i = l; i<=r; ++i)
			printf("%c", ans[i]);
		printf("\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
