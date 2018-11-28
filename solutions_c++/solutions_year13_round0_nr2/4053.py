#include <iostream>
#include <string>
#include <vector>
using namespace std;

int lawn[101][101];
bool flag=true;
int cSize,rSize;

bool ifpattern(int temp,int i,int j)
{
	int col=0;
	int row=0;

	for(int c=0;c<cSize;c++)
	{
		if(lawn[i][c]<=temp)
			col++;
		else 
			break;
	}
	
	for(int r=0;r<rSize;r++)
	{
		if(lawn[r][j]<=temp)
			row++;
		else 
			break;
	}

	if(col == cSize || row == rSize) 
		return true;
    else 
		return false;

}



void main()
{

	freopen("B-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T=0;
	cin >> T;


	for(int t=1;t<=T;t++)
	{
		
		cin>>rSize;
		cin>>cSize;


		//adding values to array
		for(int i=0;i<rSize;i++)
		{
			for(int j=0;j<cSize;j++)
			{
				int temp;
				cin>>temp;
				lawn[i][j]=temp;
			}
		}

		flag=true;

		for(int i=0;i<rSize;i++)
		{
			for(int j=0;j<cSize;j++)
			{

				int temp = lawn[i][j];
				flag= ifpattern(temp,i,j);

				if(flag==false)
					break;

			}

				if(flag==false)
					break;
		}

		if(flag==true)
		cout<<"Case #"<<t<<": "<<"YES"<<endl;
		else
		cout<<"Case #"<<t<<": "<<"NO"<<endl;

	}

}