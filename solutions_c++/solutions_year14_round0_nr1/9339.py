#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
using std::vector;
int Map[4][4];
void Main()
{
	int T1,T2;
	scanf("%d",&T1);
	for (int i=0;i<4;++i)
	{
		for (int j=0;j<4;++j)
		{
			scanf("%d",&Map[i][j]);
		}
	}
	vector<int> d;
	T1--;
	for (int i=0;i<4;++i) d.push_back(Map[T1][i]);
	scanf("%d",&T2);T2--;
	for (int i=0;i<4;++i)
	{
		for (int j=0;j<4;++j)
		{
			scanf("%d",&Map[i][j]);
		}
	}
	int Count=0,Ans=0;
	for (int i=0;i<4;++i)
	{
		for (int j=0;j<4;++j)
		{
			if (d[i]==Map[T2][j])
			{
				Count++;
				Ans=d[i];
			}
		}
	}
	if (Count==1) printf("%d\n",Ans);
	if (Count>1) puts("Bad magician!");
	if (Count==0) puts("Volunteer cheated!");
}
int main()
{
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
	{
		printf("Case #%d: ",i);
		Main();
	}
	return 0;
}
