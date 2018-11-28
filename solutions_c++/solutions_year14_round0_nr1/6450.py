#include<cstdio>
#include<cstring>
using namespace std;
int T,TT,i,j,z,x,ans,cnt[25];
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&TT);
	for(T=1;T<=TT;T++){
		scanf("%d",&x);
		memset(cnt,0,sizeof(cnt));
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++){
				scanf("%d",&z);
				if(i==x)cnt[z]++;
			}
		scanf("%d",&x);
		for(i=1;i<=4;i++)for(j=1;j<=4;j++){
			scanf("%d",&z);
			if(i==x)cnt[z]++;
		}
		ans=0;
		for(i=1;i<=16;i++)if(cnt[i]==2){
			if(ans){
				printf("Case #%d: Bad magician!\n",T);
				break;
			}
			else ans=i;
		}
		if(ans==0)printf("Case #%d: Volunteer cheated!\n",T);
		else if(i==17)printf("Case #%d: %d\n",T,ans);
	}
}