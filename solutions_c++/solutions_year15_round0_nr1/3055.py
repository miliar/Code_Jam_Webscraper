#include<stdio.h>

int main(){
	int dn,i;
	scanf("%d",&dn);
	for(int di=0;di<dn;di++){
		int n;
		scanf("%d",&n);
		int ans=0,s=0;
		for(int i=0;i<=n;i++){
			char c;
			scanf(" %c",&c);
			int x=c-'0';
			if(x>0&&s<i){
				ans+=i-s;
				s=i;
			}
			s+=x;
		}
		printf("Case #%d: %d\n",di+1,ans);
	}
	return 0;
}