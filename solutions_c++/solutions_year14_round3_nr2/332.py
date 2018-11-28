#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <set>
#include <map>

using namespace std;
const long long p = 1000*1000*1000+7;
string result;
long long res;
char d[100];
int sz;
bool isResultValid()
{
	sz=0;
	d[sz++]= result[0];
	for (int i=1;i<result.size();i++)
	{
		if (result[i]!=result[i-1])
			d[sz++]=result[i];
	}
	int ms[26]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
	for (int i=0;i<sz;i++)
	{
		int c = d[i]-'a';
		ms[c]++;
		if (ms[c]>=2)
			return false;
	}

	return true;
}

int n;
vector<string> v;
bool used[11];
void dfs(int step)
{
	if(step==n)
	{
		if (isResultValid())
			res++;
		return ;
	}
	for (int i=0;i<n;i++)
	{
		if (used[i]==false)
		{
			used[i]=true;
			result+=v[i];
			dfs(step+1);
			result.erase(result.begin()+result.size()-v[i].size(), result.end());
			used[i]= false;
		}
	}
}
void go()
{
	cin>>n;
	v.resize(n);
	for(int i=0;i<n;i++)
		cin>>v[i];
	for (int i=0;i<n;i++)
		used[i]=0;
	res=0;
	dfs(0);
	cout<<res;
}
int main()
{	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			go();
		}
		cout<<"\n";
	}
	return 0;
}
