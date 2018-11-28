#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>

using namespace std;

string getTheRow(fstream& fstr, unsigned int rowNum)
{
	string result;
	string dummystr;
	unsigned int curRowNum = 1;

	while(curRowNum<rowNum)
	{
		getline(fstr,dummystr);
		curRowNum++;
	}

	getline(fstr,result);

	curRowNum++;

	while(curRowNum<=4)
	{
		getline(fstr,dummystr);
		curRowNum++;
	}

	return result;
}

string caseProcess(unsigned int r1[], unsigned int r2[])
{
	string result;
	vector<unsigned int> concidentNums;

	for(unsigned int i = 0; i< 4; i++)
	{
		for(unsigned int j=0;j<4;j++)
		{
			if(r1[i] == r2[j])
			{
				concidentNums.push_back(r1[i]);
				break;
			}
		}
	}
	unsigned int tot = concidentNums.size();
	if(tot == 0)
	{
		result = "Volunteer cheated!";
	}
	else if(tot == 1)
	{
		stringstream ss;
		ss << concidentNums[0];
		result = ss.str();
	}
	else
		result = "Bad magician!";

	return result;
}

void main()
{
	string filename = "input.in";
	unsigned int numCases = 0;
	unsigned int ans1 = 0;
	unsigned int ans2 = 2;
	unsigned int row1[4];
	unsigned int row2[4];

	fstream fin(filename.c_str(), ios::in);
	string templine;
	getline(fin, templine);
	numCases = atoi(templine.c_str());

	fstream fout("result.out", ios::out);

	for(unsigned int caseInd=1; caseInd<=numCases; caseInd++)
	{
		string caseResult;
		string tempNum;

		//read current case
		getline(fin,templine); ans1 = atoi(templine.c_str());
		stringstream str1; 
		str1 << getTheRow(fin, ans1);

		str1 >> tempNum;
		row1[0] = atoi(tempNum.c_str());
		str1 >> tempNum;
		row1[1] = atoi(tempNum.c_str());		
		str1 >> tempNum;
		row1[2] = atoi(tempNum.c_str());
		str1 >> tempNum;
		row1[3] = atoi(tempNum.c_str());

		getline(fin,templine); ans2 = atoi(templine.c_str());
		stringstream str2; 		
		str2 << getTheRow(fin, ans2);

		str2 >> tempNum;
		row2[0] = atoi(tempNum.c_str());
		str2 >> tempNum;
		row2[1] = atoi(tempNum.c_str());		
		str2 >> tempNum;
		row2[2] = atoi(tempNum.c_str());
		str2 >> tempNum;
		row2[3] = atoi(tempNum.c_str());

		//processing
		caseResult = caseProcess(row1,row2);

		//write the result of current case into the output file
		fout<<"Case #"<<caseInd<<": "<<caseResult<<endl;
	}

	fin.close();
	fout.close();

}
