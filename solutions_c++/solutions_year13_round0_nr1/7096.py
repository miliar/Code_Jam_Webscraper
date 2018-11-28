#include <iostream>
#include <string>
using namespace std;
int main()
{
	int number;
	bool flag,dot;
	char var;
	string blank;
	char winner;
	cin>>number;
	string a[number][4];
	getline(cin,blank);
	for(int i=0; i<number; i++)
	{   
		for(int j=0;j<4;j++)
		{
			getline(cin,a[i][j]);
			for(int k=0;k<4;k++)
			{
				if(a[i][j].at(k)=='.')
				{
					dot=true;
				}
			}
		}
		getline(cin,blank);
	}
	for(int k=0;k<number;k++)
	{
		winner='N';
		dot=false;
		for(int m=0;m<2;m++)
		{
			if(m==0)
			{
				var='X';
			}
			else
			{
				var='O';
			}
			for(int i=0;i<4;i++)
			{
				flag=true;
				
					for(int j=0;j<4;j++)
					{ 
						if(flag)
						{	
							if((a[k][i].at(j)=='T')||a[k][i].at(j)==var)
							{
								
								if(j==3)
								{
									winner=var;
									goto done;
								}
							}
							else
							{
								flag=false;
							
							}
						}
					}			
			}
			for(int j=0;j<4;j++)
			{
				flag=true;
				for(int i=0;i<4;i++)
				{
					if(flag)
					{
						if((a[k][i].at(j)=='T')||a[k][i].at(j)==var)
						{
							flag=true;
							if(i==3)
							{
								winner=var;
								goto done;
							}
						}
						else
						{
							flag=false;
							
						}
					}
				}	
			}
			for(int i=0;i<4;i++)
			{
				if(a[k][i].at(i)=='T'||a[k][i].at(i)==var)
				{
					if(i==3)
					{
						winner=var;
						goto done;
					}
					
				}
				else
				{
					break;
				}
			}
			for(int i=0;i<4;i++)
			{
				if(a[k][i].at(3-i)=='T'||a[k][i].at(3-i)==var)
				{
					if(i==3)
					{
						winner=var;
						goto done;
					}
				}
				else
				{
					break;
				}
			}
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[k][i].at(j)=='.')
				{
					dot=true;
				}
			}
		}
		
		done:if(winner!='N')
		{
			cout<<"Case #"<<k+1<<": "<<winner<<" won \n";
		}
		else if(winner=='N'&&dot==true)
		{
			cout<<"Case #"<<k+1<<": Game has not completed \n";
		}
		else
		{
			cout<<"Case #"<<k+1<<": Draw \n";
		}
		
		
	}
	return 0;
}
