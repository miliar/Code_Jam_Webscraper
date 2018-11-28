#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
bool myfunction (int i,int j) { return (i<j); }

struct myclass {
  bool operator() (int i,int j) { return (i<j);}
} myobject;

int main()
{
	long long t1,n;
	ifstream inp("input.txt");
	ofstream out("output.txt");
	inp>>t1;
	for(long long it=1;it<=t1;it++)
	{
		int n;
		inp>>n;
		int a[100][100];
		vector<int> ans;
		map<int,int> mymap;
		for(int i=0;i<2*n-1;i++)
		{
			for(int j=0;j<n;j++)
			{
				inp>>a[i][j];
				if(mymap.find(a[i][j])!=mymap.end())
				{
					mymap[a[i][j]]++;
				}
				else
					mymap[a[i][j]]=1;
			}
		}
		map<int,int>::iterator i;
		for(i=mymap.begin();i!=mymap.end();i++)
		{
			if(i->second%2!=0)
				ans.push_back(i->first);
		}
		sort(ans.begin(),ans.end(),myobject);
		out<<"Case #"<<it<<": ";
		for(int i=0;i<ans.size();i++)
		{
			out<<ans[i]<<" ";
		}
		out<<endl;	
	}
	out.close();
}
