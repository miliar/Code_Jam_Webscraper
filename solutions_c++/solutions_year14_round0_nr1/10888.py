//code jam problem 1

#include <iostream>
#include <fstream>
#include <set>

using namespace std;
int main (int argc, char* argv[])
{
	ifstream ifile(argv[1]);
	ofstream ofile("output.txt");
	int numCases;
	
	ifile >> numCases;
	for (int i = 0; i < numCases; i++)
	{
		set<int> nums1;
		int row;
		ifile >> row; //this is the row with the correct number
		for (int j = 1; j <= 4; j++)
		{
			for (int k = 1; k <= 4; k++)
			{
				int num;
				ifile >> num;
				if (j == row)
				{
					nums1.insert(num);
				}
			}
		}
		ifile >> row;
		set <int> nums2;
		for (int j = 1; j <= 4; j++)
		{
			for (int k = 1; k <= 4; k++)
			{
				int num;
				ifile >> num;
				if (j == row)
				{
					nums2.insert(num);
				}
			}
		}
		int flag = 0;
		int common_num;
		for (set<int>::iterator it = nums1.begin(); it != nums1.end(); ++it)
		{
			if (nums2.find(*it)!=nums2.end())
			{
				flag++;
				common_num = *it;
			}
		}
		ofile << "Case #" << i+1 << ": ";
		switch(flag)
		{
			case 0:
				ofile << "Volunteer cheated!";
				break;
			case 1:
				ofile << common_num;
				break;
			default:
				ofile << "Bad magician!";
		}
		ofile << endl;
	}
	
	return 0;
}
