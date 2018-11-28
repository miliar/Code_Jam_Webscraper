#include<iostream>
using namespace std;
int main()
{
	int t,n,m,num=1,i,j,rowmin,k,xx;
	bool checkColumn,possible;
	int lawn[105][105];
	cin>>t;
	while(num<=t)
	{
		cin>>n>>m;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				cin>>lawn[i][j];
			}
		}
		for(i=0;i<n;i++)
		{
			//cout<<"For row :"<<i<<endl;
			rowmin = 105;
			checkColumn = false;
			possible = true;
			for(j=0;j<m;j++)
			{
				if(rowmin != lawn[i][j] && j!=0)
				checkColumn = true;
				
				if(rowmin>lawn[i][j])
				{
					rowmin = lawn[i][j];
				}
			}
			//cout<<"rowmin :: "<<rowmin<<endl;
			if(checkColumn == true)
			{
				//cout<<"NEED TO CHECK\n";
					for(j=0;j<m;j++)
					{
						if(lawn[i][j] == rowmin)
						{	
							//cout<<"the column is ::"<<j<<endl;	
							for(xx=0;xx<n;xx++)
							{
								if(lawn[xx][j] > rowmin)
								{
									possible = false;
									break;
								}
							}
						}
						if(possible == false)
							break;
					}
			}
			if(possible == false)
				break;
		}
		if(possible == true)
		{
			cout<<"Case #"<<num<<": YES"<<endl;
		}
		else
			cout<<"Case #"<<num<<": NO"<<endl;
		num++;
	}
	return 0;
}
