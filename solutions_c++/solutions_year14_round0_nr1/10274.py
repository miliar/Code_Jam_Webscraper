
int main( )
{
	unsigned int card1[4][4];
	unsigned int card2[4][4];
	unsigned int N = 0, ch1 = 0, ch2 = 0; 
	
	
	scanf("%d",&N);

	for(int i = 0; i<N; i++)
	{
		scanf("%d",&ch1);

		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				scanf("%d",&card1[j][k]);
			}
		}

		scanf("%d",&ch2);
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				scanf("%d",&card2[j][k]);
			}
		}
		int cnt = 0;
		int num = 0;
		for(int col1=0; col1<4; col1++)
		{
			for(int col2=0; col2<4; col2++)
			{
				if(card1[ch1 - 1][col1] == card2[ch2 - 1][col2]){
					num = card1[ch1 - 1][col1];
					cnt++;
				}
			}
		}

		if(cnt == 1){
			printf("Case #%d: %d\n",i+1,num);
		}else if(cnt > 1){
			printf("Case #%d: Bad magician!\n",i+1);
		}else if(cnt == 0){
			printf("Case #%d: Volunteer cheated!\n",i+1);
		}
		
	}
  
}

