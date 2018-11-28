#include<cstdio>
int group[101][101]={0};
char str[101][101];
char cha[101][101];
int min(int a,int b) {
	if(a<b) return a;
	return b;
}
int abs(int a) {
	if(a<0) return -a;
	return a;
}
void solve(int C) {
	int G[101]={0};
	int n;
	scanf("%d",&n);
	printf("Case #%d: ",C);
	for(int i=0;i<n;i++) {
		scanf("%s",str[i]);
		char pev='*';
		for(int j=0;str[i][j];j++) {
			if(str[i][j]!=pev) {
				group[i][G[i]++]=1;
				cha[i][G[i]-1]=str[i][j];
			} else group[i][G[i]-1]++;
			pev=str[i][j];
		}
		//for(int j=0;j<G[i];j++) printf("%c ",cha[i][j]); printf("\n");
		//for(int j=0;j<G[i];j++) printf("%d ",group[i][j]);
		//printf("%d\n",G[i]);
		if(G[0]!=G[i]) {
			printf("Fegla Won\n");
			return;
		}
	}
	int ans=0;
	for(int i=0;i<G[0];i++) {
		int sum=0;
		for(int j=0;j<n;j++) {
			sum+=group[j][i];
			if(cha[j][i]!=cha[0][i]) {
				printf("Fegla Won\n");
				return;
			}
		}
		sum/=n;
		int a=0,b=0;
		for(int j=0;j<n;j++) {
			a+=abs(sum-group[j][i]);
			b+=abs(sum+1-group[j][i]);
		}
		ans+=min(a,b);
	}
	printf("%d\n",ans);
}
int main () {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++) {
		solve(t+1);
	}
	return 0;
}