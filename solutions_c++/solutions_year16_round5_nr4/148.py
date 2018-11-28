#include<bits/stdc++.h>
using namespace std;
#define eb emplace_back
#define pb push_back
#define mp make_pair
const int md=1e9+7;
const int inf=1e9;
const int maxn=1234;
int T,n,m,l,nq,nk,x;
char s[maxn][maxn];
char bad[maxn];
void task(){
	scanf("%d%d",&n,&l);
	bool flag=false;
	for(int i=1;i<=n;i++) {
		scanf("%s",s[i]+1);
		int cc=0;
		for (int j=1;j<=l;j++)
			if (s[i][j]=='1') cc++;
		if (cc==l) {flag=true;}
	}
	scanf("%s",bad+1);
	if (flag) {
		puts("IMPOSSIBLE");
		return;
	}
	if (l==1) {
		puts("? 0");
		return;
	}
	for(int i=1;i<=l;i++){
		printf("%c",'?');
		if(i<l)printf("0");
	}
	printf(" ");
	for(int i=1;i<l;i++)printf("1");
	printf("\n");
}
int main(){		
	scanf("%d",&T);
	for(int ti=1;ti<=T;ti++){
		printf("Case #%d: ",ti);
		task();
	}	
	
}
