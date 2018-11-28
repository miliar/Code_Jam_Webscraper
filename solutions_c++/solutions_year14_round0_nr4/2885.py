#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;
int t,n,w=0,dw=0,temp2;
double na[2000],ke[2000],temp[2000];

int poske(double a)
{
	double max=2;
	int posx=-1;
	for(int j=0;j<n;j++)
	{
		if(ke[j]>a&&ke[j]<max)
		{
			max=ke[j];
			posx=j;
		}
	}
	return posx;
}
int min()
{
	double min=ke[0];
	int pos=0;
	for(int j=1;j<n;j++)
	{
		if(ke[j]<min)
		{
			min=ke[j];
			pos=j;
		}
	}
	return pos;
}
int check1(int j)
{
	int flag=-1;
	double burn=-1;
	for(int k=0;k<n;k++)
	{
		if(temp[k]<na[j]&&burn<temp[k])
		{
			burn=temp[k];
			flag=k;
		}
	}
	return flag;
		
}
int main()
{
	int fsd;
	ifstream fin ("C:\\file\\D-large.in");
	ofstream fout ("C:\\file\\D-large.out");
	fin>>t;
	for(int i = 0 ; i<t;i++)
	{
		fin>>n;
		w=0;
		dw=0;
		for(int j=0;j<n;j++)
			fin>>na[j];
		for(int j=0;j<n;j++)
		{
			fin>>ke[j];
			temp[j]=ke[j];
		}
		for(int j=0;j<n;j++)
		{
			fsd=poske(na[j]);
			if(fsd==-1)
			{
				fsd=min();
				w++;
			}
			ke[fsd]=20;
		}
		for(int j=0;j<n;j++)
		{
			temp2=check1(j);
			if(temp2!=-1)
			{
				dw++;
				temp[temp2]=20;
			}
		}
		fout<<"Case #"<<(i+1)<<": ";
		fout<<dw<<" "<<w;
		if((i+1)!=t)
			fout<<endl;
		
	}
	return 0;
}

