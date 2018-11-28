#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;
#define LL long long
#define MAXN 110
int a[MAXN][2];
char s[MAXN];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,n;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%s",s);
		memset(a,0,sizeof(a));
		int len=strlen(s);
		a[0][0]=(s[0]=='-');
		a[0][1]=(s[0]=='+');
		for(int i=1;i<len;i++){
			if(s[i]=='+'){
				a[i][0]=a[i-1][0];
				a[i][1]=1+a[i-1][0];
			}else{
				a[i][1]=a[i-1][1];
				a[i][0]=1+a[i-1][1];
			}
		}
		printf("Case #%d: %d\n",cas,a[len-1][0]);
	}
	return 0;
}
