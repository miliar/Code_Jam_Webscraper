#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,fr,sc,num1[4][4],num2[4][4];
    scanf("%d",&t);
	int cse=1,rslt,x,y,z;
	while(t--)
	{
		int counter =0;
		scanf("%d",&fr);
      //  cout<<fr<<"\n";
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&num1[i][j]);
                
     /*   for(int i=0;i<4;i++)
        {
    		for(int j=0;j<4;j++)
			{	printf("%d",num1[i][j]);
			}
            printf("\n");
        }  */
		scanf("%d",&sc);
       // cout<<sc<<"\n";
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				scanf("%d",&num2[x][y]);
			}
		}
        for(int a=0;a<4;a++)
        {
				for(z=0;z<4;z++)
				{
					if(num2[sc-1][a]==num1[fr-1][z] && counter==0)
						{
                            counter+=1;
							rslt=num2[sc-1][a];
                   //         cout<<"yo\n";
						}
					else if(num2[sc-1][a]==num1[fr-1][z] && counter!=0)
					{	counter+=1;
                   // cout<<"yo\n";
					}
                 //   cout<<num2[sc-1][a]<<"=="<<num1[fr-1][z]<<"\n";
				}
			}
         /*for(int i=0;i<4;i++)
        {
        	for(int j=0;j<4;j++)
			{	printf("%d",num2[i][j]);
			}
            printf("\n");
        }  */
		if(counter==1)
			printf("Case #%d: %d\n",cse,rslt);
		else if(counter==0)
			printf("Case #%d: Volunteer cheated!\n",cse);
		else if(counter>1)
				printf("Case #%d: Bad magician!\n",cse);	
        cse++;
	}
    return 0;
}
