#include <iostream>

#include "fileInput.h"
#include "fileOutput.h"
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <sstream>
#include <string>

using namespace std;


typedef std::pair<int, int> mypair;
bool mySecondfunction(mypair i, mypair j) { return (i.first<j.first); }
bool myfunction(mypair i, mypair j) { return (i.first<j.first); }



bool comparator(const mypair& l, const mypair& r)
{
	return l.first < r.first;
}

struct myclass {
	bool operator() (int i, int j) { return (i<j); }
} myobject;


int main()
{
	//cout << "Hello world";
	//파일 입력, 입력 : 파일명, 출력 : matrix 로 된 파일
	fileInputInterface *inputProcessing;
	fileInput testInput("input.txt");

	std::ifstream infile("input.txt");
	std::string line;

	std::getline(infile, line);

	std::istringstream iss(line);
	int caseNumber = stoi(line);

	vector<vector<string> > tempVector;
	tempVector.resize(caseNumber);

	for (int i = 0; i < caseNumber; i++)
	{
		std::getline(infile, line);
		stringstream stream(line);

		int n = 0;
		int vectorIndex = 1;
		string tempString;
		tempVector[i].resize(2);
		for (int j = 0; j < 2;j++)
		{
			stream >> tempString;
			tempVector[i][j] = tempString;
		}
	}
	cout << endl << endl;
	vector<int> needNumberVector;
	needNumberVector.resize(tempVector.size());
	
	for (int i = 0; i < tempVector.size(); i++)
	{
		int maxNumber = stoi(tempVector[i][0]);
		vector<int> numberInt;
		numberInt.resize(maxNumber+1);
		int wholeSum = 0;
		for (int j = 0; j <= maxNumber; j++)
		{
			numberInt[j]=(int)(tempVector[i][1][j])-'0';
			wholeSum = wholeSum + (int)(tempVector[i][1][j]) - '0';
			//cout << numberInt[j] << " ";
		}
		//cout << endl;

		int needNumber = 0;
		int sumBefore = 0;
		if (numberInt[0] == 0)
		{
			needNumber++;
			sumBefore = sumBefore + 1;
		}
		else
		{
			
			sumBefore = sumBefore + numberInt[0];
		}
		
		
		for (int j = 1; j <= maxNumber; j++)
		{
			if (j > sumBefore)
			{
				needNumber = needNumber+ j - sumBefore;
				sumBefore = j;
			}

			sumBefore = sumBefore + numberInt[j];
		
		}
		needNumberVector[i] = needNumber;
	}
	std::ofstream fmatch("output.txt", std::ios::out);

	for (int i = 0; i < needNumberVector.size(); i++)
	{
		string output = "Case #" + to_string(i + 1) + ": " + to_string(needNumberVector[i])+"\n";
		fmatch << output;
	}
	fmatch.close();

//	std::system("pause");
//	inputProcessing = &testInput;

//	inputProcessing->getFileLinebyLine();
	
	/*
	vector<pair<int, int > > answerVector;
	vector<vector<pair<int, int> > > indexVector;

	indexVector.resize(tempVector.size());
	for (int i = 0; i < tempVector.size(); i++)
	{
		indexVector[i].resize(tempVector[i].size()-2);
		for (int j = 2; j < tempVector[i].size(); j++)
		{
			indexVector[i][j-2] = (mypair (tempVector[i][j], j - 2));
		}
	}

	for (int i = 0; i < indexVector.size(); i++)
	{
		int cNumber = tempVector[i][0];
		int lNumber = tempVector[i][1];

		sort(indexVector[i].begin(), indexVector[i].end(), myfunction);
		for (int j = 0; j < indexVector[i].size(); j++)
		{
			cout << indexVector[i][j].first << " " << indexVector[i][j].second << "  :  ";
		}
		cout << endl;
		for (int j = 0; j < indexVector[i].size()-1;j++)
		{
			cout << i << " : "<<j <<" : " << j+1 << " is ";
			if (std::binary_search(indexVector[i].begin() + j+1 , indexVector[i].end(), pair<int, int>(cNumber - indexVector[i][j].first, 0), mySecondfunction))
				std::cout << "found!\n"; 
			else std::cout << "not found.\n";

		}
		

	}

	*/
	/*
	for (int i = 0; i < tempVector.size(); i++)
	{
		// sorting
		int cNumber = tempVector[i][0];
		int lNumber = tempVector[i][1];

		std::vector<int> myvector(tempVector[i].begin + 2, tempVector[i].begin + tempVector[i].size());

	}
	*/
	/*
	for (int i = 0; i<tempVector.size(); i++)
	{
		int cNumber = tempVector[i][0];
		int lNumber = tempVector[i][1];
		pair<int, int> answerPair;

		bool isFind = false;

		for (int j = 2; j < tempVector[i].size()-1; j++)
		{
			for (int q = j + 1; q < tempVector[i].size(); q++)
			{
				if (tempVector[i][j] + tempVector[i][q] == cNumber)
				{
					answerPair.first = j-1;
					answerPair.second = q-1;
					isFind = true;
					break;
				}
			}
			if (isFind == true)
				break;
		}
		answerVector.push_back(answerPair);
	}
	for (int i = 0; i < answerVector.size(); i++)
	{
		cout << answerVector[i].first << " " << answerVector[i].second << endl;

	}
	*/


	/*
	fileOutputInterface *outputProcessing;
	
	fileOutput testOutput("outputTest.txt");

	vector<string> testTable;
	testTable.resize(3);
	testTable[0] = "Case #1: 2 3";
	testTable[1] = "Case #2: 1 4";
	testTable[2] = "Case #3: 4 5";

	outputProcessing = &testOutput;

	outputProcessing->setFileLinebyLine(testTable);

	cout<<" compare "<<testOutput.compareOutput("output.txt", testTable);
	*/

	
}