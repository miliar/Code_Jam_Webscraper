#include <cstdio>
#define SIZE 4

bool checkRow(int A[SIZE+1][SIZE+1])
{
	int i,j,sum = 0;
	for(i = 1; i<= SIZE; i++){
		sum = 0;
		for(j = 1; j <= SIZE; j++)
			if(A[i][j])sum++;
		if(sum == 4)return true;
	}
	return false;
}
bool checkColumn(int A[SIZE+1][SIZE+1])
{
	int i,j,sum = 0;
	for(i = 1; i<= SIZE; i++){
		sum = 0;
		for(j = 1; j <= SIZE; j++)
			if(A[j][i])sum++;
		if(sum == 4)return true;
	}
	return false;
}
bool checkCross(int A[SIZE+1][SIZE+1])
{
	int i,j,sum = 0,sum2= 0;;
	for(i = 1; i<= SIZE; i++){
		if(A[i][i])sum++;
		if(A[i][SIZE-i+1])sum2++;
	}
	if(sum == 4 || sum2 == 4)return true;
	return false;
}
int play(int cases)
{
	int A[SIZE+1][SIZE+1] ={ 0 },B[SIZE+1][SIZE+1] = { 0 };
	int i,j,sum =0;
	char inp;
	for(i = 1; i<= SIZE; i++){
		for(j = 1; j <= SIZE; j++)
		{
			scanf(" %c",&inp);
			//printf("%c",inp);
			switch(inp)
			{
				case 'T':
					B[i][j] = 1;
				case 'X':
					A[i][j] = 1;
					++sum;
					break;
				case 'O':
					B[i][j] = 1;
					++sum;
					break;
				default:
					A[i][j] = B[i][j] = 0;
			}
		}
//printf("\n");
	}
	if(checkCross(A) || checkColumn(A) || checkRow(A))
		printf("Case #%d: X won\n",cases);
	else if(checkCross(B) || checkColumn(B) || checkRow(B))
		printf("Case #%d: O won\n",cases);
	else if(sum == 16)
		printf("Case #%d: Draw\n",cases);
	else printf("Case #%d: Game has not completed\n",cases);
	return 0;
}
int main()
{
	int N,i = 0;
	freopen("probA.out","w",stdout);
	freopen("probA.in","r",stdin);
	scanf(" %d",&N);
	while(N--)play(++i);
	

}