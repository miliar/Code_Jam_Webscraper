#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T,d,ans,len;
char str[10010];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		scanf(" ");
		scanf("%s%d",&str, &d);		
		len = strlen(str);
		ans = 0;
		for (int i=0;i+d<=len;++i)
			if (str[i] == '-'){
				for(int j=i;j<i+d;++j)
					str[j] = '-'+'+'-str[j];
				++ans;
			}
		bool flag = false;
		REP(i,len) if (str[i-1]=='-')
			flag = true;
		if (flag)
			printf("Case #%d: IMPOSSIBLE\n", T_T, ans);
		else
			printf("Case #%d: %d\n", T_T, ans);
	}
}
