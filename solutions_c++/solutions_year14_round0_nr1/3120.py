#include<iostream>
#include<fstream>
#include<string>
using namespace std;

void checkUnique(int arr[][4])
{
	int temp[20] = {0};

	for( int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			temp[arr[i][j]]++;
			if(temp[arr[i][j]] > 1)
				exit(1);
		}
}

int main()
{
	int arr1[4][4],arr2[4][4];
	int T=0;
	ifstream fin("A-small-attempt2.in");
	if(!fin)
		return 1;

	ofstream fout("A.out");
	if(!fout)
		return 1;

	fin>>T;
	if(T<1 || T>100)
		return 1;
	int ans1=0,ans2=0;

	for(int i=0; i<T; i++)
	{
		fin>>ans1;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				fin>>arr1[i][j];
		fin>>ans2;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				fin>>arr2[i][j];

		checkUnique(arr1);
		checkUnique(arr2);

		fout<<"Case #"<<i+1<<": ";
		int val=0;		
		int count=0;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(arr1[ans1-1][i] == arr2[ans2-1][j])
				{
					count++;
					val = arr1[ans1-1][i];
				}
		if(count == 1)
			fout<<val<<endl;
		else if(count >1)
			fout<<"Bad magician!"<<endl;
		else
			fout<<"Volunteer cheated!"<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}