#include <iostream>
#include <fstream>
using namespace std;

unsigned int method_1(int *a, int N)
{
	int sum = 0;
	for(int i=1; i<N; i++)
	{
		if(a[i] < a[i-1])
			sum += (a[i-1] - a[i]);
	}
	return sum;
}

unsigned int method_2(int *a, int N)
{
	int diff_Max = 0;
	for (int i = 1; i < N; ++i)
	{
		if((a[i-1] - a[i]) >= diff_Max)
			diff_Max = (a[i-1] - a[i]);
	}
	int sum = 0;
	for(int i = 1; i<N; i++)
	{
		if((a[i-1] - a[i]) < diff_Max)
		{
			if((a[i - 1] - diff_Max) <= 0)
				sum += a[i-1];
			else 
				sum += diff_Max;
		}
		else
			sum +=diff_Max;
	}
	return sum;
}
int main()
{
	ofstream myfile;
    myfile.open ("a1.txt");
	int t;
	cin >> t;
	for(int i=0; i<t; i++)
	{
		int N, inpArr[9];
		cin >> N;
		for(int j=0; j<9; j++)
			{	inpArr[j] = 0;	}
		for(int j=0; j<N; j++)
			{	cin >> inpArr[j];	}
		unsigned int a = method_1(inpArr, N);
		unsigned int b = method_2(inpArr, N);

		myfile << "Case #"<<i+1<<": "<< a << " " << b << endl;
	}
	return 0;
}
