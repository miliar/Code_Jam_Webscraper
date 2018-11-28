#include <cstdio>

using namespace std;

bool checkRow(int A[][100] , int index  , int N , int key)
{
	int j;
	for(j=0 ; j<N; j++)
	{
		if(A[index][j] > key)
			return false;
	}
	return true;
}
bool checkCol(int A[][100] , int index ,  int M , int key)
{
	int j;
	for(j=0 ; j<M ; j++)
	{
		if(A[j][index] > key)
			return false;
	}
	return true;
}

int main()
{
	int T , garden[100][100] , i , j , N , M;
	scanf("%d" , &T);
	bool flag;
	for(int a=1; a<=T ; a++)
	{
		printf("Case #%d: " , a);
		scanf("%d %d" , &N , &M);
		for(i=0 ; i<N ; i++)
		{
			for(j=0 ; j<M ; j++)
			{
				scanf("%d" , &garden[i][j]);
			}
		}
		flag = true;
		for(i=0 ; i<N ; i++)
		{
			for(j=0 ; j<M ; j++)
			{
				flag = flag && (checkRow(garden , i , M , garden[i][j] ) || checkCol(garden , j , N , garden[i][j] ));
			}			
		}
		if(flag)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
