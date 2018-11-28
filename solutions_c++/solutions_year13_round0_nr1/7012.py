#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int copy=t;
	while(t--)
	{
		char a[4][4];		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a[i][j];
		
		char win='.';
		int i,j;
		//row
		for(i=0;i<4;i++)
		{
			char temp;
			if(a[i][0]!='T')
				temp=a[i][0];
			else
				temp=a[i][1];
			for(j=1;j<4;j++)
			{
				if(a[i][j]=='T')
					continue;
				if(a[i][j]!=temp)
					break;
			}
			if(j==4&&temp!='.')
				win=temp;
		}
		if(win=='.')
		{
			for(i=0;i<4;i++)
			{	
				char temp;
				if(a[0][i]!='T')
					temp=a[0][i];
				else
					temp=a[1][i];
				for(j=1;j<4;j++)
				{
					if(a[j][i]=='T')
						continue;
					if(a[j][i]!=temp)
						break;
				}
				if(j==4&&temp!='.')
					win=temp;
			}
		}
		if(win=='.')
		{
			char temp;
				if(a[0][0]!='T')
					temp=a[0][0];
				else
					temp=a[1][1];
			for(i=1;i<4;i++)
			{	
					if(a[i][i]=='T')
						continue;
					if(a[i][i]!=temp)
						break;
			}
			if(i==4&&temp!='.')
					win=temp;
		}
		if(win=='.')
		{
			char temp;
				if(a[0][3]!='T')
					temp=a[0][3];
				else
					temp=a[1][2];
			for(i=1;i<4;i++)
			{	
					if(a[i][3-i]=='T')
						continue;
					if(a[i][3-i]!=temp)
						break;
					
			}
			if(i==4&&temp!='.')
					win=temp;
		}
		cout<<"Case #"<<copy-t<<": ";
		if(win!='.')
			cout<<win<<" won";
		else
		{
			for(int i=0;i<16;i++)
			{
				if(a[i/4][i%4]=='.')
					win='n';
			}
			if(win=='n')
				cout<<"Game has not completed";
			else
				cout<<"Draw";
		}
		cout<<endl;
	}
}
