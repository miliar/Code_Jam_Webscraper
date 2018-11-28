#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

#define MAXNUM 15

bool checkA(int A)
{
	int arr[MAXNUM];
	int k=0, N=0;
	while(A>=1)
	{
		arr[k] = A%10;
		k++;
		A = A/10;
		N++;
	}

	for (int i=0; i<N/2; i++)
	{
		if (arr[i] != arr[N-i-1])
			return false;
	}
	return true;
}

bool checkB(int A)
{
	int k=0, N=0;
	int a=sqrt(A);
	if (a*a != A)
		return false;
	else if (checkA(a))
		return true;
	else
		return false;
}

void main()
{
	fstream fs, fs_out;
	fs.open("input.txt", ios::in);
	fs_out.open("output.txt", ios::out);
	int n;
	fs>>n;
	for (int loop=0; loop<n; loop++)
	{
		int A, B;
		fs>>A>>B;
		int sum = 0;
		for (int i=A; i<=B; i++)
			if ( checkB(i) && checkA(i) )
				sum++;

		fs_out<<"Case #"<<loop+1<<": "<<sum<<endl;
	}
	fs.close();
	fs_out.close();
}