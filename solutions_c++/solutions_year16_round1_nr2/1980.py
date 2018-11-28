#include<bits/stdc++.h>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
	ifstream in("B-large.in");
	ofstream out("output_large.txt");
	int t;
	in>>t;
	int m=t;
	while(t--)
	{
		int n;
		in>>n;
		int a[2501]={0};
		int x,b[n];
		for(int i=0;i<2*n-1;i++)
		{
			for(int j=0;j<n;j++)
			{
				in>>x;
				a[x]++;
			}			
		}
		int j=0;
		for(int i=0;i<2501;i++)
		{
			if(a[i]%2!=0)
			{
				b[j++]=i;
			}
		}
		sort(b,b+n);
		for(int i=0;i<n;i++)
		cout<<b[i]<<" ";
		//cout<<"aayush";
		//cout<<a<<"\n";
		out<<"Case #"<<m-t<<": ";
		for(int i=0;i<n;i++)
		out<<b[i]<<" ";
		out<<"\n";
	}
}
