#include<iostream>
#include<cmath>
#include<vector>
#include<fstream>
using namespace std;
int palin(int n)
{
	int t=n,rev=0;
	while(t!=0)
	{
		rev=(rev*10)+(t%10);
		t/=10;
	}
	if(rev==n)
	return 1;
	else
	return 0;
}
int perfsq(int n)
{
	if(int(sqrt(n))*int(sqrt(n))==n)
	return 1;
	else
	return 0;
}
int main()
{
	ifstream fin("p3.in");
	ofstream fout("p3.out");
	int t;
	fin>>t;
	vector <int> ans;
	for(int i=0;i<t;i++)
	{
		int a,b,s=0;
		fin>>a>>b;
		for(int j=a;j<=b;j++)
		if((palin(j)==1)&&(perfsq(j)==1))
		{
			if(palin(int(sqrt(j)))==1)
			s++;
		}
		ans.push_back(s);
	}
	for(int i=0;i<ans.size();i++)
	fout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
	fin.close();
	fout.close();
	return 0;
}
