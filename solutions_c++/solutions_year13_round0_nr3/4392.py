#include <stdio.h>

int T,N,M;
int arr[] = {0,1,4,9,121,484,1e5};

int cc(int n)
{
	int i = 0;
	while (arr[i]<=n)
		i++;
	return i;
}

int main(int argc, char *argv())
{
	int i,j;
	int A,B;
	scanf("%d", &T);
	for (int t=0;t<T;++t)
	{
		printf("Case #%d: ", t+1);
		scanf("%d %d", &A, &B);
		printf("%d\n", cc(B)-cc(A-1));
	}
	return 0;
}