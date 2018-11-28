#include<cstdio>

using namespace std;

int TC,firstAnswer,secondAnswer;
int array1[4][4], array2[4][4];
int a,b,c,counter;
int number;

int main()
 {
 	scanf("%d",&TC);
 	for(a = 1; a <= TC; a++)
 	{
 		counter = 0;
 		scanf("%d",&firstAnswer);
 		
 		// Loop for the Combination 1
 		for(b = 0; b < 4; b++)
 		{
 			for(c = 0; c < 4; c++)
 			{
 				scanf("%d",&array1[b][c]);
 			}
 		}
 		
 		scanf("%d",&secondAnswer);
 		
 		// Loop for the Combination 2
 		for(b = 0; b < 4; b++)
 		{
 			for(c = 0; c < 4; c++)
 			{
 				scanf("%d",&array2[b][c]);
 			}
 		}
 		
 		// To search  the Answer
 		for(b = 0; b < 4; b++)
 		{
 			for(c = 0; c < 4; c++)
 			{
 				if(array1[firstAnswer-1][b] == array2[secondAnswer-1][c])
 				{
 					counter++;
 					number = array1[firstAnswer-1][b];
 				}
 			}
 		}
 		// Answer
 	printf("Case #%d: ",a);
 	if(counter == 0)  printf("Volunteer cheated!\n");
 	else if(counter == 1)  printf("%d\n",number);
 	else printf("Bad magician!\n");
 	
 	}
 	
 	return 0;
 }
