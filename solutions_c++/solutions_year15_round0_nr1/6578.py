#include<iostream>
#include<fstream> 
using namespace std;

int main()
{
	ifstream f;
	ofstream f1;
	f.open("E:\\learn for fun\\code jam\\2015\\QA\\A-small-attempt1.in");
	f1.open("E:\\learn for fun\\code jam\\2015\\QA\\1.out");
	int t,i,j,max,result;
	char number[1111];
	int sum[1111];
	f>>t;
	for (i=0;i<t;i++)
	{
		f>>max;
		for (j=0;j<max+1;j++) 
		{
			f>>number[j];
			number[j] = number[j] - 48;
		}
		result = 0;
		sum[0] = number[0];
		for (j=1;j<max+1;j++)
		{
			sum[j]=sum[j-1]+number[j];
		}
		for (j=1;j<max+1;j++)
		{
			if (j > sum[j-1] + result)
			{
				result += j - sum[j-1] - result;
			}
		}
		f1<<"Case #"<<i+1<<": "<<result<<endl;
	}
	return 0;
}
