#include<stdio.h>
#include<string.h>
#include<math.h>
#define maxn 1010
char s[maxn];
int n;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		scanf("%d%s",&n,s);
		int res=0,sum=0;
		for(int i=0;i<=n;i++){
			if(sum<i){
				res+=i-sum;
				sum=i+s[i]-'0';
			}else sum+=s[i]-'0';	
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}
