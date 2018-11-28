#include <stdio.h>

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("sample_output.txt", "w", stdout);
	
	int nt, t=1;
	scanf(" %d", &nt);
	
	while(nt--)
	{
		int r1, r2;
		int m1[5][5], m2[5][5];
		
		scanf(" %d", &r1);
		r1--;
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf(" %d", &m1[i][j]);
		
		scanf(" %d", &r2);
		r2--;
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf(" %d", &m2[i][j]);
		
		int card = 0;
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(m1[r1][i] == m2[r2][j])
				{
					if(card == 0)
						card = m1[r1][i];
					else
						card = -1;
				}
		
		printf("Case #%d: ", t++);
		
		if(card == -1)
			printf("Bad magician!\n");
		else if(card == 0)
			printf("Volunteer cheated!\n");
		else
			printf("%d\n", card);
	}
	
	//fclose(stdin);
	//fclose(stdout);
	
	return 0;
}
