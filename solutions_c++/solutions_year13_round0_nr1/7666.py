#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int test;
	cin>>test;
	for(int t=0;t<test;t++)
	{
		char a[4][4];
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
	bool f1=false,f2=false;
	for(int i=0;i<4;i++)
	{
		int count_x=0,count_t=0,count_o=0;
		for(int j=0;j<4;j++)
		{
			if(a[i][j]=='X')
			{
				count_x++;
			}
			else if(a[i][j]=='T')
			{
				count_t++;
			}
			if(a[i][j]=='O')
			{
				count_o++;
			}
		}
		if(count_x==3&&count_t==1)
		{
			cout<<"Case #"<<t+1<<":"<<" "<<"X won"<<endl;
			f1=true;
			break;
		}
		else if(count_o==3&&count_t==1)
		{
			cout<<"Case #"<<t+1<<":"<<" "<<"O won"<<endl;
			f1=true;
			break;
		}
	}
	if(f1==false)
	{
		for(int i=0;i<4;i++)
	{
		int count_x=0,count_t=0,count_o=0;
		for(int j=0;j<4;j++)
		{
			if(a[j][i]=='X')
			{
				count_x++;
			}
			else if(a[j][i]=='T')
			{
				count_t++;
			}
			if(a[j][i]=='O')
			{
				count_o++;
			}
		}
		if((count_x==3&&count_t==1) || (count_x==4))
		{
			cout<<"Case #"<<t+1<<":"<<" "<<"X won"<<endl;
			f1=true;
			break;
		}
		else if((count_o==3&&count_t==1)||count_o==4)
		{
			cout<<"Case #"<<t+1<<":"<<" "<<"O won"<<endl;
			f1=true;
			break;
		}
		}
	}
	if(f1==false)
	{
		int count_x=0,count_t=0,count_o=0;
		
		for(int i=0;i<4;i++)
		{
			
			if(a[i][i]=='X')
				count_x++;
			if(a[i][i]=='O')
				count_o++;
			if(a[i][i]=='T')
				count_t++;
		}
		if((count_x==3&&count_t==1)||count_x==4)
		{
			cout<<"Case #"<<t+1<<":"<<" "<<"X won"<<endl;
			f1=true;
			
		}
		else if((count_o==3&&count_t==1)||count_o==4)
		{
			cout<<"Case #"<<t+1<<":"<<" "<<"O won"<<endl;
			f1=true;
		}
		
	}
	if(f1==false)
	{
			int count_x=0,count_t=0,count_o=0;
	
		for(int i=0,j=3;i<4,j>=0;i++,j--)
		{
			if(a[i][j]=='X')
				count_x++;
			if(a[i][j]=='O')
				count_o++;
			if(a[i][j]=='T')
				count_t++;
		}
		if((count_x==3&&count_t==1)||count_x==4)
		{
			cout<<"Case #"<<t+1<<":"<<" "<<"X won"<<endl;
			f1=true;
			
		}
		else if((count_o==3&&count_t==1)||count_o==4)
		{
			cout<<"Case #"<<t+1<<":"<<" "<<"O won"<<endl;
			f1=true;
		}
	}
	if(f1==false)
	{
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i][j]=='.')
				{
					cout<<"Case #"<<t+1<<":"<<" "<<"Game has not completed"<<endl;
					f1=true;
					break;
				}
			}
		if(f1==true)
			break;
		}
	}
	if(f1==false)
	{
		cout<<"Case #"<<t+1<<":"<<" "<<"Draw"<<endl;
	}
	}
	
	return 0;
}