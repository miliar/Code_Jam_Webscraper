#include<iostream>
#include<cstdio>
#include<cmath>
#include<map>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
	int t,a1,a2,cnt,i,j,k,cntt,tmp;
	int mat1[4][4],mat2[4][4];
	map<int,int>mp;
	scanf("%d",&t);
	cntt=1;
	while(t--)
	{
		mp.clear();  cnt=0;
		scanf("%d",&a1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&mat1[i][j]);
				if(i==a1-1)
					mp[mat1[i][j]]=1;
			}
		}
		scanf("%d",&a2);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&mat2[i][j]);
				if(i==a2-1)
				{
					if(mp[mat2[i][j]]==1)
					{
						cnt++;
						tmp = mat2[i][j];
					}
				}
			}
		}
		if(cnt==1)
			printf("Case #%d: %d\n",cntt,tmp);
		if(cnt>1)
			printf("Case #%d: Bad magician!\n",cntt);
		if(cnt==0)
			printf("Case #%d: Volunteer cheated!\n",cntt);
		cntt++;
	}
	return 0;
}