#include<iostream>
using namespace std;

void main ()
{
	int n, firstanswer, secondanswer;
	int first [4][4];
	int second [4][4];
	int row [4];
	int count, temp;
	cin>>n;
	for (int k=0;k<n;k++)
	{
	count = 0;
	cin>>firstanswer;
	firstanswer--;
	for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
			cin>>first[i][j];
	cin>>secondanswer;
	secondanswer--;
	for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
			cin>>second[i][j];
	for (int j=0;j<4;j++)
			row[j] = first[firstanswer][j];
	for (int j=0;j<4;j++)
	for (int i=0;i<4;i++)
	{
		if (row[j] == second[secondanswer][i])
		{
			temp = row[j];
			count++;
		}
	}
	if (count==0)
		cout<<"Case #"<<k+1<<": Volunteer cheated!"<<endl;
	else if (count ==1)
		cout<<"Case #"<<k+1<<": "<<temp<<endl;
	else
		cout<<"Case #"<<k+1<<": Bad magician!"<<endl;
	}
}