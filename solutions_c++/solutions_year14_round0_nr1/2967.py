#include<cstdio>
void solve(int x) {
	int a,ans;
	int n=4,p=0,cout=0;
	int num[5][5];
	int tmp[5];
	scanf("%d",&a);
	for(int i=0;i<n;i++) 
		for(int j=0;j<n;j++) {
			scanf("%d",&num[i][j]);
			if(i+1==a) tmp[p++]=num[i][j];
		}
	scanf("%d",&a);
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++) 
			scanf("%d",&num[i][j]);
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			if(tmp[i]==num[a-1][j]) {
				cout++;
				ans=tmp[i];
			}
	printf("Case #%d: ",x);
	if(cout==0) printf("Volunteer cheated!");
	else if(cout>1) printf("Bad magician!");
	else printf("%d",ans);
	printf("\n");
}
int main () {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++) solve(t+1);
	return 0;
}