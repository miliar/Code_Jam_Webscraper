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
	int A, B, K;
	A = B = K = 0;
	int m = 1;
//	times = 1;
	while(times > 0)
	{
		int count = 0;
		fin >> A >> B >> K;
		cout << A << B << K;
		for(int i = 0; i < A; i++)
			for(int j = 0; j < B; j++)
			{
				if ((i & j) < K) 
				{
					count++;
			//		cout << i << " and " << j << endl;
				}
			}
		cout << count << endl;
		fout << "Case #" << m << ": " << count << endl; 
		times--;
		m++;
	}
	fin.close();
	fout.close();
	return 0;
}
