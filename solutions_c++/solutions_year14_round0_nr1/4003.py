#include <bits/stdc++.h>

using namespace std;

void solve()
{
	int x,y, A[4][4], B[4][4];
	std::vector<int> ans;
	ans.clear();
	scanf("%d",&x);
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
			scanf("%d",&A[i][j]);
	scanf("%d",&y);
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
			scanf("%d",&B[i][j]);
	x--; y--;
	for(int i=0;i<4;++i)
	{
		for(int j=0;j<4;++j)
			if(A[x][i]==B[y][j]) ans.push_back(A[x][i]);
	}
	if(ans.size()==1) printf("%d\n",ans[0]);
	else if(ans.size() == 0) printf("Volunteer cheated!\n");
	else printf("Bad magician!\n");
	ans.clear();
	return ;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
