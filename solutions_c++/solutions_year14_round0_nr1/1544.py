#include <cstdio>

int main()
{
	FILE * Input;
	FILE * Output;
	Output = fopen("output.txt","w");
	Input = fopen("A-small-attempt0.in", "r");
	int TC;
	int count,temp;
	int selected,selected2;
	int arr[5][5],arr2[5][5];
	int memo[4];
	fscanf(Input,"%d", &TC);

	for ( int tc = 1; tc <= TC ; tc++ )
	{
		count = 0;
		fscanf(Input,"%d", &selected);
		for ( int i = 0 ; i < 4 ; i++)
			for ( int j = 0 ; j < 4 ; j++ )
				fscanf(Input,"%d", &arr[i][j]);

		fscanf(Input,"%d",&selected2);
		for ( int i = 0 ; i < 4 ; i++ )		
			for ( int j = 0 ; j < 4 ; j++ )
				fscanf(Input,"%d", &arr2[i][j]);
		
		for ( int i = 0 ; i < 4 ; i++ )
			memo[i] = arr[selected-1][i];
		
		
		for ( int i = 0 ; i < 4 ; i++ )
		{
			for ( int j = 0 ; j < 4 ; j++ )
			{
				if ( memo[i] == arr2[selected2-1][j] )
				{
					count++;
					temp = memo[i];
				}
			}
		}
		
		if ( count == 0 )
			fprintf(Output,"Case #%d: Volunteer cheated!\n", tc);
		else if ( count == 1)
			fprintf(Output,"Case #%d: %d\n",tc, temp);
		else 
			fprintf(Output,"Case #%d: Bad magician!\n",tc);
	}
	fclose(Input);
	fclose(Output);

	return 0;
}
