#include<iostream>
using namespace std;
int main()
{
	int t,flag,ite=1;
	cin>>t;
	while(t--)
	{
		cin>>val1;
		flag=1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a[i][j];
		cin>>val2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>b[i][j];
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i][val1]==b[j][val2])
				{
					count++;
					if(count==1)
					{
						val=a[i][val1];
						flag=1;
					}
					if(count>1)
						flag=0;
				}
			}
		}
		if(count==1)
			cout<<"Case #<<ite<<": "<<val<<endl;
		else if(count==0)
			cout<<"Case #<<ite<<": "<<"Volunteer cheated!"<<endl;
		else
			cout<<"Case #<<ite<<": "<<"Bad magician!"<<endl;
		ite++;
	}
}