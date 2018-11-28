// cpp_console_test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool isFairNumber(const long num)
{
	char buffer[256];
	long length;
	const char *pHead;
	const char *pTail;

	if (num < 10) {
		if (num == 1 || num == 4 || num == 9) return true;
		else return false;
	}

	ltoa(num,buffer,10);
	length = strlen(buffer);
	pHead = buffer;
	pTail = &buffer[length-1];
	while(pHead++ < pTail--)
	{
		if (*pHead != *pTail)
		{
			pHead = buffer;
			break;
		}
	}
	return (pHead > pTail);
}

const long GetCountFairNumbers(const long num1, const long num2)
{
	long count=0;

	for(long i=num1;i<=num2;i++)
	{
		if (isFairNumber(i)) {

			if (i >= 10) {
				long n = sqrt((long double)i);
				//check sqrt value
				if (n*n == i && isFairNumber(n) ) {
					count++;
				}
			} else {
				count++;
			}
		}
	}
	return count;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input;

	if (argc <= 1) {
		cout<<"*usage : "<<*argv[0]<<" input_file_name"<<endl;
		return -1;
	}

	input.open(argv[1],ifstream::in);

	long read_count;
	char buffer[256];

	input.getline(buffer,256);

	read_count=atol(buffer);

	for(long i=0;i<read_count;i++)
	{
		char * pch;
		long num1, num2;

		input.getline(buffer,256);

		pch = strtok(buffer," ");
		num1 = atol(pch);

		pch = strtok(NULL," ");
		num2 = atol(pch);

		cout<<"Case #"<<i+1<<": "<<GetCountFairNumbers(num1,num2)<<endl;
	}
	
	input.close();

	return 0;
}