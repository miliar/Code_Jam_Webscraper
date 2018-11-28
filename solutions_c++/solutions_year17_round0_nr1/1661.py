#include<bits/stdc++.h>
using namespace std;

int T,K,len,arr[2000],ans;
char str[2000];

int main(){
	freopen("flipper.in","r",stdin);
	freopen("flipper.out","w",stdout);
	
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		scanf("%s %d",&str, &K);
		len=strlen(str);
		for(int j=0;j<len;j++) {
			if (str[j]=='+') arr[j]=1;
			else arr[j]=0;
		}
		//for (int j=0;j<len;j++) printf("%d",arr[j]); printf("\n");
		ans=0;
		for (int j=0;j<=len-K;j++){
			if (arr[j]!=1){
				ans++;
				for(int k=j;k<j+K;k++) arr[k]=(arr[k]+1)%2;
			}
		}
		for (int j=len-K;j<len;j++){
			if (arr[j]!=1) ans=-1;
		}
		//for (int j=0;j<len;j++) printf("%d",arr[j]); printf("\n");
		printf("Case #%d: ",i);
		if (ans==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}
