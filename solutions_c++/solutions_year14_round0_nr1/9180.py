#include <cstdio>
#include <iostream>

using namespace std;

int T,n1,n2,in1[5][5],in2[5][5];
int sum,sumj,TT;

int main()
{
	scanf("%d",&T);TT=T;
	while (T--)
	{
		scanf("%d",&n1);
		for (int i=1;i<=4;i++)
		{
			for (int j=1;j<=4;j++)
			{
				scanf("%d",&in1[i][j]);
			}
		}
		scanf("%d",&n2);
		for (int i=1;i<=4;i++)
		{
			for (int j=1;j<=4;j++)
			{
				scanf("%d",&in2[i][j]);
			}
		}

		sum=0; sumj=0;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
			{
				if (in1[n1][i]==in2[n2][j])
					sumj=in1[n1][i],sum++;
			}
		cout<<"Case #"<<TT-T<<": ";
		if (sum==1) cout<<sumj<<"\n";
		else if (sum==0) cout<<"Volunteer cheated!\n";
		else cout<<"Bad magician!\n";
	}
	return 0;
}