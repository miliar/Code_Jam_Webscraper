#include <cstdio>
#include <cstring>
using namespace std;
char st[10005];
int main(){
	int T,n,i,j,k,l,ans,tt=0;
	scanf("%d",&T);
	while(T--){
		tt++;
		scanf("%s%d",st,&k);
		ans=0;
		n = strlen(st);
		for(i=0;i<n-k+1;i++){
			if(st[i]=='-'){
				ans++;
				for(j=i;j<i+k;j++){
					if(st[j]=='-')st[j]='+';
					else st[j]='-';
				}
			}
		}
		for(i=n-k;i<n;i++)
			if(st[i]=='-')break;
		printf("Case #%d: ",tt);
		if(i<n)printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}
