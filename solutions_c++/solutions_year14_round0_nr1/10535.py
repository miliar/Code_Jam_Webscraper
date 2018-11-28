#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{

	ifstream ifile;
	ifile.open("input.txt");

	ofstream ofile;
	ofile.open("output.txt");

	int arr1[4];
	int arr2[4];
	int temparr[4];

	int tests;
	ifile>>tests;
	int row1;
	int row2;
	int temp = 1;

	for(int i = 1; i<=tests; i++)
	{
		int temp = 1;
		ifile>>row1;
		
		while(temp <= row1) 
		{
			for(int j = 0; j<=3; j++)
			{
				ifile>>arr1[j];
			}

			temp++;
		}
		temp = 4 - row1;
		int temp1 = 1;

		while(temp1 <= temp) 
		{
			for(int j = 0; j<=3; j++)
			{
				ifile>>temparr[j];
			}

			temp1++;
		}

		//for the second number picking

		temp = 1;
		ifile>>row2;
		
		while(temp <= row2) 
		{
			for(int j = 0; j<=3; j++)
			{
				ifile>>arr2[j];
			}

			temp++;
		}
		temp = 4 - row2;
		temp1 = 1;

		while(temp1 <= temp) 
		{
			for(int j = 0; j<=3; j++)
			{
				ifile>>temparr[j];
			}

			temp1++;
		}

		vector<int> same; 

		for(int k = 0; k<=3; k++)
		{
			for(int e = 0; e<=3; e++)
			{
				if(arr1[k] == arr2[e])
				{
					same.push_back(arr1[k]);
				}

			}
		}

		if(same.size() == 0)
		{
			ofile<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
		}


		if(same.size() == 1)
		{
			int a = same[0];
			ofile<<"Case #"<<i<<": "<<a<<endl;
			same.pop_back();
		}

		if(same.size() > 1)
		{
			ofile<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
			while(same.size()!=0)
			{
				same.pop_back();
			}
		}



	}



	return 0;
}