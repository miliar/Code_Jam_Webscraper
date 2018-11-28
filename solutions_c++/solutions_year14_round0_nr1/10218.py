#include <iostream>
#include <string>
#include<fstream>

using namespace std;

int CheckMag(int *arr,int *temp,int pos)
{
	int index=0,counter=0,result=0;
	for (int j=4*(pos-1);j<4*pos;j++)
	{
		for (int kk=0;kk<4;kk++)
		{
			if (temp[kk]==arr[j])
			{
				result=temp[kk];
				counter++;
			}
		}
	}

	if (counter>1)
		return 21;

	else if (counter==1)
		return result;

	return 22;
}

void Savetemp(int *arr2,int *&temp2,int pos2)
{
	int index=0;
	for (int j=4*(pos2-1);j<4*pos2;j++)
	{
		temp2[index]=arr2[j];
		index++;
	}
}

int main()
{
	ifstream in;
	ofstream out;
	in.open("A-small-attempt1.in");
	out.open("moneer.txt");
	int testnum=0,row=0,casenum=0;
	int arr[16];
	int*temp=new int[4];
	in>>testnum;
	if (in.is_open())
	for (int ii=0;ii<testnum;ii++)
	{
		in>>row;
		for (int i=0;i<16;i++)
			in>>arr[i];
		Savetemp(arr,temp,row);
		in>>row;
		for (int i=0;i<16;i++)
			in>>arr[i];

		if (CheckMag(arr,temp,row)==21)
			out<<"Case #"<<casenum+1<<": Bad magician!"<<endl;
		else if (CheckMag(arr,temp,row)==22)
			out<<"Case #"<<casenum+1<<": Volunteer cheated!"<<endl;
		else 
			out<<"Case #"<<casenum+1<<": "<<CheckMag(arr,temp,row)<<endl;
		casenum++;
	}
	in.close();
	return 0;
}