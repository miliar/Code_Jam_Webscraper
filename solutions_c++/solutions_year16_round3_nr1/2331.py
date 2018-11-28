#include<bits/stdc++.h>
using namespace std;
int main()
{
	ifstream f1("A-large.in");
	ofstream f2("A-ans2.txt");
	int t,x=1;
	f1>>t;
	while(t--)
	{
		f2<<"Case #"<<x++<<": ";
		int n;
		f1>>n;
		int a[n],sum=0,max=0;
		for(int i=0;i<n;i++)
		{
			f1>>a[i];
			sum+=a[i];
			if(a[i]>a[max])
				max=i;
		}
		while(1)
		{
			char ch=max+65;
			f2<<ch;
			a[max]--;
			sum--;
			for(int i=0;i<n;i++)
				if(a[i]>a[max])
					max=i;
			float d=(float)a[max]/sum;
			if(d>0.5||a[max]-1==1)
			{
				ch=max+65;
				f2<<ch;
				a[max]--;
				sum--;
			}
			f2<<" ";
			for(int i=0;i<n;i++)
				if(a[i]>a[max])
					max=i;
			if(a[max]==0)
				break;
		}f2<<'\n';
	}
}
