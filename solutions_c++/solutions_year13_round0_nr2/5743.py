// C_ConsoleApplication.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while(std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    return split(s, delim, elems);
}

string ANS(ifstream &infile, string str)
{	
	int id;
	int col;
	int value;

	string answ = "YES";
	vector<string> x = split(str, ' ');
	const int N = stoi(x[0]);
	const int M = stoi(x[1]);
	int* arr = new int[N*M];
	int* minR = new int[N];
	int* maxR = new int[N];
	int* minC = new int[M];
	int* maxC = new int[M];
	for(id = N-1; id >= 0; --id)
	{
		minR[id] = 100;
		maxR[id] = 0;
	}
	for(id = M-1; id >= 0; --id)
	{
		minC[id] = 100;
		maxC[id] = 0;
	}
	//first row
	getline(infile, str);
	vector<string> y = split(str, ' ');
	int row = 0;
	for(col = 0; col < M; ++col)
	{
		id = col;
		value = stoi(y[col]);
		arr[id] = value;

		if(minC[col] > value) minC[col] = value;
		if(maxC[col] < value) maxC[col] = value;
			
		if(minR[row] > value) minR[row] = value;
		if(maxR[row] < value) maxR[row] = value;
	}	
	
	++row;
	while(row < N) 
	{
		getline(infile, str);
		vector<string> y = split(str, ' ');
		for(col = 0; col < M; ++col)
		{
			id = row * M + col;
			value = stoi(y[col]);
			arr[id] = value;
			if(minC[col] > value) minC[col] = value;
			if(maxC[col] < value) maxC[col] = value;
			
			if(minR[row] > value) minR[row] = value;
			if(maxR[row] < value) maxR[row] = value;
			if(col - 1 >= 0)
			{
				if(arr[id] < arr[id-M] && arr[id] < arr[id-1]) answ = "NO";
				if(arr[id-M] < arr[id] && arr[id-M] < arr[id-M-1]) answ = "NO";
					
			}
			if( col + 1 < M)
			{
				if(arr[id-M] < arr[id] && arr[id-M] < arr[id-M+1]) answ = "NO";
				if((id-M-M) > 0) {
					if(arr[id-M] < arr[id-M-M] && arr[id-M] < arr[id-M+1]) answ = "NO";
				}
			}
		}	
		++row;
		//getline(infile, str);
	}
	--row;
	for(col = 0; col < M; ++col)
	{
		id = row * M + col;
		if(col + 1 < M && id-M > 0)
		{
			if(arr[id] < arr[id-M] && arr[id] < arr[id+1]) answ = "NO";
		}
	}

	if(answ == "NO") return answ;

	for(id = 0; id < N; id++)
	{
		for(col = 0; col < M; col++)
		{
			value = id * M + col;
			//arr[value]
			if(minR[id] < maxR[id] && minC[col] < maxC[col])			
				if(arr[value] <= minR[id] && arr[value] <= minC[col])
					return "NO";
			
			/*
			if(arr[id] < arr[id-M] && arr[id] < arr[id-1]) answ = "NO";
			if(arr[id-M] < arr[id] && arr[id-M] < arr[id-M-1]) answ = "NO";				
			if(arr[id-M] < arr[id] && arr[id-M] < arr[id-M+1]) answ = "NO";
			if(arr[id-M] < arr[id-M-M] && arr[id-M] < arr[id-M+1]) answ = "NO";*/
		}
	}

	return answ;//"YES";
}

void test()
{
	string str1, str2;
	ifstream infile;
	infile.open ("data.out");
	ifstream testfile;
	testfile.open ("test.out");

	int n = 0;
	while(getline(infile, str1) && getline(testfile, str2))
	{
		++n;
		if(str1.compare(str2) != 0) cout << str1 << ":::" << str2 << endl;		
	}
	cout << "Compared " << n << " cases!" << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream outfile( "data.out" , ios::app );
	
	string str;
    ifstream infile;
    infile.open ("data.in");
	getline(infile, str);
    int const cases = stoi(str);
	int n = 1;	
	while(n <= cases)
	{
		getline(infile, str);
		outfile << "Case #" << n << ": " << ANS(infile, str) << endl;
		++n;
	}
	infile.close();

	//test();
	
	cin >> n;
	return 0;
}