#include<bits/stdc++.h>
using namespace std;
int main()
{
	ifstream file1("B-large.in");
	ofstream file2("file2.txt");
	int t;
	file1>>t;
	for(int j=0;j<t;j++)
	{
		int n;
		file1>>n;
		n=(2*n-1)*n;
		int a[2500];
		for(int i=0;i<2500;i++) a[i]=0;
		for(int i=0;i<n;i++) 
		{
			int x;
			file1>>x;
			a[x-1]++;
		}
		list<int> ans;
		int k=0;
		for(int i=0;i<2500;i++) if(a[i]%2==1) ans.push_back(i+1);
		ans.sort();
		file2<<"Case #"<<j+1<<": ";
		for(list<int>::iterator i=ans.begin();i!=ans.end();i++) file2<<*i<<" ";
		file2<<endl;
	}
}
