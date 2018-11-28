#include <iostream>
#include <fstream>

using namespace std;

int val;

int GetResult(int *org, int *des)
{
	int same = 0;
	//	for(int i=0;i<4;i++)
	//		cout<<org[i]<<" ";
	//	cout<<endl;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(org[i] == des[j])
			{
				val = des[j];
				same ++;
			}
			//	cout<<same<<endl;
			return same;
}

int main()
{
	ofstream fout("A-small-attempt5.out");
	ifstream fin("A-small-attempt5.in");	
	int t;
	fin>>t;
	int *result;
	result = new int[t];
	for(int i=0;i<t;i++)
	{
		int row;
		int row_num[4][4];
		int probable_num[4];
		fin>>row;
		row--;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
			{
				fin>>row_num[j][k];
				if(row == j)
					probable_num[k] = row_num[j][k];
			}
			//		for(int j=0;j<4;j++)
			//			cout<<probable_num[j]<<endl;
			fin>>row;
			row--;
			for(int j=0;j<4;j++)
				for(int k=0;k<4;k++)
					fin>>row_num[j][k];
			int r = GetResult(row_num[row],probable_num);
			switch(r)
			{
			case 1:
				result[i] = val;
				break;
			case 0:
				result[i] = 0;
				break;
			default:
				result[i] = -1;
				break;
			}
	}
	for(int i=0;i<t;i++)
	{
		if(result[i] == -1)
			fout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		else if(result[i] == 0)
			fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else
			fout<<"Case #"<<i+1<<": "<<result[i]<<endl;
	}
	return 0;
}
