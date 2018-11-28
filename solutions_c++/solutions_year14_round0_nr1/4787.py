#include <iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
int A[5][5],B[5][5];
int n,a,b;
int solve()
{
	int out=-1;
	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
			if(A[a][i]==B[b][j])
				if(out!=-1)return 0;
				else out=A[a][i];
	}
	return out;
}
int main() {
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		scanf("%d",&a);
		for(int j=1;j<=4;j++)
		{
			for(int u=1;u<=4;u++)
			{
				scanf("%d",&A[j][u]);
			}
		}
		scanf("%d",&b);
		for(int j=1;j<=4;j++)
		{
			for(int u=1;u<=4;u++)
			{
				scanf("%d",&B[j][u]);
			}
		}
		int out=solve();
		string pre="Case #";
		if(out==0)printf("%s%d: Bad magician!\n",pre.c_str(),i);
		else if(out==-1)printf("%s%d: Volunteer cheated!\n",pre.c_str(),i);
		else printf("%s%d: %d\n",pre.c_str(),i,out);
	}
	return 0;
}
