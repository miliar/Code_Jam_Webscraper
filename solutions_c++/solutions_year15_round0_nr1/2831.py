#include<stdio.h>
#include<cstdlib>
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int sm;
	char s[1002];
	int cur;
	int ans;
	for(int ca=0;ca<t;ca++){
		scanf("%d",&sm);
		scanf("%s", s );
		cur=ans=0;
		for(int i=0;i<=sm;i++){
			if(cur<i){
				ans+=i-cur;
				cur =i;
			}
			cur+=s[i]-'0';
		}
		printf("Case #%d: %d\n",ca+1,ans);
	}
}
