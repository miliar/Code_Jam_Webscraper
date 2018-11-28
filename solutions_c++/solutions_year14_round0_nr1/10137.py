/*
 * Problem.cpp
 *
 *  Created on: Mar 13, 2014
 *      Author: yshaalan
 */
using namespace std;
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <sstream>
#include<vector>
#include <map>
#include <math.h>

class SingleCase {
public:
	int _firstAnswer;
	int _secondAnswer;
	int  _firstArrangmentRow [4];
	int _secondArrangmentRow [4];
};

class ProblemCase {
public:
	int _nNumCases;
	SingleCase* _allCases;
};
bool ReadandIntializeCases(string filePath, ProblemCase*& problemCases)
{
  string line;
  ifstream myfile (filePath.c_str());
  if (myfile.is_open())
  {
	problemCases = new ProblemCase();
	getline (myfile,line);
	//cout<<line<<"\n";
	int nNumCases = atoi(line.c_str());
	problemCases->_nNumCases = nNumCases;
	problemCases->_allCases = new  SingleCase[nNumCases];
	//cout<<line<<"\n";
	for (int i=0;i<nNumCases;i++)
	{
		 getline (myfile,line);
		 //cout<<line<<"\n";
		 int nTemp = atoi(line.c_str());
		 problemCases->_allCases[i]._firstAnswer = nTemp;
		 for(int k=0;k<4;k++)
		 {
			 getline (myfile,line);
			 //cout<<line<<"\n";
			 if((k+1) == problemCases->_allCases[i]._firstAnswer)
			 {
			     int nIndex = 0;
				 istringstream iss(line);
				 do
				 {
					 string sub;
					 iss >> sub;
					 if(!sub.empty())
					 {
						 nTemp = atoi(sub.c_str());
						 problemCases->_allCases[i]._firstArrangmentRow[nIndex] = nTemp;
						 nIndex++;
					 }
				 } while (iss);
			 }
		 }
		 getline (myfile,line);
		 //cout<<line<<"\n";
		 nTemp = atoi(line.c_str());
		 problemCases->_allCases[i]._secondAnswer = nTemp;
		 for(int k=0;k<4;k++)
		 {
			 getline (myfile,line);
			 //cout<<line<<"\n";
			 if((k+1) == problemCases->_allCases[i]._secondAnswer)
			 {
			     int nIndex = 0;
				 istringstream iss(line);
				 do
				 {
					 string sub;
					 iss >> sub;
					 if(!sub.empty())
					 {
						 nTemp = atoi(sub.c_str());
						 problemCases->_allCases[i]._secondArrangmentRow[nIndex] = nTemp;
						 nIndex++;
					 }
				 } while (iss);
			 }
		 }
	}
	myfile.close();
	return 1;
  }
  else
  {
	  cout << "Unable to open file";
  }
}
bool solveProblem(ProblemCase* problemCases)
{
	ofstream myfile;
	myfile.open ("solution.txt");

	int nNumCases = problemCases->_nNumCases;
	for (int i=0;i<nNumCases;i++)
	{
		bool bFound = false;
		bool bBadMag = false;
		int nSelected=0;
		 for(int k=0;k<4;k++)
		 {
			for(int l=0;l<4;l++)
			{
				if(problemCases->_allCases[i]._firstArrangmentRow[k] == problemCases->_allCases[i]._secondArrangmentRow[l])
				{
					if(!bFound)
					{
						nSelected = problemCases->_allCases[i]._firstArrangmentRow[k];
						bFound = true;
					}
					else
					{
						if(nSelected != problemCases->_allCases[i]._firstArrangmentRow[k])
						{
							bBadMag = true;
						}
					}
				}
			}
		 }
		 if(bBadMag)
		 {
			myfile<<"\nCase #"<<i+1<<": "<<"Bad magician!";
		 }
		 else
		 {
			 if(bFound)
			 {
				myfile<<"\nCase #"<<i+1<<": "<<nSelected;
			 }
			 else
			 {
				myfile<<"\nCase #"<<i+1<<": "<<"Volunteer cheated!";
			 }
		 }
	}
	myfile.close();
	return 1;
}
int main (int argc, char **argv )
{
	cout << "Sovling the Problem\n";
	int nNumCases=0;
	ProblemCase* problemCases=0;
	string filePath= argv[1];//"B-small-practice.in";
	bool bRet = ReadandIntializeCases(filePath,problemCases);
	if(bRet)
	{
		cout<<"File parsed successfully\n";
		bRet = solveProblem(problemCases);
		if(bRet)
		{
			cout<<"\nSolution completed successfully\n";
		}
		else
		{
			cout<<"Solution failed\n";
		}
	}
	else
	{
		cout<<"Error Reading file\n";
	}
	return 0;
}
