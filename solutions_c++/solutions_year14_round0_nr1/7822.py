#include <iostream>
using namespace std;

int t1[5][5];
int t2[5][5];
int x1, x2, kejsy;
	
	
void load(int t[5][5])
{
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4;j++)
		cin>>t[i][j];
	}
}


int trick()
{
	cin>>x1;
	load(t1);
	cin>>x2;
	load(t2);
	int fnd=0;
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if(t1[x1-1][i]==t2[x2-1][j] && fnd!=0)
			{
				return -1;
			}
			if(t1[x1-1][i]==t2[x2-1][j] && fnd==0)
			{
				fnd=t1[x1-1][i];
			}
		}
	}
	return fnd;
}
int main ()
{
	cin >> kejsy;
	for(int i=0; i<kejsy; i++)
	{
		cout << "Case #"<<i+1<<": ";
		switch(int j=trick())
		{
			case -1: cout << "Bad magician!";
			break;
			case 0: cout << "Volunteer cheated!";
			break;
			default: cout << j;
		}
		cout << endl;
	}
}
