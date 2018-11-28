#include<iostream>
#include<fstream>
using namespace std;

int main()
{
ifstream  in("A-small-attempt1.in");
ofstream out;
out.open("A-small-attempt1.txt",ios::trunc);
int num_a[4][4];
int num_b[4][4];
int n;
in>>n;
for (int i=0;i<n;i++)
	{
	int first,second; 
	in>>first;
	for (int j=0;j<4;j++)
		for (int k=0;k<4;k++)
			in>>num_a[j][k];
	in>>second;
	for (int j=0;j<4;j++)
		for (int k=0;k<4;k++)
			in>>num_b[j][k];
	int num;
	int out_number=0;
	num=0;
	for (int j=0;j<4;j++)
		for (int k=0;k<4;k++)	
	if (num_a[first-1][j]==num_b[second-1][k])
		{
		num=num+1;
		out_number=num_a[first-1][j];
		}
	if (num==1) out<<"Case #"<<i+1<<": "<<out_number<<endl;
	else if (num==0) out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
	else out<<"Case #"<<i+1<<": Bad magician!"<<endl;
	}
return 0;
}
