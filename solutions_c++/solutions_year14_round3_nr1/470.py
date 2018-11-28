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
	long A, B;
	char S;
	A = B = 0;
	int m = 1;
//	times = 1;
	while(times > 0)
	{
		long K = 0;
		int num = 0;
		fin >> A >> S >> B;
		long large = B;
		long small = A;
		do{
			K = A;
			B = B % A;
			A = B;
			B = K;
		}while (A > 1);
		if (A == 0) {
			large = large / B;
			small = small / B;
		}
		while (large % 2 == 0)
		{
			if (large > small)
				num++;
			large = large / 2;
		}
		if(large != 1)
			fout << "Case #" << m << ": impossible" << endl;
		else if(large == 1)
			fout << "Case #" << m << ": " << num << endl;
		times--;
		m++;
	}
	fin.close();
	fout.close();
	return 0;
}
