#include <cstdio>

#define SIZE 4
int main()
{
	
	//freopen ("aain.txt","r",stdin);
	//freopen ("aaout.txt","w",stdout);
  
	int tc, v, m, t=0;
	scanf("%d", &tc);
	while(tc--)
	{
		t++;
		scanf("%d", &v);
		int varr[SIZE][SIZE];
		for(int i=0;i<SIZE;i++)
			for(int j=0;j<SIZE;j++)
				scanf("%d", &varr[i][j]);
		scanf("%d", &m);
		int marr[SIZE][SIZE];
		for(int i=0;i<SIZE;i++)
			for(int j=0;j<SIZE;j++)
				scanf("%d", &marr[i][j]);
		int ctr=0, ans;		
		for(int i=0;i<SIZE;i++)
		{
			for(int j=0;j<SIZE;j++)
			{
				if(varr[v-1][i]==marr[m-1][j])
				{
					ctr++;
					ans= varr[v-1][i];
				}
			}
		}
		
		if(ctr==1)
		printf("Case #%d: %d\n",t, ans);
		else
		{
			if(ctr==0)
				printf("Case #%d: Volunteer cheated!\n",t);
			else
				printf("Case #%d: Bad magician!\n",t);
		}
	}
	return 0;
}
