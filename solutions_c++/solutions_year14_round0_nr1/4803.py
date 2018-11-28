#include <iostream>
#include <vector>
using namespace std;

int p[20];

void solve()
{
	vector<int> ans;
	int i,tmp1,j,x;
	for(i=0;i<20;i++) p[i]=0;
	scanf("%d",&tmp1);
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			scanf("%d",&x);
			if(i+1==tmp1) p[x]++; 
		}
	scanf("%d",&tmp1);
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			scanf("%d",&x);
			if(i+1==tmp1) p[x]++; 
		}
	for(i=0;i<20;i++) if(p[i]==2) ans.push_back(i);
	if(ans.size()==0) {printf("Volunteer cheated!\n"); return;}
	if(ans.size()>1) {printf("Bad magician!\n"); return;}
	printf("%d\n",ans[0]);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++) {printf("Case #%d: ",i); solve();}
	return 0;
}