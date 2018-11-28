#include<iostream>
#include<fstream>
#include<string>

int main()
{
	using namespace std;
	ifstream fin("a_small_in.txt");
	ofstream fout("a_small_out.txt");

	int count;
	fin>>count;
	for(int i=1;i<=count;i++)
	{
		int row_num[2];
		int first_arr[4][4];
		int second_arr[4][4];

		fin>>row_num[0];
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				fin>>first_arr[j][k];
			}
		}

		fin>>row_num[1];
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				fin>>second_arr[j][k];
			}
		}

		int a=0;
		int picked_num=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(first_arr[row_num[0]-1][j]-second_arr[row_num[1]-1][k]==0)
				{
					a++;
					picked_num=first_arr[row_num[0]-1][j];
				}

			}
		}
		if(a==0)fout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
		if(a==1)fout<<"Case #"<<i<<": "<<picked_num<<endl;
		if(a>1)fout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;

	}


}