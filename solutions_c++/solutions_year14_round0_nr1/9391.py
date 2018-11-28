#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;



// 2014Spring ProblemA
void getRowVal(int rowNum, vector<int>*val)
{
	for (int i = 1; i <= 4; ++i)
	{
		for (int j = 1; j <= 4; ++j)
		{
			int temp; cin >> temp;
			if (i == rowNum)
				val->push_back(temp);
		}
	}
}

int main()
{
	int testNum; cin >> testNum;
	for (int testCount = 1; testCount <= testNum; ++testCount)
	{
		vector<int> val1, val2;
		int firstRow; cin >> firstRow;
		getRowVal(firstRow, &val1);
		int secondRow; cin >> secondRow;
		getRowVal(secondRow, &val2);

		int d=0, val=0;
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				if (val1[i] == val2[j])
				{
					d++;
					val = val1[i];
				}					
			}
		}
		if (d==0)
			cout << "Case #" << testCount << ": " << "Volunteer cheated!" << "\n";
		else if (d==1)
			cout << "Case #" << testCount << ": " << val << "\n";
		else //if (d<=2)
			cout << "Case #" << testCount << ": " << "Bad magician!" << "\n";
	}
	return 0;
}
