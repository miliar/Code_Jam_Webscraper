#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#define For(x,a,b) for(int x=a; x<b; x++)
using namespace std;

int main()
{
	int T,row,cont=1,arr[4][4],v[4];
	
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&row);
		For(i,0,4)
		{
				For(j,0,4)
				scanf("%d",&arr[i][j]);
		}

		For(i,0,4) v[i] = arr[row-1][i];
					
		scanf("%d",&row);
		For(i,0,4)
		{
			For(j,0,4)
				scanf("%d",&arr[i][j]);
		}
		
		int res = 0,num = 0;
		
		//For(i,0,4)printf("%d ",v[i]); printf("\n");
//		For(j,0,4)printf("%d ",arr[row-1][j]); printf("\n");
		
		For(i,0,4)
			For(j,0,4)
			{
				if(v[i] == arr[row-1][j])
					num = v[i], res++;
			}
		
		printf("Case #%d: ",cont++);
		if(res == 1) printf("%d\n",num);
		else if(res == 0) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	return 0;
}
