#include <cstdio>

int main()
{
	int t;
	int poss[4];
	int ans;
	scanf(" %d",&t);
	for(int i=1; i<=t; i++)
	{
		scanf(" %d",&ans);
		for(int k=1; k<ans; k++)
			for(int j=0; j<4; j++)
				scanf(" %*d");
		for(int j=0; j<4; j++)
			scanf(" %d", &poss[j]);
		for(int k=ans+1; k<=4; k++)
			for(int j=0; j<4; j++)
				scanf(" %*d");
		scanf(" %d",&ans);
		for(int k=1; k<ans; k++)
			for(int j=0; j<4; j++)
				scanf(" %*d");
		int qt=0;
		int ant=0;
		int num = 0;
		for(int j=0; j<4; j++)
		{
			int a;
			scanf(" %d", &a);
			qt+=(a==poss[0])+(a==poss[1])+(a==poss[2])+(a==poss[3]);
			if(qt>ant) {num = a; ant = qt;}		
		}
		for(int k=ans+1; k<=4; k++)
			for(int j=0; j<4; j++)
				scanf(" %*d");
		printf("Case #%d: ",i);
		if(qt==1)
			printf("%d\n",num);
		else if(qt>1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}
