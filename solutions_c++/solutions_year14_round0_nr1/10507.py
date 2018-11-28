#include <cstdio>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("a.out","w",stdout);
	int cards[17];
	int cases, row1,row2, card,res,n;
	scanf("%d", &cases);
	for(int k=1; k<=cases; k++)
	{
		res=0;
		scanf("%d", &row1);
		for(int i=1; i<5; i++)
			for(int j=1; j<5; j++)
			{
				scanf("%d", &card);
				cards[card]=i;
			}
		
		scanf("%d", &row2);
		for(int i=1; i<5; i++)
			for(int j=1; j<5; j++)
			{
				scanf("%d", &card);
				if(i==row2)
					if(cards[card]==row1) 
					{
						n=card;
						res++;
					}
			}
		
		printf("Case #%d:", k);
		if(res==0) printf(" Volunteer cheated!\n");
		else if(res==1) printf(" %d\n", n);
		else if(res>1) printf(" Bad magician!\n");
	}
	return 0;
}
