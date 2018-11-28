/*************************************************************************
	> File Name: main.cpp
	> Author: ma6174
	> Mail: ma6174@163.com 
	> Created Time: Sun 04 May 2014 12:11:02 AM CST
 ************************************************************************/


#include<iostream>
#include<fstream>
#include<cstdlib>
//#define MAX 10000
//#define LEN 1000
using namespace std;
int main(int argc, char *argv[])
{
	if(argc == 1)
	{
		cerr << "Missing arguments." << endl;
		exit(1);
	}
	if(argc > 3)
	{
		cerr << "Too many arguments" << endl;
		exit(1);
	}
	ifstream fin (argv[1]);
	ofstream fout (argv[2]);
	if(!fin)
	{
		cerr << "No file." << endl;
	}
	int times;
	fin >> times;
//	double weightA[MAX];
	int m = 1;
	int N, M, K;
//	times = 1;
	while(times > 0)
	{
		fin >> N >> M >> K;
		int result = K;
		if (N == 1 || N == 2 || M == 1 || M == 2)
			result = K;
		else if(N == 3 && M == 3)
		{
			if (K > 4) result = K - 1;
			else result = K;
		}
		else if((N == 3 && M == 4) || (N == 4 && M == 3))
		{
			if (K <= 4)
				result = K;
			else if (K > 4 && K < 8)
				result = K - 1;
			else if (K >= 8)
				result = K - 2;
		}
		else if((N == 3 && M == 5) || (N == 5 && M == 3))
		{
			if (K <= 4)
				result = K;
			else if (K > 4 && K < 8)
				result = K - 1;
			else if (K >= 8 && K < 11)
				result = K - 2;
			else if (K >= 11)
				result = K - 3;
		}
		else if((N == 3 && M == 6) || (N == 6 && M == 3))
		{
			if (K <= 4)
				result = K;
			else if (K > 4 && K < 8)
				result = K - 1;
			else if (K >= 8 && K < 11)
				result = K - 2;
			else if (K >= 11 && K < 14)
				result = K - 3;
			else if (K >= 14)
				result = K - 4;
		}
		else if(N == 4 && M == 4)
		{
			if (K <= 4)
				result = K;
			else if (K > 4 && K < 8)
				result = K - 1;
			else if (K >= 8 && K < 10)
				result = K - 2;
			else if (K >= 10 && K < 12)
				result = K - 3;
			else if (K >= 12)
				result = K - 4;
		}
		else if((N == 4 && M == 5) || (N == 5 && M == 4))
		{
			if (K <= 4)
				result = K;
			else if (K > 4 && K < 8)
				result = K - 1;
			else if (K >= 8 && K < 10)
				result = K - 2;
			else if (K >= 10 && K < 12)
				result = K - 3;
			else if (K >= 12 && K < 14)
				result = K - 4;
			else if (K >= 14 && K < 16)
				result = K - 5;
			else if (K >= 16)
				result = K - 6;
		}
		fout << "Case #" << m << ": " << result << endl;
		times--;
		m++;
	}
	fin.close();
	fout.close();
	return 0;
}
