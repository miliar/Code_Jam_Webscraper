#include <stdio.h>
#include <stdlib.h>
#define rep(i,n) for(i=0;i<n;++i)
#define REP(i,s,n) for(i=s;i <n;++i)

int main()
{
	int T,i,j, k,ans1, ans2, a[4][4], a1[17], flag=0, res = 0;
	FILE* out = fopen("abc.txt","w");
	scanf("%d",&T);
	if(1 > T || T > 100)
		return 0;

	rep(k,T){
		rep(i,17)
			a1[i] = 0;
		flag = 0;
		res = 0;
		scanf("%d",&ans1);
		rep(i,4)
		{
			rep(j,4)
			{
				scanf("%d",&a[i][j]);
				if(i == ans1 - 1)
				{
					a1[a[i][j]] ++;
				}
			}
		}

		scanf("%d",&ans1);
		rep(i,4)
		{
			rep(j,4)
			{
				scanf("%d",&a[i][j]);
				if(i == ans1 - 1)
				{
					a1[a[i][j]] ++;
					if(a1[a[i][j]] == 2){
						res = a[i][j];
						flag ++;
					}
				}
			}
		}
		if(flag == 1)
			fprintf(out,"Case #%d: %d\n",k+1,res);
		else if(flag > 1)
			fprintf(out,"Case #%d: Bad magician!\n",k+1);
		else
			fprintf(out,"Case #%d: Volunteer cheated!\n",k+1);
	}
	fclose(out);
	return 0;
}
