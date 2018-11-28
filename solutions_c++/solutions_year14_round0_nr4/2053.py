#include <iostream>
#include <fstream>
#include <algorithm>
#include <deque>
using namespace std;
double a[1000],b[1000];
int main()
{
	ifstream fin("D-large.in");
	ofstream fout("D-large.out");
	int t,k,n,i,j,c,ans,dans;
	fin>>t;
	for (k=1;k<=t;k++)
	{
		fin>>n;
		for (i=0;i<n;i++) fin>>a[i];
		sort(a,a+n);
		for (i=0;i<n;i++) fin>>b[i];
		sort(b,b+n);
		deque<double> d;
		for (i=0;i<n;i++) d.push_front(b[i]);
		ans=0;
		for (i=n-1;i>=0;i--)
			if (a[i]>d.front())
			{
				d.pop_back();
				ans++;
			}
			else d.pop_front();
		dans=n;i=j=c=0;
		while (i<n&&j<n)
		{
			if (a[i]<b[j])
			{
				if (c) c--;
				else dans--;
				i++;
			}
			else {c++;j++;}
		}
		fout<<"Case #"<<k<<": "<<dans<<" "<<ans<<endl;
	}
	return 0;
}