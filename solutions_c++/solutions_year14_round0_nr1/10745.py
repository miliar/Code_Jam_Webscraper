#include<iostream>
#include<fstream>
using namespace std;
bool isSame(int arr1[][4],int arr2[][4])
{
	for (int j = 0; j < 4; j++)
		for (int k = 0; k < 4; k++)
			if(arr1[j][k]!=arr2[j][k])
				return false;
	return true;
}
bool Isthere(int key,int arr[])
{
	for (int i = 0; i < 4; i++)
		if(arr[i]==key)
			return true;
	return false;
}
int GetCard(int arr1[][4],int arr2[][4],int arr[],int answer1,int answer2)
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if(arr1[answer1][i]==arr2[answer2][j])
				if(!Isthere(arr1[answer1][i],arr))
					return arr1[answer1][i];
	return -1;
}
void Play()
{
	ifstream ifile("A-small-attempt1.in");
	ofstream ofile("output.txt");
	if(ifile.fail())
	{
		cout<<"Unable to open the input file";
		exit(1);
	}

	int total_cases=0;
	ifile>>total_cases;
	for (int i = 0; i < total_cases; i++)
	{
		int arr1[4][4];
		int arr2[4][4];
		int answer1=0,answer2=0;
		ifile>>answer1;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				ifile>>arr1[j][k];
		ifile>>answer2;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				ifile>>arr2[j][k];
		int card=-1;
		if(isSame(arr1,arr2))
		{
			if(answer1==answer2)
				ofile<<"Case #"<<i+1<<": Bad Magician!"<<endl;
			else
				ofile<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
		else
		{
			int arr3[4]={0};
			int count=0;
			for (int j = 0; j < 4; j++)
			{
				arr3[j]=GetCard(arr1,arr2,arr3,answer1-1,answer2-1);
				if(arr3[j]>0)
					count++;
			}
			if(count==0)
				ofile<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
			else if(count>1)
				ofile<<"Case #"<<i+1<<": Bad magician!"<<endl;
			else
				ofile<<"Case #"<<i+1<<": "<<arr3[0]<<endl;
		}
		
			
	}
	ofile.close();
	ifile.close();
}
int main()
{
	Play();
	return 0;
}