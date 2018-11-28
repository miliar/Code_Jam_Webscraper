#include <stdio.h>
#include <math.h>

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int i,j,k,T,cnt,kcase=1,res;
	char s[1100];
	scanf("%d",&T);
	while(T--){
		scanf("%d",&k);
		scanf("%s",s);
		res=0;cnt=0;
		if(s[0]=='0') cnt=res=1;
		else cnt=s[0]-'0';
		for(i=1;i<=k;i++){
			if(i>cnt){
				res+=(i-cnt);
				cnt=i;
			}
			cnt+=(s[i]-'0');
		}
		printf("Case #%d: %d\n",kcase++,res);
	}
	return 0;
}
