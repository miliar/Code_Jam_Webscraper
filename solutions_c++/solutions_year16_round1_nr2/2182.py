#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>

using namespace std;


int main()
{
	fstream in;
	in.open("C://B2.in", ios::in);
	if (in.fail()){
		cerr << "Open graph file inputfile error!" << endl;
		return false;
	}
	ofstream outfile("C://2.txt");
	if (!outfile){
		cout << "Unable to open outfile";
		exit(1); // terminate with error  
	}
	const int BUFFER_LENGTH = 100000;
	char buffer[BUFFER_LENGTH] = { 0 };
	int CaseNum = 0;
	in.getline(buffer, BUFFER_LENGTH);
	CaseNum = atoi(buffer);
	int count = 1;
	for (int i = 0; i < CaseNum; i++)
	{
		in.getline(buffer, BUFFER_LENGTH);
		string inputString;
		inputString.assign(buffer);
		int N = atoi(inputString.c_str());
		int max = 2600;
		int min = 0;
		map<int, int>mapList;
		for (int j = 0; j < 2 * N - 1; j++)
		{
			in.getline(buffer, BUFFER_LENGTH);
			vector<int>tempNum;
			stringstream stream1;
			stream1 << buffer;
			string temp;
			while (stream1 >> temp)
			{
				tempNum.push_back(atoi(temp.c_str()));
			}
			for (int tempCount = 0; tempCount < tempNum.size(); tempCount++)
			{
				if (mapList.find(tempNum[tempCount]) == mapList.end())
					mapList[tempNum[tempCount]] = 1;
				else
					mapList[tempNum[tempCount]] ++;
			}
		}
		vector<int>resultList;
		for (map<int, int>::iterator iter = mapList.begin(); iter != mapList.end(); iter++)
		{
			if (iter->second % 2 != 0)
			{
				resultList.push_back(iter->first);
			}
		}
		sort(resultList.begin(), resultList.end());
		outfile << "Case #" << count << ": " << resultList[0];
		for (int resultCount = 1; resultCount < resultList.size(); resultCount++)
		{
			outfile << " " << resultList[resultCount];
		}
		outfile << endl;
		count++;
	}

	in.close();
	outfile.close();

}