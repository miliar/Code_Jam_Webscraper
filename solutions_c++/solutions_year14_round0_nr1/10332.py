#include<cstdio>
#include<cstdlib>

void input (int matrix[][4])
{
	for( int i=0; i<4; i++ )
		for( int j=0; j<4; j++ )
			scanf("%d", &matrix[i][j]);
}  
int compare (int matrix[][4], int memory[], int row)
{
	int count = 0;
	int result = 0;
	
	for( int i=0; i<4; i++ )
	{
		for( int j=0; j<4; j++ )
		{
			if( matrix[row][i] == memory[j] )
			{
				count++;
				result = memory[j];
			}
		}
	}
	
	if( count == 1 )
		return result;
	else if( count > 0 )
		return 0;
	else
		return -1;
}
int main()
{
	int total;
	scanf("%d", &total);
	
	
	
	for( int i=0; i<total; i++ )
	{
		int row[2];
		int matrix[4][4];
		int memory[4];
		int result;
		
		scanf("%d", &row[0]);
		input(matrix);
		
		for( int j=0; j<4; j++ )
			memory[j] = matrix[row[0]-1][j];
		
		scanf("%d", &row[1]);
		input(matrix);
		
		result = compare(matrix, memory, row[1]-1);
		
		printf("Case #%d: ", i+1);
		if( result > 0 )
			printf("%d", result);
		else if( result == 0 )
			printf("Bad magician!");
		else
			printf("Volunteer cheated!");
		printf("\n");
		
	}
	
	return 0;
}
