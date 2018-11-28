#include<bits/stdc++.h>
using namespace std;
int n,a,used[10];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&n);
	for(int i=1 ; i<=n ; i++){
		scanf("%d",&a);
		if(!a){
			printf("Case #%d: INSOMNIA\n",i);
			continue;
		}
		for(int j=a ; ; j+=a){
			int x=j,cnt=0;
			while(x){
				used[x%10]=1;
				x/=10;
			}
			for(int q=0 ; q<=9 ; q++){
				if(!used[q]){
					cnt=1;
					break;
				}
			}
			if(!cnt){
				printf("Case #%d: %d\n",i,j);
				break;
			}
		}
		memset(used,0,sizeof(used));
	}
	return 0;
}
