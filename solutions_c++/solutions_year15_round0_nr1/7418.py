#include <iostream>  
#include <fstream>    
#include <stdlib.h>   
#include <string> 
#include <vector>
using namespace std;


int standing_Ovation(int *a, int num)
{
	int sum = 0;
	int count = 0;
	int add = 0;
	for (int i = 0; i < num; i++)
		sum += a[i];
	for (int i = num - 1; i >= 0; i--)
	{
		int diff = i - (sum - a[i]);
		if (diff>0 && add<diff)
		{
			add = diff;
		}
		sum = sum - a[i];
	}
	return add;
}

int numDigits(int num)
{
	if (num == 0)return 1;
	int count = 0;
	while (num)
	{
		num = num / 10;
		count++;
	}
	return count;
}
int main()
{
	ifstream in("A-large.in");         
	ofstream out("A-large.out");       
	if (!in.is_open() || in.eof())             
	{
		cerr << "ERROR: invalid input file" << endl;
		return (-1);
	}
	if (!out.is_open())                         
	{
		cerr << "ERROR: couldn't create ouput file" << endl;
		return (-1);
	}

	int numCases;                      
	string line;                       
	getline(in, line, '\n');            
	numCases = atoi(line.c_str());     
	vector<long long> xVect;
	for (int c = 1; c <= numCases; c++)             
	{
		getline(in, line);
		int num = atoi(line.c_str());
		//int num = line[0] - '0';
		int *a = new int[num + 1];
		int start = numDigits(num)+1;
		int i = start;
		while (line[i])
		{
			a[i - start] = line[i] - '0';
			i++;
		}
		int k = standing_Ovation(a, num + 1);
		out << "Case #" << c << ": " << k << endl;
	}
	in.close();      
	out.close();      

	return 0;
}