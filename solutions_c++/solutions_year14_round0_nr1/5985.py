#include <stdio.h>

#define FOR(i,a) for(int i=0;i<a;i++)

int readInt()
{
	int tmp;
	scanf("%d",&tmp);
	return tmp;
}

void readArr(int arr[][4])
{
	FOR(i,4)
		FOR(a,4)
			arr[i][a] = readInt();
}

void testcase(int caseNum)
{
	int aws1 = readInt() - 1;
	int arr1[4][4];

	readArr(arr1);

	int aws2 = readInt() - 1;
	int arr2[4][4];
	readArr(arr2);

	int num = 0;
	int found = 0;

	FOR(i,4)
		FOR(j,4)
			if(arr1[aws1][i] == arr2[aws2][j])
			{
				num = arr1[aws1][i];
				found++;
			}

	if(found == 0)
		printf("Volunteer cheated!");
	else if(found == 1)
		printf("%d",num);
	else
		printf("Bad magician!");
	printf("\n");
}

int main()
{
	int T = readInt();
	FOR(i,T)
	{
		printf("Case #%d: ",i+1);
		testcase(i+1);
	}
	return 0;
}