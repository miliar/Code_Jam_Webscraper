/* scanf example */
#include <stdio.h>

int main ()
{ 
	int t;
	int result = -1;
	int userinput = 0;
	int userinput2 = 0;
	int tmp = 0;
	int match = 0; 
	scanf ("%d",&t);
	int* lines = new int[4];
	int* lines2 = new int[4];
	for (int i = 0; i < t; ++i)
	{
		result = -1;

		scanf ("%d",&userinput);
		lines[0] = 0;
		lines[1] = 0;
		lines[2] = 0;
		lines[3] = 0;
		for (int j = 0; j < 4; ++j)
		{ 
			for (int k = 0; k < 4; ++k)
			{ 
				
				scanf ("%d",&tmp);
				lines[j]|=1<<tmp;
			}
		}
		scanf ("%d",&userinput2);
		lines2[0] = 0;
		lines2[1] = 0;
		lines2[2] = 0;
		lines2[3] = 0;
		for (int j = 0; j < 4; ++j)
		{ 
			for (int k = 0; k < 4; ++k)
			{ 
				
				scanf ("%d",&tmp);
				lines2[j]|=1<<tmp;
			}
		}
		if(userinput>=1 && userinput<=4&&userinput2>=1 && userinput2<=4){
			match =  lines2[userinput2-1]&lines[userinput-1];
			if(match==0){
				result = -2;
			}
			for (int k = 1; k <= 16; ++k)
			{
				if(match == (1<<k)){
					result = k;
				}
			}
		}
		printf ("Case #%d: ",i+1);

		if (result==-1)
		{
			printf ("Bad magician!\n");
		}else if (result==-2){
			printf ("Volunteer cheated!\n");

		}else{
			printf ("%d\n", result);

		}

	}
	
	return 0;
}
