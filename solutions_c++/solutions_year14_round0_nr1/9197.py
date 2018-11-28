#include <cstdlib>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> row1;
vector<int> row2;

int main()
{
	FILE *file=freopen("A-small-attempt0.in","r",stdin);
	FILE *file2=freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		int r1,r2;
		scanf("%d",&r1);
		row1.clear();row2.clear();
		int v;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&v);
				if(i==r1)
					row1.push_back(v);
			}

		scanf("%d",&r2);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&v);
				if(i==r2)
					row2.push_back(v);
			}
		int ans=0;
		int ansV=0;
		for(int i=0;i<row1.size();i++)
		{
			int s=row1[i];
			if(find(row2.begin(), row2.end(),s) != row2.end())
			{
				ans++;
				ansV=s;
			}
		}
		printf("Case #%d: ",kase);
		if(ans>1) printf("Bad magician!\n");
		else if(ans==0) printf("Volunteer cheated!\n");
		else printf("%d\n", ansV);
	}
	return 0;
}