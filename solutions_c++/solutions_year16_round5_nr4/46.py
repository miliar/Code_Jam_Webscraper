#include <bits/stdc++.h>
using namespace std;
int N,L,Test;
bool flag,ok;
char s[310];
int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&Test);
	for (int tt=1;tt<=Test;tt++){
		scanf("%d%d",&N,&L);
		printf("Case #%d: ",tt);
		flag=0;
		for (int i=1;i<=N;i++){
			scanf("%s",s+1);
			ok=1;
			for (int j=1;j<=L;j++)
				if (s[j]!='1')ok=0;
			flag|=ok;
		}
		scanf("%s",s+1);
		if (flag){
			printf("IMPOSSIBLE\n");
			continue;
		}
		else	if (L==1)printf("0 ?\n");
		else{
			for (int i=1;i<L;i++)printf("?");
			printf(" ");
			printf("10?");
			for (int i=3;i<=L;i++)printf("10");
			printf("1\n");
		}
	}
}