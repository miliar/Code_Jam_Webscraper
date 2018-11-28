#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<sstream>
#include<math.h>
#include<algorithm>
using namespace std;
long infinity = 1000*1000*1000;
long motes(vector<int> & sizes, int n, int a, int i)
{
	long x = infinity, y = infinity;
	if(i==n) return 0;
	//cout<<"i = "<<i<<endl;
	if(a>sizes[i]) return motes(sizes, n, a+sizes[i], i+1);
	if(a!=1)
		x = motes(sizes, n, 2*a - 1, i) + 1;
	y = motes(sizes, n, a, i + 1) + 1;
	return min(x,y);
}
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("A-small-attempt0.in");
	cout.open("motes_small.txt");
	int t,a,n,temp;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		vector<int> sizes;
		cin>>a>>n;
		for(int j=0;j<n;j++)
		{
			cin>>temp;
			sizes.push_back(temp);
		}
		sort(sizes.begin(),sizes.end());
		cout<<"Case #"<<i+1<<": "<<motes(sizes, n, a, 0)<<endl;
	}
}
