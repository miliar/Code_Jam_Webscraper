#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

int solve(vector<double> a,vector<double> b)
{
	int ret=0;
	int k=0;
	for(int i=0;i!=b.size();++i)
	{
		if(b[i]>a[k])
		{
			ret++;
			k++;
		}
	}
	return ret;
}

int main()
{
	ifstream f1("D-large.in");
	ofstream f2("out.txt");
	int T;
	f1>>T;
	for(int tt=0;tt!=T;++tt)
	{
		f2<<"Case #"<<tt+1<<": ";
		int N;
		f1>>N;
		vector<double> a,b;
		for(int i=0;i!=N;++i)
		{
			double temp;
			f1>>temp;
			a.push_back(temp);
		}
		for(int i=0;i!=N;++i)
		{
			double temp;
			f1>>temp;
			b.push_back(temp);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		int ans1=solve(a,b);
		int ans2=solve(b,a);
		f2<<ans2<<" "<<N-ans1<<endl;
	}
	return 1;
}