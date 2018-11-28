#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;
int main()
{
	int buffer[256];
	int caseNum;
	ifstream myfile("A-small-attempt1.in");
	ofstream outfile("b.out");
	int ans1, ans2;
	int arr1[4][4];
	int arr2[4][4];
	int myCase = 1;
	myfile >> caseNum;

	while(myCase <= caseNum)
	{
		vector<int> res;
		myfile >> ans1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				myfile >> arr1[i][j];
		myfile >> ans2;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				myfile >> arr2[i][j];
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(arr1[ans1 - 1][i] == arr2[ans2 - 1][j])
					res.push_back(arr1[ans1 - 1][i]);
			}
		}
		if(res.size() == 1)
		{
			outfile << "Case #" << myCase << ": " << res[0] << endl;
		}
		if(res.size() > 1)
		{
			outfile << "Case #" << myCase << ": " << "Bad magician!" << endl;
		}
		if(res.size() == 0)
		{
			outfile << "Case #" << myCase << ": " << "Volunteer cheated!" << endl;
		}
		myCase++;
	}
	myfile.close();
	outfile.close();
}
