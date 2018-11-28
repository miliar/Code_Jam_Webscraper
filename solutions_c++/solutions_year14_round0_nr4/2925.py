#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

const int maxn=1000+10;

double a[maxn],b[maxn];
int t,tt,n,i,j,ans1,ans2;

ifstream fin("D-large.in");
ofstream fout("D.txt");



int main()
{
	fin>>t;
	for(tt=1;tt<=t;tt++)
	{
		fin>>n;
		for(i=0;i<n;i++)
			fin>>a[i];
		for(i=0;i<n;i++)
			fin>>b[i];

		sort(a,a+n);
		sort(b,b+n);

		ans1=0; i=0 ; j=0;
		while(i<n)
		{
			while(i<n && a[i]-b[j]<1e-6)
				i++;
			if (i<n)
			{
				ans1++;
				i++;
				j++;
			}
		}
		ans2=0; i=0; j=0;
		while(j<n)
		{
			while(j<n && a[i]-b[j]>1e-6)
				j++;
			if (j<n)
			{
				ans2++;
				i++;
				j++;
			}
		}

		fout<<"Case #"<<tt<<": "<<ans1<<" "<<n-ans2;
		
		
		fout<<endl;
	}
	return 0;
}
