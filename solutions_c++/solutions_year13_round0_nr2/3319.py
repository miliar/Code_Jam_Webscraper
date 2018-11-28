#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int N;
	fin>>N;
	int num[101][101];
	for(int i=0;i<N;i++)
	{
		memset(num,0,sizeof(num));
		int m,n;
		fin>>m>>n;
		for(int j=0;j<m;j++)
		{
			for(int k=0;k<n;k++)
			{
				fin>>num[j][k];
			}
		}
		bool flag=true;
		for(int j=0;j<m;j++)
		{
			for(int k=0;k<n;k++)
			{
				int count=0;
				for(int l=0;l<m;l++)
				{
					if(num[j][k]<num[l][k])
					{
						count++;
						break;
					}
				}
				for(int l=0;l<n;l++)
				{
					if(num[j][k]<num[j][l])
					{
						count++;
						break;
					}
				}
				if(count>=2)
				{
					flag=false;
					goto A;
				}
			}
		}
A:if(flag)
  {
	  fout<<"Case #"<<i+1<<": YES"<<endl;
  }
  else
  {
	  fout<<"Case #"<<i+1<<": NO"<<endl;
  }
	}

	return 0;
}