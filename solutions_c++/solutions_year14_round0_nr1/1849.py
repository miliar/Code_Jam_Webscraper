#include<cstdio>
#include<iostream>
using namespace std;
void solve(int T){
	printf("Case #%d: ",T);
	int ans,num=0,row,app[20],map[5][5];
	for(int i=1;i<=16;++i)app[i]=0;
	scanf("%d",&row);
	for(int i=1;i<=4;++i)
		for(int j=1;j<=4;++j){
			int x;
			scanf("%d",&x);
			if(i==row)app[x]=1;
		}
	scanf("%d",&row);
	for(int i=1;i<=4;++i)
		for(int j=1;j<=4;++j){
			int x;
			scanf("%d",&x);
			if(i==row&&app[x]){
				++num;
				ans=x;
			}
		}
	if(num>1)printf("Bad magician!\n");
	else if(num==0)printf("Volunteer cheated!\n");
	else printf("%d\n",ans);
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int i=1;i<=test;++i)solve(i);
	return 0;
} 
