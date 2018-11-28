#include<cstdio>
int num[17];
int main(){
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		for(int j=1;j<=16;j++) num[j]=0;
		for(int j=0;j<=1;j++){
			int x;
			scanf("%d",&x);
			for(int k=1;k<=4;k++){
				int a,b,c,d;
				scanf("%d%d%d%d",&a,&b,&c,&d);
				if(k==x){
					num[a]++;
					num[b]++;
					num[c]++;
					num[d]++;
				}
			}
		}
		int cnt=0,numu;
		for(int j=1;j<=16;j++){
			if(num[j]==2){
				cnt++;
				numu=j;
			}
		}
		printf("Case #%d: ",i);
		if(cnt==0) puts("Volunteer cheated!");
		if(cnt==1) printf("%d\n",numu);
		if(cnt>=2) puts("Bad magician!");
	}
	return 0;
}