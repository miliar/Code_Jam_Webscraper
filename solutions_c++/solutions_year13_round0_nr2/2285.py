#include<iostream>
#include<cmath>
#include <cstdlib>
#include<fstream>
#include <cstring>
#include<string>
#include<algorithm>
using namespace std;
using std::ofstream;

int a[100][100]={-1};
int N,M;

bool addCol(int c, int h)
{
	bool ans =true;
	for(int i=0;i<N;i++)
	{
		a[i][c]+=h;
		if(a[i][c]>100)
			ans=false;
	}
	return ans;
}

bool addRow(int r, int h)
{
	bool ans =true;
	for(int i=0;i<M;i++)
	{
		a[r][i]+=h;
		if(a[r][i]>100)
			ans=false;
	}
	return ans;
}

bool checkCol(int x, int y, int n)
{
	bool up =false, down=false;
	for(int i=0;i<x;i++)
	{
		if(a[i][y]>n)
			up= true;
	}
	for(int i=x+1;i<N;i++)
	{
		if(a[i][y]>n)
			down =true;
	}
	if(up || down)
		return true;
	return false;
}

bool checkRow(int x, int y, int n)
{
	bool left =false, right =false;
	for(int i=0;i<y;i++)
	{
		if(a[x][i]>n)
			left=true;
	}
	for(int i=y+1;i<M;i++)
	{
		if(a[x][i]>n)
			right= true;
	}
	if(left || right)
		return true;
	return false;
}

int main()
{
	ofstream out;
//	out.open("output.txt");
	int maxR[100]={-1}, maxC[100]={-1};

	int T;
	string ans="YES";
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		ans="YES";
		cin>>N>>M;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				cin>>a[i][j];
				if(a[i][j]>maxR[i])
					maxR[i]=a[i][j];
				if(a[i][j]>maxC[j])
					maxC[j]=a[i][j];
			}

		}
		cout<<"Case #"<<t<<": ";
		//out<<"Case #"<<t<<": ";
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
				if(a[i][j]!=maxR[i] && a[i][j]!=maxC[j] )
				{
					if(!((i==0 && j==0) || (i==0 && j ==M-1) || (i==N-1 && j==0) || (i==N-1 && j==M-1)))
					{
						if(checkRow(i,j,a[i][j]) && checkCol(i,j,a[i][j]))
						{
								ans="NO";
								break;
						}
					}
					else
					{
						bool col=false, row=false;
						//col
						for(int k=0;k<N;k++)
							{
								if(a[k][j]>a[i][j])
									col= true;
							}
						for(int k=0;k<M;k++)
							{
								if(a[i][k]>a[i][j])
									row=true;
							}
						if(col && row)
						{
								ans="NO";
								break;
						}
					}
						
				}
		}
		cout<<ans<<"\n";
	//	out<<ans<<"\n";

		
		
	}


	
		

	//out.close();
		
	return(0);
}