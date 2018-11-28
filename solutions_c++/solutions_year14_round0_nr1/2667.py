#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;
typedef pair<int,int> par;
int ar[10];
int main(){
	int t;
	scanf("%d",&t);
	int T=0;
	while(t--){T++;
		int x,tmp;
		scanf("%d",&x);
		for(int i=1;i<x;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&tmp);
		for(int j=0;j<4;j++)
			scanf("%d",&ar[j]);
		for(int i=0;i<(4-x);i++)
			for(int j=0;j<4;j++)
				scanf("%d",&tmp);
		scanf("%d",&x);
		for(int i=1;i<x;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&tmp);
		int ans=0,out=0;
		for(int j=0;j<4;j++){
			scanf("%d",&tmp);
			for(int i=0;i<4;i++)
				if(tmp==ar[i])ans++,out=tmp;
			}
		for(int i=0;i<(4-x);i++)
			for(int j=0;j<4;j++)
				scanf("%d",&tmp);
		if(ans==1)printf("Case #%d: %d\n",T,out);
		else if(!ans)printf("Case #%d: Volunteer cheated!\n",T);
		else printf("Case #%d: Bad magician!\n",T);

		}
    return 0;
    }
