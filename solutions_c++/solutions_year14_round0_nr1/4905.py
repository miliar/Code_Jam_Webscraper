#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
	ofstream out("output2.txt");
	ifstream in("A-small-attempt2.in");
	int T;
	in >> T;
	for (int k = 1; k <= T;k++)
	{
		vector<int> myVec1, myVec2;
		int row1;
		in >> row1;
		row1--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int x;
				in >> x;
				if (i == row1)
				{
					myVec1.push_back(x);
				}
			}
		}

		int row2;
		in >> row2;
		row2--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int x;
				in >> x;
				if (i == row2)
				{
					myVec2.push_back(x);
				}
			}
		}

		// input correct
		int count = 0;
		int number;
		for (int i = 0; i < myVec1.size(); i++)
		{
			for (int j = 0; j < myVec2.size(); j++)
			{
				if (myVec1[i] == myVec2[j])
				{
					count++;
					number = myVec1[i];
				}
			}
		}
		out << "Case #" << k << ": ";
		if (count == 0)
		{
			out << "Volunteer cheated!" << endl;
		}
		else if (count == 1)
		{
			out << number << endl;
		}
		else out << "Bad magician!" << endl;
	}
	out.close();
	in.close();
	return 0;
}