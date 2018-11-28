#include<iostream>
#include<fstream>
using namespace std;
void main()
{
	int arr1[4][4], arr2[4][4], r1, r2;
	int cases, card, flag;
	ifstream fin("A-small-attempt0.in",ios::in);
	ofstream fout("output.txt",ios::out);
	fin>>cases;
	for(int c=1;c<=cases;c++)
	{  flag=0;
		fin>>r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				fin>>arr1[i][j];
		fin>>r2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				fin>>arr2[i][j];
	r1--;r2--;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(arr1[r1][i]==arr2[r2][j])
			{
				card=arr1[r1][i];
				flag++;
			
			}
	
			fout<<"\nCase #"<<c<<": ";
	if(flag==1)
		fout<<card;
	else if(flag>1)
		fout<<"Bad magician!";
	else 
		fout<<"Volunteer cheated!";
	
	}

	fin.close();
	fout.close();


}