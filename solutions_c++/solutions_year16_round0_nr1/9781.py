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

int check_digits(string strN);

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

	 int GetNoOfcases() {return this->iNoOfCases;}
	 vector<string> & GetStringInfo() {return this->sFileInfo;}
};


int main() {
	int iNoOfCases;
	CParser test;
	test.ReadFile(INPUT_FILE);
	vector<string> &my_vector = test.GetStringInfo();
	vector<string> my_algo;
	iNoOfCases = test.GetNoOfcases();
	for (vector<string>::iterator it = my_vector.begin() ; it != my_vector.end(); ++it)
	{
		int iTemp = check_digits(*it);
		if(iTemp == 0)
			my_algo.push_back("INSOMNIA");
		else
			my_algo.push_back(std::to_string(iTemp));
	}
	test.WriteFile(OUTPUT_FILE, my_algo);
	return 0;
}

int check_digits(string strN)
{
	list<int> digits;
	int iTest;
	int iNo = atoi(strN.c_str());
	if (iNo == 0) return iNo;
	int iCount=0;
	while(1)
	{

		int iTemp = iNo * (iCount+1);
		iTest = digits.size();
		do
		{
			int iTemp2 = iTemp % 10;
			std::list<int>::iterator findIter = std::find(digits.begin(), digits.end(), iTemp2);
			if(findIter == digits.end())
				digits.push_back(iTemp2);
			iTemp = iTemp /10;
		}while(iTemp);

		if(digits.size() == 10) return iNo * (iCount+1);
		iCount++;
	}

	return 0;
}

