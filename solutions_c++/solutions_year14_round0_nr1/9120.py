#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
int T;
vector<int> read()
{
	vector<int>ans;
	int r;
	static int map[6][6];
	scanf("%d",&r);
	for (int i=1;i<=4;i++)
		for (int j=1;j<=4;j++)
		{
			scanf("%d",&map[i][j]);
			if (i == r)
				ans.push_back(map[i][j]);
		}
	return ans;
}
int main()
{
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++)
	{
		vector<int> a=read(),b=read(),ans;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				if (a[i]==b[j])
				{
					ans.push_back(a[i]);
					break;
				}
		printf("Case #%d: ",TT);
		if (ans.size() == 0)
			printf("Volunteer cheated!\n");
		if (ans.size() > 1)
			printf("Bad magician!\n");
		if (ans.size() == 1)
			printf("%d\n",ans[0]);
	}
	return 0;
}