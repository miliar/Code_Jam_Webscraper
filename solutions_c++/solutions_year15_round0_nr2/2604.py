#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
using namespace std;
int best;
vector<int> num;
int max(vector<int> &a)
{
	int i,ans=a[0];
	for (i=1;i<a.size();i++)
	{
		if (ans<a[i])
			ans=a[i];
	}
	return ans;
}
void dfs(vector<int> a,int b)
{

	if (b>=best) return;
	int i,j;
	int tmp=max(a);
	if (tmp+b<best)
	{
		best=tmp+b;
		cout << best;
	}
	sort(a.begin(),a.end());
	a.push_back(0);
	int l=a.size();
	tmp=a[l-2];
	for (i=1;i<=tmp/2;i++)
	{
		a[l-2]=i;
		a[l-1]=tmp-i;
		dfs(a,b+1);
	}
}
int main()
{
	ifstream fin("3.txt");
	ofstream fout("5.txt");
	int t;
	int i,j,n,tmp;
	int now;	
	fin >> t;

	for (i=0;i<t;i++)
	{
		fin >> n;
		num.resize(n);
		for (j=0;j<n;j++)
		{
			fin>>num[j];
		}
		best=max(num);
		dfs(num,0);
		fout << "Case #"<<i+1<<": "<<best << endl;
		cout << "Case #"<<i+1<<": "<<best << endl;
	}
	return 0;
}