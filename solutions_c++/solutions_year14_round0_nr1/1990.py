#include <cstdio>
using namespace std;
int a1[8][8],a2[8][8];
int main()
{
	int t;
	scanf("%d",&t);
	for(int k=0;k<t;k++){
		int ans1,ans2;
		scanf("%d",&ans1);
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)scanf("%d",&a1[i][j]);
		scanf("%d",&ans2);
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)scanf("%d",&a2[i][j]);
		int ct=0,ans;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(a1[ans1-1][i]==a2[ans2-1][j]){
				ans=a1[ans1-1][i];
				++ct;
			}
		if(ct>1)printf("Case #%d: %s\n",k+1,"Bad magician!");
		else if(ct==0)printf("Case #%d: %s\n",k+1,"Volunteer cheated!");
		else printf("Case #%d: %d\n",k+1,ans);
		
	}
	return 0;
}
