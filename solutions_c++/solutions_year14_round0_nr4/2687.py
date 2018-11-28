#include<iostream>
#include<fstream>
#include<algorithm>
#include<set>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<vector>
#include<cstring>
using namespace std;

int main()
{
	int T;
	ifstream fin ("/home/kidd/D-large.in", ios::in);
	ofstream fout ("/home/kidd/D-large.out", ios::out);
	fin>>T;
	for(int it=1;it<=T;it++)
	{
		vector<double> a;
		vector<double> b;
		int n;
		int i,j;
		int ra=0,rb=0;
		fin>>n;
		a.assign(n,0);
		b.assign(n,0);
		for(i=0;i<n;i++)
		{
			fin>>a[i];
		}
		for(i=0;i<n;i++)
		{
			fin>>b[i];
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		j=n-1;
		for(i=n-1;i>=0;i--)
		{
			while(j>=0&&a[i]<=b[j])
			{
				j--;
			}
			if(j>=0)
			{
				ra++;
				j--;
			}
			else
				break;
		}
		j=0;
		for(i=0;i<n;i++)
		{
			while(j<n&&a[i]>=b[j])
			{
				j++;
			}
			if(j<n)
			{
				rb++;
				j++;
			}
			else
				break;
		}
		fout<<"Case #"<<it<<": ";
		fout<<ra<<" "<<n-rb<<endl;
	}
}
