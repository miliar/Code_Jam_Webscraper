#include<iostream>
#include<cmath>
#include<fstream>

using namespace std;

int found(int array1[4],int array2[4])
{
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if(array1[j]==array2[i])
				return array1[j];
		}

	}
	return -1;
}

bool badMagician(int array1[4],int array2[4])
{
	int count=0;
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if(array1[j]==array2[i])
				count++;
		}

	}
	if(count>1)
		return true;
	return false;
	return -1;
}



int main()
{
	int T, oPos, fPos;
	int firstArr[4][4];
	int secondArr[4][4];
	int temp[4];
	ifstream in;
	ofstream out;
	in.open("C:\\Users\\Oumar\\Downloads\\A-small-attempt2.in");
	out.open("Output.txt");

	in>>T;


	for(int v=0 ; v<T ; v++)
	{
	in>>oPos;
	oPos--;
	for(int i=0; i<4; i++)
	{
		for(int j=0 ; j<4 ; j++)
		{
			in>>firstArr[i][j];
		}
	}

	for(int p=0; p<4; p++){		temp[p]=firstArr[oPos][p];	}

	in>>fPos;
	fPos--;
	for(int i=0; i<4; i++)
	{
		for(int j=0 ; j<4 ; j++)
		{
			in>>secondArr[i][j];
		}
	}
	

	if(badMagician(temp,secondArr[fPos]))
	{
		out<<"Case #"<<v+1<<": Bad magician!"<<endl;
	}

	else if(found(temp,secondArr[fPos])!= -1)
	{
		int h=found(temp,secondArr[fPos]);
		out<<"Case #"<<v+1<<": "<<h<<endl<<endl;
		
	}
	else
		out<<"Case #"<<v+1<<": Volunteer cheated!"<<endl;

	}
	in.close();
	out.close();
}
