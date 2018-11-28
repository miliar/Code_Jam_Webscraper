#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int test(vector <vector <int> > A,int r,int c)
{
	int a=0,b=0;
	for(int i=0;i<A.size();i++)
	if(A[i][c]>A[r][c])
	{
		a=1;
		break;
	}
	for(int i=0;i<A[r].size();i++)
	if(A[r][i]>A[r][c])
	{
		b=1;
		break;
	}
	if((a==1)&&(b==1))
	return 0;
	else
	return 1;
}
int main()
{
	ifstream fin("p2.in");
	ofstream fout("p2.out");
	int t;
	vector <int> ans;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		int n,m,x,f=0;
		vector < vector <int> > A;
		vector <int> B;
		fin>>n>>m;
		for(int j=0;j<n;j++)
		{
			A.push_back(B);
			for(int k=0;k<m;k++)
			{
				fin>>x;
				A[j].push_back(x);
			}
		}
		for(int j=0;j<n;j++)
		{
			B.clear();
			x=0;
			for(int k=1;k<m;k++)
			if(A[j][k]<A[j][x])
			x=k;
			for(int k=0;k<m;k++)
			if(A[j][k]==A[j][x])
			B.push_back(k);
			for(int k=0;k<B.size();k++)
			{
				if(test(A,j,B[k])==0)
				{
					f=1;
					break;
				}
			}
			if(f==1)
			break;
		}
		if(f==1)
		ans.push_back(0);
		else
		ans.push_back(1);
	}
	for(int i=0;i<ans.size();i++)
	{
		fout<<"Case #"<<i+1<<":";
		if(ans[i]==0)
		fout<<" NO\n";
		else
		fout<<" YES\n";
	}
	fin.close();
	fout.close();
	return 0;
}
