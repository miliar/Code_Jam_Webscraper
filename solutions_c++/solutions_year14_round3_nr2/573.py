#include<stdio.h>
#include<string.h>
#include<set>
#include<algorithm>
using namespace std;
char a[111][111];
int l[111];
bool memo[111][255];
pair<char,char> p[111];
int b[111];
int main()
{
	int q,T;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-output1.txt","w",stdout);
	scanf("%d",&T);
	for(q=1;q<=T;q++){
		int N,i,j;
		scanf("%d",&N);
		for(i=1;i<=N;i++)b[i]=i;
		
		//for(i=1;i<=N;i++){
		//	for(j='a';j<='z';j++)memo[i][j]=false;
		//}
		for(i=1;i<=N;i++){
			scanf("%s",a[i]);
			l[i]=strlen(a[i]);
			p[i].first=a[i][0];
			p[i].second=a[i][l[i]-1];
			for(j=0;j<l[i];j++){
				memo[i][a[i][j]]=true;
			}
		}
		pair<int,int> index;
		int ans=0;
		do{
			bool can=true;
			for(j='a';j<='z';j++)memo[0][j]=false;
			index.first=1;index.second=0;
			int cur=a[b[1]][0];
			memo[0][cur]=true;
			while(index.first<=N){
				//printf("find %d,%d\n",index.first,index.second);
				if(a[b[index.first]][index.second]!=cur){
					cur=a[b[index.first]][index.second];
					if(memo[0][a[b[index.first]][index.second]]==true){can=false;break;}
					memo[0][a[b[index.first]][index.second]]=true;
				}
				index.second++;
				if(index.second>=l[b[index.first]]){index.first++;index.second=0;}
			}
			if(can){
				ans++;
				/*for(i=1;i<=N;i++)printf("%d ",b[i]);
				puts("");*/
			}
		}while(next_permutation(b+1,b+N+1));
		printf("Case #%d: %d\n",q,ans);
		//for(i=1;i<=N;i++){printf("%c %c\n",p[i].first,p[i].second);}
	}
	return 0;
}