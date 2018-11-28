#include<iostream>
#include<fstream>
#include<algorithm>
#include<set>
using namespace std;
int main()
{
	int T;
	ifstream fin ("/home/kidd/A-small-attempt0.in", ios::in);
	ofstream fout ("/home/kidd/A-small-attempt0.out", ios::out);
	fin>>T;
	for(int it=1;it<=T;it++)
	{
		int i,j;
		set<int> s;
		set<int>::iterator its;
		set<int> ret;
		int n=4;
		int r,e;
		fin>>r;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				fin>>e;
				if(i!=r)
					continue;
				s.insert(e);
			}
		}
		fin>>r;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				fin>>e;
				if(i!=r)
					continue;
				its=s.find(e);
				if(its!=s.end())
					ret.insert(*its);
			}
		}
		fout<<"Case #"<<it<<": ";
		if(ret.size()==0)
			fout<<"Volunteer cheated!\n";
		else if(ret.size()>1)
			fout<<"Bad magician!\n";
		else
			fout<<*ret.begin()<<endl;
	}
}
