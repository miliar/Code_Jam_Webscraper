#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

long long int solve(long long int N, long long int sum,int digit[10])
{
	long long int tim = sum;
	if (tim == 0)
		digit[0]++;
	while (tim > 0)
	{
		digit[tim % 10]++;
		tim = tim / 10;
	}
	int count=0;
	for (int i = 0; i < 10;i++)
	if (digit[i] != 0)
		count++;
	if (count == 10)
		return sum;
	else if (sum + N == sum)
		return -1;
	else
		return solve(N, sum + N, digit);
}
int main()
{
	ofstream fout("out.txt");
	ifstream fin("in.txt");
//	ofstream fout1("in.txt");
//	fout1 << 1000000 << endl;
//	for (int i = 0; i < 1000000; i++)
//		fout1 << i << endl;
	int test_cases;
	fin >> test_cases;
	int num123 = 1;
	while (test_cases--)
	{
		int digit[10];
		for(int i=0;i<10;i++)
			digit[i]= 0;
		long long int num,result;
		fin >> num;
		result = solve(num, num, digit);
		if (result != -1)
			fout <<"Case #"<<num123<<": "<< result << endl;
		else
			fout << "Case #" << num123 << ": " << "INSOMNIA" << endl;
		num123++;
	}
	return 0;
}