#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cstdlib>
#include<cmath>
using namespace std;
char str[105];
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int i,j,n,m,T,ans,vcase=0;
	scanf("%d",&T);
	while(T--){
		scanf("%s",str+1);
		n=strlen(str+1);
		ans=0;
		if(str[1]=='-'){
			ans=1;
			for(i=2;i<=n;i++){
				if(str[i]!=str[i-1] && str[i]=='-'){
					ans+=2;
				}
			}
		}
		else{
			ans=0;
			for(i=2;i<=n;i++){
				if(str[i]!=str[i-1] && str[i]=='-'){
					ans+=2;
				}
			}
		}
		printf("Case #%d: %d\n",++vcase,ans);
	}
	return 0;
}