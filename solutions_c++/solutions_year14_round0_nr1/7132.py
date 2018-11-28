#include<bits/stdc++.h>
using namespace std;

int a[5][5],b[5][5],ra,rb,t,tcase=0;
vector<int> ans;

int main()
{
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&ra);
		for(int i=1;i<=4;i++)
		  for(int j=1;j<=4;j++)
			scanf("%d",&a[i][j]);
		scanf("%d",&rb);
		for(int i=1;i<=4;i++)
		  for(int j=1;j<=4;j++)
			scanf("%d",&b[i][j]);
		
		ans.clear();
		for(int i=1;i<=4;i++)
		  for(int j=1;j<=4;j++)
			if(a[ra][i]==b[rb][j])
			  ans.push_back(a[ra][i]);
		printf("Case #%d: ",++tcase);
		if(ans.size()==0)
		  puts("Volunteer cheated!");
		else if(ans.size()>1)
		  puts("Bad magician!");
		else
		  printf("%d\n",ans[0]);
	}

	return 0;
}
