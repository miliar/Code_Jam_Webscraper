// pancake.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int flip(char *a, int n);
void filter(string);
char  str1[100] = { 0 };
int _tmain(int argc, _TCHAR* argv[])
{
	int testcase = 0;
	ifstream infile("ip.txt");
	ofstream outfile("op.txt");
	infile >> testcase;
	if (testcase < 1 || testcase > 100){
		return 0;
	}
	string str;
	for (int i = 0; i < testcase; i++) {
		memset(str1, 0, 100);
		infile >> str;
		filter(str);
		outfile<<"Case #"<<i+1<<": "<<flip(str1, str.size())<< endl;
	}
	return 0;
}
void filter(string str) {
	int len = str.size();
	for (int i = 0; i < len; i++){
		if (str[i] == '+')
			str1[i] = 1;
		else
			str1[i] = 0;
	}
}
int flip(char *arr, int n)
{
	int i1, m, N = n, i, j; char b;
	for (m = 0 ; ; m++)
	{
		if (arr[0] == 1)
		{
			for (i1 = 0; (i1<n - 1) && (arr[i1 + 1] == 1); i1++);
			if (i1 == n - 1) 
				break; 
		}
		else for (i1 = n - 1; (i1 >= 0) && (arr[i1] == 1); i1--, n--);
		for (i = 0, j = i1; i <= j; i++, j--)
		{
			b = 1 - arr[i]; 
			arr[i] = 1 - arr[j]; 
			arr[j] = b;
		}
	}
	return m;
}