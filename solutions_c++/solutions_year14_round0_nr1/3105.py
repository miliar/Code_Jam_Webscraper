
#include<iostream>
using namespace std;
int main()
{

	int t;
	cin>>t;
	int rowo=0,rown = 0,count=0;
	int op;
	int old[4][4], suf[4][4];
	for(int i=0;i<t;i++)
	{
		cin>>rowo;
		for(int j = 0;j<4;j++)
		{
			for(int k = 0;k<4;k++)
			{
				cin>>old[j][k];
			}
		}
		cin>>rown;
		for(int j = 0;j<4;j++)
		{
			for(int k = 0;k<4;k++)
			{
				cin>>suf[j][k];
			}
		}
		for(int j=0;j<4;j++)
		{
			for(int k = 0;k<4;k++)
			{
				if(old[rowo-1][j] == suf[rown-1][k])
				{
					count++;
					op = old[rowo-1][j];
				}
			}
		}
		if(count == 0)
			cout<<"Case #"<<i+1<<":"<<" Volunteer cheated!"<<endl;
		else if(count > 1)
			cout<<"Case #"<<i+1<<":"<<" Bad magician!"<<endl;
		else if(count == 1)
		cout<<"Case #"<<i+1<<": "<<op<<endl;
		count = 0;
	}
	return 0;
}
