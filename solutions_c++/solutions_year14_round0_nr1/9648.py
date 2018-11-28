#include <iostream>
#include <fstream>
using namespace std;

const int arrsize=4;
void turn_input(ifstream &fin,unsigned int arr[][arrsize]);
int finalprocess(unsigned int arr1[][arrsize],unsigned int arr2[][arrsize]);

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	unsigned int inputs, arr1[1][arrsize], arr2[1][arrsize];
	fin>>inputs;

	for(int i=0;i<inputs;i++)
	{
		turn_input(fin,arr1);
		turn_input(fin,arr2);
		int result=finalprocess(arr1,arr2);
		if(result==-1)
			fout<<"Case #"<<i+1<<": Bad magician!"<<endl;	
		else if(result==0)
			fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else
			fout<<"Case #"<<i+1<<": "<<result<<endl;
	}


	fout.close();
	fin.close();
	system("pause");
	return 0;
}

void turn_input(ifstream &fin,unsigned int arr[][arrsize])
{
	unsigned int answer,temp;
	fin>>answer;
	for(int j=0;j<arrsize;j++)
	{
		if(answer==j+1)
		{
			for(int k=0;k<arrsize;k++)
			{
				fin>>arr[0][k];
			}
		}
		else
		{
			for(int k=0;k<arrsize;k++)
			{
				fin>>temp;
			}
		}
	}
}

int finalprocess(unsigned int arr1[][arrsize], unsigned int arr2[][arrsize])
{
	unsigned int result=0;
	for(int i=0;i<arrsize;i++)
	{
		for(int j=0;j<arrsize;j++)
		{
			if(arr1[0][i]==arr2[0][j])
			{
				if(result==0)
					result=arr1[0][i];
				else
					return -1;
			}

		}
	}
	return result;

}