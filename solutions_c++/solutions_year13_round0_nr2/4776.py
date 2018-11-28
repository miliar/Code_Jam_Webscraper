#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ofstream fout ("2.out");
ifstream fin ("2.in");

bool judge(int **a,int n,int m)
{
	
	int *row=new int[n];  //biggest in a row
	int *col=new int[m];  //biggest in a colum
	for (int i=0;i<n;i++)
	{
		int max=a[i][0];
		for (int j=1;j<m;j++)
		{
			if(max<a[i][j])
			{
				max=a[i][j];
			}
		}
		row[i]=max;
	}
	for (int i=0;i<m;i++)
	{
		int max=a[0][i];
		for (int j=1;j<n;j++)
		{
			if(max<a[j][i])
			{
				max=a[j][i];
			}
		}
		col[i]=max;
	}
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<m;j++)
		{
			if (a[i][j]<row[i]&&a[i][j]<col[j])
			{
				return false;
			}
		}
	}

	return true;










}


int main() {

	int t;
	fin>>t;
	int *n=new int[t];
	int *m=new int[t];
	for (int i=0;i<t;i++)
	{
		fin>>n[i]>>m[i];
		//cout<<n[i]<<m[i]<<endl;
		int **a=new int *[n[i]];
		for (int j=0;j<n[i];j++)
		{
			a[j]=new int[m[i]];
			for (int k=0;k<m[i];k++)
			{
				fin>>a[j][k];
				//cout<<a[j][k];
			}
			//cout<<endl;
		}
		fout<<"Case #"<<i+1<<": ";
		if (judge(a,n[i],m[i])==true)
		{
			fout<<" YES"<<endl;
		} 
		else
		{
			fout<<" NO"<<endl;
		}
	}







	//system("pause");
	return 0;
}