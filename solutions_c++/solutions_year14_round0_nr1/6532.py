#include <stdio.h>

int arr1[4][4];
int arr2[4][4];

void getArray(int array[][4])
{
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			scanf("%d", &array[i][j]);
		}
	}
}

int judge(int *arr1, int *arr2, int *ans) 
{
	int sameCount = 0;

	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if (arr1[i] == arr2[j]) {
				sameCount++;
				*ans = arr1[i];
			}	
		}
	}
	return sameCount;
}

int main() 
{
	int T;

	scanf("%d", &T);

	for(int i=1; i<=T; i++) 
	{
		int sr1, sr2;

		scanf("%d", &sr1);
		getArray(arr1);

		scanf("%d", &sr2);
		getArray(arr2);

		int ans;
		int result = judge(arr1[sr1-1], arr2[sr2-1], &ans);

		if (result == 1) {
			printf("Case #%d: %d\n", i, ans);
		} else if (result > 1) {
			printf("Case #%d: Bad magician!\n", i);
		} else {
			printf("Case #%d: Volunteer cheated!\n", i);
		}
	}

	return 0;
}
