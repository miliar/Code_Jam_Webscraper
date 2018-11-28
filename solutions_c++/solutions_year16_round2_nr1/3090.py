#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int T=t;
	while(t--)
	{
		string s;
		cin>>s;
		int n = s.length();
		int a[27];
		int x[n+1];
		int top=-1;
		for(int i=0;i<=26;i++)
		{
			a[i]=0;
		}
		for(int i=0;i<n;i++)
		{
			a[s[i]-'A']++;
		}

		int r = a['X'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 6;
		}
		a['S'-'A']-= r;
		a['I'-'A']-= r;
		a['X'-'A']-= r;

		r = a['Z'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 0;
		}
		a['Z'-'A']-= r;
		a['E'-'A']-= r;
		a['R'-'A']-= r;
		a['O'-'A']-= r;

		r = a['W'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 2;
		}
		a['T'-'A']-= r;
		a['W'-'A']-= r;
		a['O'-'A']-= r;

		r = a['G'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 8;
		}
		a['E'-'A']-= r;
		a['I'-'A']-= r;
		a['G'-'A']-= r;
		a['H'-'A']-= r;
		a['T'-'A']-= r;

		r = a['S'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 7;
		}
		a['S'-'A']-= r;
		a['E'-'A']-= r;
		a['V'-'A']-= r;
		a['E'-'A']-= r;
		a['N'-'A']-= r;

		r = a['V'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 5;
		}
		a['F'-'A']-= r;
		a['I'-'A']-= r;
		a['V'-'A']-= r;
		a['E'-'A']-= r;
		
		r = a['F'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 4;
		}
		a['F'-'A']-= r;
		a['O'-'A']-= r;
		a['U'-'A']-= r;
		a['R'-'A']-= r;
		
		r = a['O'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 1;
		}
		a['O'-'A']-= r;
		a['N'-'A']-= r;
		a['E'-'A']-= r;

		r = a['H'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 3;
		}
		a['T'-'A']-= r;
		a['H'-'A']-= r;
		a['R'-'A']-= r;
		a['E'-'A']-= r;
		a['E'-'A']-= r;
		
		r = a['E'-'A'];
		for(int i=0;i<r;i++)
		{
			x[++top] = 9;
		}
		a['N'-'A']-= r;
		a['I'-'A']-= r;
		a['N'-'A']-= r;
		a['E'-'A']-= r;
		
		

		sort(x,x+top+1);
		cout<<"CASE #"<<T-t<<": ";
		for(int i=0;i<top+1;i++)cout<<x[i];
		cout<<"\n";
	}
}