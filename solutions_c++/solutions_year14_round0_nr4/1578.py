#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main(void)
{
	ifstream fin;
	fin.open("D-large.in");
	ofstream fout;
	fout.open("D-large.out");
	int t;
	fin>>t;
	double a[1000];
	double b[1000];
	for(int i=0;i<t;i++)
	{
		//cin
		int n;
		int ra=0;
		int rb=0;
		fin>>n;
		for(int j=0;j<n;j++)
		{
			fin>>a[j];
		}
		for(int j=0;j<n;j++)
		{
			fin>>b[j];
		}
		sort(a,a+n);
		sort(b,b+n);
		
		if(n==1 && a[0]>b[0]) {ra=1;rb=1;}
		
		int k=0;
		for(int j=0;j<n;j++)
		{
			while(a[k]<b[j])
			{
				k++;
				if(k==n) break;
			}
			if(k==n-1) {ra=j+1;break;}
			if(k==n) {ra=j;break;}
			if(k<n-1) {k++;}
		}
		if(a[0]>b[n-1]) ra=n;
		k=0;
		for(int j=0;j<n;j++)
		{
			while(b[k]<a[j])
			{
				k++;
				if(k==n) break;
			}
			if(k==n-1) {rb=n-j-1;break;}
			if(k==n) {rb=n-j;break;}
			if(k<n-1) {k++;}
		}
		
		fout<<"Case #"<<i+1<<": ";
		fout<<ra<<" "<<rb<<endl;
	}
	return 0;
}