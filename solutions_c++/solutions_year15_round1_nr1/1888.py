#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

/*void Sort(long int (&A)[N])
{
	long int tmp;
	for(long int i=0; i<N; i++)
	{
		for(long int j=0; j<N-1; j++)
		{
			if(A[j] > A[j+1])
			{
				tmp = A[j];
				A[j] = A[j+1];
				A[j+1] = tmp;
			}
		}
	}
}*/

long int number2Ofmushrooms(long int A[], long int N)
{
	long int maxDiff = 0;
	for(long int i=0; i<N-1; i++)
	{
		if((A[i] - A[i+1])> maxDiff) maxDiff = A[i] - A[i+1]; 
	}
	long int num = 0;
	for(long int i=0; i<N-1; i++)
	{
		if(A[i] < maxDiff) num = num+A[i];
		else num = num + maxDiff;
	}
	return num;
}

long int number1Ofmushrooms(long int A[], long int N)
{
	long int num1 = 0;
	for(long int i=0; i<N-1; i++)
	{
		if(A[i] > A[i+1])
		{
			num1 = num1 + (A[i] - A[i+1]);
		}
	}
	return num1;
}

int main()
{
	long int T;
	cin >> T;
	long int result[T][2];
	for(long int i=0; i<T; i++)
	{
		long int N;
		cin >> N;
		long int m[N];
		for(long int j=0; j<N; j++)
		{
			cin >> m[j];
		}
		result[i][0] = number1Ofmushrooms(m,N);
		result[i][1] = number2Ofmushrooms(m,N);
		
		//2nd method
		
		
	}
	
	for(long int i=0; i<T; i++)
	{
		cout<<"Case #"<<i+1<<": "<<result[i][0]<<" "<<result[i][1]<<endl;
	}

}
