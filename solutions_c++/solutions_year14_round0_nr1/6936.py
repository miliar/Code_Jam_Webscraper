#include<iostream>
#include<cstdio>
#include<cmath>
#include<map>
#include<cstring>
#include<string>

using namespace std;
int main()
{
	int Total_kase=0,kase=0,j=0,k=0,user_input_1=0,user_input_2=0;
	int matrix_one[4][4],matrix_two[4][4];
	int same=0,value=0;
	char temp;
	freopen("A-small-attempt1.in","r",stdin);
    freopen("output_file.out","w",stdout);
	
	scanf("%d",&Total_kase);

	for(kase=0;kase<Total_kase;kase++)
	{
		same=0;
		value=0;
		scanf("%d",&user_input_1);

		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			scanf("%d",&matrix_one[j][k]);
		}

		scanf("%d",&user_input_2);

        for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			scanf("%d",&matrix_two[j][k]);
		}
        
		for(k=0;k<4;k++)
		{
			for(j=0;j<4;j++)
			if(matrix_one[user_input_1-1][k]==matrix_two[user_input_2-1][j])
			{
				same++;
				value=matrix_one[user_input_1-1][k];
			}
        }

		if(same>1)
			printf("Case #%d: Bad magician!\n",kase+1);
		else if(same==0)
			printf("Case #%d: Volunteer cheated!\n",kase+1);
		else if(same==1)
			printf("Case #%d: %d\n",kase+1,value);

		/*.........................................
		printf("user input=%d\n",user_input_1);
		for(k=0;k<4;k++)
		{
			for(j=0;j<4;j++)
			printf("%d",matrix_one[k][j]);
			printf("\n");
		}
		printf("user input=%d\n",user_input_2);
		for(k=0;k<4;k++)
		{
			for(j=0;j<4;j++)
			printf("%d",matrix_two[k][j]);
			printf("\n");
		}
		..........................................*/
							
		
	}

	

	return 0;
}
