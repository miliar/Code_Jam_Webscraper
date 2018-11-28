#include<iostream>
using namespace std;
int main()
{
int testcase;
cin>>testcase;
//while(testcase--)
for (int x=0; x<testcase; x++)
{
	int select1;
	cin>>select1;
	int marks1[4][4];
	int marks3[4];
	int marks4[4];
	int k;
	int k2;
for(int i=0;i<4;i++)
{
	for(int j=0;j<4;j++)
	{
		cin>>marks1[i][j];
	}
}
int marks2[4][4];
int select2;
cin>>select2;
for(int i=0;i<4;i++)
{
	for(int j=0;j<4;j++)
	{
		cin>>marks2[i][j];
	}
}
int killer =select1;
k=0;
while(killer)
{
	for(int j=0;j<4;j++)
	{
	//	cout<<marks1[killer-1][j];
		marks3[k++] = marks1[killer-1][j];
		//cout<<"\t";
	}
//	cout<<"\n";
	break;
}
/*for(k=0; k<4; k++)
{
cout <<marks3[k];
cout<<"\t";
}*/
//cout<<"\n";
int jeans =select2;
k2=0;
while(jeans)
{
	for(int j=0;j<4;j++)
	{
		//cout<<marks2[jeans-1][j];
		marks4[k2++] = marks2[jeans-1][j];
		//cout<<"\t";
	}
	//cout<<"\n";
	break;
}
/*for(k2=0; k2<4; k2++)
{
cout <<marks4[k2];
cout<<"\t";
}*/
int count=0; int z=0;
for (int i=0; i<4; i++)
{
	for (int j=0; j<4; j++)
	{
		if (marks3[i]==marks4[j])
		{
			count+=1;
			z=marks3[i];
		}
	}
}
if(count==0)
cout<<"Case #"<<x+1<<": "<<"Volunteer cheated!"<<endl;
else if(count>1)
cout<<"Case #"<<x+1<<": "<<"Bad magician!"<<endl;
else
cout<<"Case #"<<x+1<<": "<<z<<endl;
}
return 0;
}

 
