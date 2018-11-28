#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int main()
{	
	
	int test_cases;
	cin>>test_cases;
	string L[4];
	stringstream ss;
	bool flag=false;
	char temp;
	
	
	for(int k=1;k<test_cases+1;k++)
	{
		cin>>L[0];
		cin>>L[1];
		cin>>L[2];
		cin>>L[3];
		for(int j=0;j<4;j++)
		{
			temp=L[j][0];
			if(!flag)
			if(temp!='.')
			{
			flag=true;
				for(int i=1;i<4;i++)
				{
				if(!(temp==L[j][i]||L[j][i]=='T'))
					{
					flag=false;
					break;
					}
				}
			
			
			if(flag)
			{
				ss<<"Case #"<<k<<": "<<temp<<" won\n";
				
			}}
		}
		if(!flag)
		for(int j=0;j<4;j++)
		{
			temp=L[0][j];
			if(!flag)
			if(temp!='.')
			{
			flag=true;
				for(int i=1;i<4;i++)
				{
				if(!(temp==L[i][j]||L[i][j]=='T'))
					{
					flag=false;
					break;
					}
				}
			
			
			if(flag)
			{
				ss<<"Case #"<<k<<": "<<temp<<" won\n";
				
			}
			}
		}
		temp=L[0][0];
		if(!flag)
		if(temp!='.')
		{
			flag=true;
			for(int i=1;i<4;i++)
			{
				if(!(temp==L[i][i]||L[i][i]=='T'))
				{
					flag=false;
					break;
				}
			}
			if(flag)
			{
				ss<<"Case #"<<k<<": "<<temp<<" won\n";
				
			}
		}
		temp=L[0][3];
		if(!flag)
		if(temp!='.')
		{
			flag=true;
			for(int i=1;i<4;i++)
			{
				if(!(temp==L[i][3-i]||L[i][3-i]=='T'))
				{
					flag=false;
					break;
				}
			}
			if(flag)
			{
				ss<<"Case #"<<k<<": "<<temp<<" won\n";
				
			}
		}
		if(!flag)
		{
		
		bool flag2=false;
		for(int h=0;h<4;h++)
		{
		for(int g=0;g<4; g++)
		flag2=flag2||L[h][g]=='.';
		}
		if(!flag2)
		ss<<"Case #"<<k<<": Draw\n";
		else
		ss<<"Case #"<<k<<": Game has not completed\n";
		}
		flag=false;
		
	}
	
	
	string s=ss.str();
	cout<<s;
}
		
			
	
