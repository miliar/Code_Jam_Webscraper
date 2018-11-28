#include<cstdio>
#include<algorithm>
#include<vector>

int T[20];

int main()
{
	int t;
	scanf("%d", &t);
	for(int qwe=1; qwe<=t; qwe++)
	{
		for(int i=0; i<20; i++) T[i]=0;
		for(int i=0; i<2; i++)
		{
			int a;
			scanf("%d", &a);
			for(int j=0; j<4; j++)
			{
				for(int k=0; k<4; k++)
				{
					int b;
					scanf("%d", &b);
					if(j+1==a) T[b]++;
				}
			}
		}
		int good=0, num=0;
		for(int i=0; i<20; i++)
		{
			if(T[i]==2)
			{
				num=i;
				good++;
			}
		}
		if(good==0) printf("Case #%d: Volunteer cheated!\n", qwe);
		if(good==1) printf("Case #%d: %d\n", qwe, num);
		if(good>1) printf("Case #%d: Bad magician!\n", qwe);
	}
	return 0;
}
