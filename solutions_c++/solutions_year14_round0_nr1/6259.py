#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<set>
#include<vector>
using namespace std;
main()
{
	int cases;
	scanf("%d",&cases);
	int a[4][4];
	for(int c1=1;c1<=cases;c1++)
	{
		int row1,row2;
		vector <int> a1,a2;
		scanf("%d",&row1);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		for(int j=0;j<4;j++)
			a1.push_back(a[row1-1][j]);
		scanf("%d",&row2);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		for(int j=0;j<4;j++)
			a2.push_back(a[row2-1][j]);
		int ret=0,ret1;
		for(int i=0;i<a1.size();i++)
			for(int j=0;j<a2.size();j++)
				if(a1[i]==a2[j])
				{
					ret++;
					ret1=a1[i];
					break;
				}
//		cout<<"ret "<<ret<<"\n";
		if(ret==1)
			printf("Case #%d: %d\n",c1,ret1);
		else if(ret>1)
			printf("Case #%d: Bad magician!\n",c1);
		else
			printf("Case #%d: Volunteer cheated!\n",c1);

	}
}
