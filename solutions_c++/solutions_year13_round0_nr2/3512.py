#include<iostream>
#include<fstream>
#include<string>

using namespace std;

ifstream fin("data.in");
ofstream fout("result.out");

int a[100][100];
int b[100][100];

int main()
{
	int t;
	fin>>t;
	for(int case_no=1;case_no<=t;++case_no)
	{
		fout<<"Case #"<<case_no<<": ";
		int n,m;
		fin>>n>>m;
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
			{
				fin>>a[i][j];
				b[i][j]=100;
			}

		for(int i=0;i<n;++i)
		{
			int max_h=1;
			for(int j=0;j<m;++j)
				max_h=max(max_h,a[i][j]);
			for(int j=0;j<m;++j)
				b[i][j]=min(b[i][j],max_h);
		}

		for(int j=0;j<m;++j)
		{
			int max_h=1;
			for(int i=0;i<n;++i)
				max_h=max(max_h,a[i][j]);
			for(int i=0;i<n;++i)
				b[i][j]=min(b[i][j],max_h);
		}

		bool ok=true;
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				if(a[i][j]!=b[i][j])
				{
					ok=false;
					break;
				}
		fout<<(ok?"YES":"NO")<<endl;
	}
}