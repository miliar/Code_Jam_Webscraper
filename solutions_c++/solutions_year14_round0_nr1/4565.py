#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
 
int main() 
{
	int t,a[4][4],b[4][4],i,j,k,ans1,ans2;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		vector <int> v;
		scanf("%d",&ans1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		}
		scanf("%d",&ans2);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[ans1-1][i]==b[ans2-1][j])
				v.push_back(b[ans2-1][j]);
			}
		}
		if(v.size()>1)
		printf("Case #%d: Bad magician!\n",k);
		else if(v.size()==1)
		printf("Case #%d: %d\n",k,v[0]);
		else
		printf("Case #%d: Volunteer cheated!\n",k);
	}
	return 0;
}