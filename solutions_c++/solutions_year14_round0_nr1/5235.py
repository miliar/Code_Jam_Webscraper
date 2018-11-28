#include <bits/stdc++.h>
using namespace std;
char s1[]="Bad magician!";
char s2[]="Volunteer cheated!";
int num[4][4];
vector <int> temp;
vector <int> ans;
int main()
{
	int t,x,i,j,c=0;
	scanf("%d",&t);
	while(c<t)
	{
		c++;
		scanf("%d",&x);
		x--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&num[i][j]);
		temp.clear();
		for(j=0;j<4;j++)
			temp.push_back(num[x][j]);


		scanf("%d",&x);
		x--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&num[i][j]);
		for(j=0;j<4;j++)
			temp.push_back(num[x][j]);

		sort(temp.begin(),temp.end());
		ans.clear();
		for(i=0;i<temp.size()-1;i++)
		{
			if(temp[i]==temp[i+1])
				ans.push_back(temp[i]);
		}
		if(ans.size()==0)
			printf("Case #%d: %s\n",c,s2);
		else if(ans.size()>1)
			printf("Case #%d: %s\n",c,s1);
		else
			printf("Case #%d: %d\n",c,ans[0]);
	}

	return 0;
}