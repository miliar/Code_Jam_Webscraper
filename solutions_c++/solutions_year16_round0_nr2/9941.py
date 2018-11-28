//============================================================================
// Name        : test_large.cpp
// Author      : shan
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <list>

using namespace std;

#define INPUT_FILE "D:\\file.txt"
#define OUTPUT_FILE "D:\\output.txt"


int check_jamcoin(string strN, string &strOutput);
uint64_t get_value(int iBaseIndex, vector<char> &data);

class CParser
{
public:
	CParser(){}
private:
  int iNoOfCases; // Needs to use Template...
  vector<string> sFileInfo;

public:
	void ReadFile(const char *pFile)
	{
		string data;
		int iCount=0;
		ifstream ifile; // declaring an object of class ifstream
		   ifile.open(pFile); // open "file.txt" for reading
		   while (!ifile.eof())
		   { // while the end of file [ eof() ] is not reached
		      getline(ifile, data); // read a line from file
		      if(iCount == 0)
		      	this->iNoOfCases = atoi(data.c_str());
		      if(iCount >= 1)
		      {
		      	this->sFileInfo.push_back(data);
		      }
		      iCount++;
		  }
		  ifile.close(); // close the file
	}

	void WriteFile(const char *pFile, vector<string> &my_vector)
		{
			string data;
			ofstream ofile; // declaring an object of class ifstream
			ofile.open(pFile); // open "file.txt" for reading
			int iIndex=1;
			for (vector<string>::iterator it = my_vector.begin() ; it != my_vector.end(); ++it)
			{
				ofile<<"Case #"<<iIndex++<<": "<<*it<<endl;
			}
			  ofile.close(); // close the file
		}


	void WriteFile(const char *pFile, vector<int> &my_vector)
			{
				string data;
				ofstream ofile; // declaring an object of class ifstream
				ofile.open(pFile); // open "file.txt" for reading
				int iIndex=1;
				for (vector<int>::iterator it = my_vector.begin() ; it != my_vector.end(); ++it)
				{
					ofile<<"Case #"<<iIndex++<<": "<<*it<<endl;
				}
				  ofile.close(); // close the file
			}

	 int GetNoOfcases() {return this->iNoOfCases;}
	 vector<string> & GetStringInfo() {return this->sFileInfo;}
};


int main() {
	int iNoOfCases;
	CParser test;
	test.ReadFile(INPUT_FILE);
	vector<string> &my_vector = test.GetStringInfo();
	vector<int> my_algo;
	iNoOfCases = test.GetNoOfcases();
	for (vector<string>::iterator it = my_vector.begin() ; it != my_vector.end(); ++it)
	{
		string test_str = *it;
		vector<char> temp1;
		vector<char> temp(test_str.begin(), test_str.end());
		vector<char>::iterator it2 = temp.begin();
		char old_char = -1, new_char;
		while(it2 != temp.end())
		{
			new_char = *it2;
			if(old_char != new_char)
			{
				temp1.push_back(new_char);
				old_char = new_char;
			}
			it2++;
		}
		if(temp1.size() >2)
		{
			if(new_char == '-')
				my_algo.push_back(temp1.size());
			else
				my_algo.push_back(temp1.size()-1);
		}
		else if(temp1.size() == 2 && temp1[0] == '+')
		{
			my_algo.push_back(2);
		}
		else if(temp1.size() == 1 && temp1[0] == '+')
			my_algo.push_back(0);
		else
			my_algo.push_back(1);

	}
	test.WriteFile(OUTPUT_FILE, my_algo);
	return 0;
}

int check_jamcoin(string strN, string &test_str)
{
	int iCount=0;
	uint64_t value=0;
	while(1)
	{
		vector<char> temp;
		for(int i=2;i<10;i++)
		{
			//copy(strN.c_str(), strN.c_str()+strN.length(), temp);
			//value =get_value(i, temp);
		}
	}

	return 0;
}

#if 0
uint64_t get_value(int iBaseIndex, vector<char> &data)
{
	uint64_t value = 0;
	uint64_t Count=0;
	for (vector<char>::iterator it = data.begin() ; it != data.end(); ++it)
	{
		value = value + ((*it) - '0') * pow(iBaseIndex,Count);
		//sqrt of value = value1
		// 2-value1
		cout<<value<<endl;
		Count++;
	}
	return value;
}
#endif


// If a no is not prime
// check
