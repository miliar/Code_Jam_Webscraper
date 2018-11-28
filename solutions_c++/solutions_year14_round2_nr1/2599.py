#include <stdio.h>
#include <vector>
#include <map>
#include <string.h>
#include <algorithm>

using namespace std;

#define f(i,n) for(int i=0; i <n;i++)


int main()
{
	int T;
	scanf("%d",&T);
	f(i,T)
	{
		int n;
		scanf("%d",&n);
		int ind;
			char ar[100][100];
			char ar2[100][100];
			char ar3[100][100];
		f(j,n)
		{
			f(k,100)
			{
				ar[j][k]=0;
				ar2[j][k]=0;
				ar3[j][k]=0;
			}

			scanf("%s",ar[j]);
			ar2[j][0] = ar[j][0];
			ind =0;
			int count = 1;
			f(k, strlen(ar[j]))
			{
				if(k==0)continue;
				if(ar[j][k]!=ar2[j][ind])
				{
					ar3[j][ind] = count;
					//printf("j ind %d %d %d\n",j, ind, count);
					ind++;
					count = 1;
					ar2[j][ind] = ar[j][k];
				}
				else
				{
					count++;
				}
			}

			ar3[j][ind] = count;
			//printf("j ind %d %d %d\n",j, ind, count);
			ind++;
		}

		bool works = true;
		f(j,n)
		{
			//printf("%s\n",ar2[j]);
			
			if(j==0)continue;
			if(strcmp(ar2[j],ar2[j-1]))
			{
				works = false;
			}
		}

		if(!works)
		{
			printf("Case #%d: Fegla Won\n",i+1);
			continue;
		}
/*
		f(j,n)
		{
			f(k,ind)
				printf("%d ",ar3[j][k]);
			printf("\n");
		}
		printf("done\n");
*/
		int ar4[100][100];
		f(j,100)
			f(k,100)
				ar4[j][k] = ar3[k][j];
		/*	
		f(j,ind)
		{
			f(k,n)
				printf("%d ",ar4[j][k]);
			printf("\n");
		}

		printf("done2\n");
*/
		f(j,100)
			sort(ar4[j],ar4[j]+n);
		int* med = new int [ind];
		f(j,ind)
		{
			med[j] = 0;
			f(k,n)
			{
			//	printf("%d ",ar4[j][k]);
				med[j]+=abs(ar4[j][k]-ar4[j][n/2]);
			}

		//	printf("\n");
		}

		int tot = 0;
		f(j,ind)
		{
			tot+=med[j];
		}

		printf("Case #%d: %d\n",i+1,tot);
	}
	return 0;
}
