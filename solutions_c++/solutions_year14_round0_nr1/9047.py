//#include<iostream>
#include<fstream>
using namespace std;
int deck1[4][4];
int deck2[4][4];
ifstream cin;
ofstream cout;
int main()
{
	cin.open("A-small-attempt0.in");
	cout.open("hello");
	int T, choice1,choice2;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cin>>choice1;

		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>deck1[j][k];
			}
		}
		cin>>choice2;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>deck2[j][k];
			}
		}
		int count=0;
		int sol=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(deck1[choice1-1][j]==deck2[choice2-1][k])
				{
					sol=deck1[choice1-1][j];
					count++;
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(count==0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		if(count==1)
		{
			cout<<sol<<endl;
		}
		if(count>1)
		{
			cout<<"Bad magician!"<<endl;
		}
	}
	cin.close();
	cout.close();
	return 0;
}