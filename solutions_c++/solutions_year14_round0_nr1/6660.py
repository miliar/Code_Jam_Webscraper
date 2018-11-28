#include<iostream>
using namespace std;

#define Max 4
#define IsRange(a) (a>0 && a<Max+1)

int combination[2][Max][Max];

char message[2][50] = {"Bad magician!", "Volunteer cheated!"};


int main()
{
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("A-small-attempt0.out","w",stdout);

	int t, i, j, k, it, found, result, error;
	int answer[2];

	scanf("%d",&t);
	for(it=1; it<=t; it++)
	{
		for(i=0; i<2 ; i++)
		{
			scanf("%d",&answer[i]);
			for(j=0; j < Max; j++)
			{
				for(k=0; k < Max; k++)
				{
					scanf("%d",&combination[i][j][k]);
				}
			}
		}
		found = error =  result = 0;

		 
		for(j=0; j < Max; j++)
		{
			for(k=0; k < Max; k++)
			{
				if(combination[0][answer[0]-1][j] == combination[1][answer[1]-1][k])
				{
					found++;
					result = combination[0][answer[0]-1][j];
				}
			}
		}

		if(found==0)
		{
			error = 1;
		}
		else if(found == 1)
		{
			error = -1;
		}
		else 
			error = 0;
		 

		printf("Case #%d: ",it);
		if(error == -1)
			printf("%d",result);
		else
			printf("%s",message[error]);

		if(it != t)
			printf("\n");
	}

	return 0;
}