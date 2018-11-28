#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#include<vector>

using namespace std;

long long TenToTwo(long long num,int length)
{
	long long result = 0;
	for (int i = 0; i < length; i++)
	{
		int digit = num % 10;
		result += digit*pow(2, i);
		num = num / 10;
	}
	return result;
}

void TenToTwoToOther(vector<long long>&resultList, long long num, int length)
{
	resultList.clear();
	resultList.resize(11);
	for (int i = 2; i <= 10; i++)
		resultList[i] = 0;
	for (int i = 0; i < length; i++)
	{
		int digit = num % 2;
		for (int j = 2; j <= 10; j++)
		{
			resultList[j] += digit*pow(j, i);
		}
		num = num / 2;
	}
}

bool IfPrime(long long num,long long& divisor)
{
	divisor = 0;
	for (long long i = 2; i <= sqrt(num)+1; i++)
	{
		if (num % i == 0)
		{
			divisor = i;
			return false;
		}
	}
	return true;
}

int main()
{
	fstream in;
	in.open("C://2.txt", ios::in);
	if (in.fail()){
		cerr << "Open graph file inputfile error!" << endl;
		return false;
	}
	ofstream outfile("C://output2.txt");
	if (!outfile){
		cout << "Unable to open outfile";
		exit(1); // terminate with error  
	}

	const int BUFFER_LENGTH = 100000;
	char buffer[BUFFER_LENGTH] = { 0 };
	int CaseNum = 0;
	in.getline(buffer, BUFFER_LENGTH);
	CaseNum = atoi(buffer);
	int length, needNum;
	while (in.getline(buffer, BUFFER_LENGTH))
	{
		sscanf(buffer, "%d	%d", &length, &needNum);
	}
	long long maxNum = 0;
	for (int i = length - 1; i >= 0; i--)
	{
		maxNum += pow(10, i);
	}
	long long minNum = 0;
	minNum = pow(10, length - 1) + 1;
	
	int startNum = TenToTwo(minNum,length);
	int endNum = TenToTwo(maxNum, length);
	int count = 1;
	outfile << "Case #" << count << ": "<< endl;
	for (int probe = startNum; probe <= endNum&&count <= needNum; probe += 2)
	{
		vector<long long>baseResult;
		vector<long long>divisorList;
		divisorList.resize(11);
		bool satisfy = true;
		TenToTwoToOther(baseResult, probe, length);
		for (int i = 2; i <= 10; i++)
		{
			if (IfPrime(baseResult[i], divisorList[i]))
			{
				satisfy = false;
				break;
			}
		}
		if (satisfy)
		{
			outfile << baseResult[10];
			for (int i = 2; i <= 10; i++)
				outfile << " " << divisorList[i];
			outfile << endl;
			count++;
		}
	}

	in.close();
	outfile.close();

	return 0;
}