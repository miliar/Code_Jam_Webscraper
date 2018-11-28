#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int War(double A[], double B[], int N)
{
	int i, j, count = 0;
	
	j = 0;
	
	for(i=0; i<N; i++)
	{
		while(j<N && B[j] < A[i])
			j++;
		if(j<N)
		{
			count++;
			j++;
		}
		else
			break;
	}
	
	return N-count;
}

bool myfunction (double i, double j) 
{ 
	return (i<j); 
}

int func(double A[], int i, int j, double B[], int p, int q)
{
	// only 1 element in array
	if(i == j)
	{
		return (A[i] > B[p]);
	}
	
	if(A[j] > B[q])
	{
		return 1 + func(A, i, j-1, B, p, q-1);
	}
	
	return func(A, i+1, j, B, p, q-1);
}


int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int t, counter = 1, i, N, res, res2;
	double A[1005], B[1005];
	
	scanf("%d", &t);
	
	while(t--)
	{
		scanf("%d", &N);
		
		for(i=0; i<N; i++)
			scanf("%lf", &A[i]);
		for(i=0; i<N; i++)
			scanf("%lf", &B[i]);
		
		sort(A, A+N, myfunction);
		sort(B, B+N, myfunction);
		
		/*
		for(i=0; i<N; i++)
			printf("%f ", A[i]);
			printf("\n");
		for(i=0; i<N; i++)
			printf("%f ", B[i]);
			printf("\n");
		*/
		
		res = func(A, 0, N-1, B, 0, N-1);
		res2 = War(A, B, N);
		
		printf("Case #%d: ", counter++);
		printf("%d %d\n", res, res2);				
	}
	
	
	return 0;
}
