#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> get_union(vector<int> v1, vector<int> v2);

int main()
{
	long long n, N;
	int r1, r2;
	int i, j;
	vector<int> tempVec;
	vector<int> row1;
	vector<int> row2;
	vector<int> resultVec;
	int tempInt;
	int resultSize;
	ifstream inFile("input.txt");
	ofstream outFile("output.txt");

	inFile >> N;

	for (n=0; n<N; ++n)
	{
		inFile >> r1;
		for (i=1; i<=4; ++i)
		{
			tempVec.clear();
			for (j=1; j<=4; ++j)
			{
				inFile >> tempInt;
				tempVec.push_back(tempInt);
			}
			if (i==r1)
			{
				row1=tempVec;
			}
		}
		inFile >> r2;
		for (i=1; i<=4; ++i)
		{
			tempVec.clear();
			for (j=1; j<=4; ++j)
			{
				inFile >> tempInt;
				tempVec.push_back(tempInt);
			}
			if (i==r2)
			{
				row2=tempVec;
			}
		}
		resultVec=get_union(row1, row2);
		resultSize=resultVec.size();
		outFile << "Case #" << n+1 << ": ";
		if (resultSize == 0)
		{
			outFile << "Volunteer cheated!";
		} else if (resultSize == 1) {
			outFile << resultVec[0];
		} else {
			outFile << "Bad magician!";
		}
		outFile << endl;
	}

	inFile.close();
	outFile.close();

	return 0;
}

vector<int> get_union(vector<int> v1, vector<int> v2)
{
	vector<int> i(v1.size()+v2.size());
	vector<int>::iterator it;

	sort(v1.begin(),v1.end());
	sort(v2.begin(),v2.end());

	it=set_intersection(v1.begin(),v1.end(), v2.begin(),v2.end(), i.begin());

	i.resize(it-i.begin());

	return i;
}
