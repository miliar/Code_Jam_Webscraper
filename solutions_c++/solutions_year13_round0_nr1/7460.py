#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<string>
#include<cstring>
#include<vector>
using namespace std;

vector<string> vec;
int D2;
int D1;
int D3;
int D4;
int R1[4];
int Temp[4];
int C1[4];
int R2[4];
int C2[4];

int main()
{
	int t;
	cin >> t;
	string inp;
	for(int i=1;i<=t;i++)
	{
		vec.clear();
	for(int j=0;j<4;j++)
	{
		cin>>inp;
		vec.push_back(inp);
	}
		int dc=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(vec[j][k]=='.')
				{
					dc=1;
					break;
				}
			}
			if(dc==1)
				break;
		}
		for(int j=0;j<4;j++)
		{
			if(vec[j][3]=='X' || vec[j][3]=='T')
				Temp[3]=1;
			else
				Temp[3]=0;


			for(int k=2;k>=0;k--)
			{
				if(vec[j][k]=='X' || vec[j][k]=='T')
				{
					Temp[k]=Temp[k+1]+1;
				}
				else
					Temp[k]=0;
			}
			R1[j]=Temp[0];
		}

		for(int j=0;j<4;j++)
		{
			if(vec[0][j]=='X' || vec[0][j]=='T')
				Temp[0]=1;
			else
				Temp[0]=0;


			for(int k=1;k<=3;k++)
			{
				if(vec[k][j]=='X' || vec[k][j]=='T')
				{
					Temp[k]=Temp[k-1]+1;
				}
				else
					Temp[k]=0;
			}
			C1[j]=Temp[3];
		}
		D1=0;
		D2=0;
		for(int j=0;j<4;j++)
		{
			if(vec[j][j]=='X' || vec[j][j]=='T')
				D1+=1;
			if(vec[j][3-j]=='X' || vec[j][3-j]=='T')
				D2+=1;
		}
		int r1=0,c1=0;
		for(int j=0;j<4;j++)
		{
			if(R1[j]==4)
				r1=1;
			if(C1[j]==4)
				c1=1;
		}

		for(int j=0;j<4;j++)
		{
			if(vec[j][3]=='O' || vec[j][3]=='T')
				Temp[3]=1;
			else
				Temp[3]=0;


			for(int k=2;k>=0;k--)
			{
				if(vec[j][k]=='O' || vec[j][k]=='T')
				{
					Temp[k]=Temp[k+1]+1;
				}
				else
					Temp[k]=0;
			}
			R2[j]=Temp[0];
		}

		for(int j=0;j<4;j++)
		{
			if(vec[0][j]=='O' || vec[0][j]=='T')
				Temp[0]=1;
			else
				Temp[0]=0;


			for(int k=1;k<=3;k++)
			{
				if(vec[k][j]=='O' || vec[k][j]=='T')
				{
					Temp[k]=Temp[k-1]+1;
				}
				else
					Temp[k]=0;
			}
			C2[j]=Temp[3];
		}
		D3=0;
		D4=0;
		for(int j=0;j<4;j++)
		{
			if(vec[j][j]=='O' || vec[j][j]=='T')
				D3+=1;
			if(vec[j][3-j]=='O' || vec[j][3-j]=='T')
				D4+=1;
		}
		int r2=0,c2=0;
		for(int j=0;j<4;j++)
		{
			if(R2[j]==4)
				r2=1;
			if(C2[j]==4)
				c2=1;
		}
		if(r1||c1||D1==4 ||D2==4)
		{
			cout<<"Case #"<<i<<": X won\n";
		}
		else
		{
			if(r2 || c2 || D3==4 || D4==4)
				cout<<"Case #"<<i<<": O won\n";
			else
			{
				if(dc==1)
				{
					cout<<"Case #"<<i<<": Game has not completed\n";
				}
				else
					cout<<"Case #"<<i<<": Draw\n";
			}
		}
	}
		return 0;
}
