#include<fstream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");
	int t;
	in>>t;
	int m=t;
	while(t--)
	{
		string s;
		string ans="";
		int b[10]={0};
		in>>s;
		char a[26]={0};
		int l=s.length();
		for(int i=0;i<l;i++)
		{
			a[s[i]-65]++;
		}
		if(a['Z'-65]>0)
		{
			a['E'-65]-=a['Z'-65];
			a['R'-65]-=a['Z'-65];
			a['O'-65]-=a['Z'-65];
			b[0]=a['Z'-65];
		}
		if(a['W'-65]>0)
		{
			a['T'-65]-=a['W'-65];
			a['O'-65]-=a['W'-65];
			b[2]=a['W'-65];
		}
		if(a['U'-65]>0)
		{
			a['F'-65]-=a['U'-65];
			a['O'-65]-=a['U'-65];
			a['R'-65]-=a['U'-65];
			b[4]=a['U'-65];
		}
		if(a['X'-65]>0)
		{
			a['S'-65]-=a['X'-65];
			a['I'-65]-=a['X'-65];
			b[6]=a['X'-65];
		}
		if(a['G'-65]>0)
		{
			a['E'-65]-=a['G'-65];
			a['I'-65]-=a['G'-65];
			a['H'-65]-=a['G'-65];
			a['T'-65]-=a['G'-65];
			b[8]=a['G'-65];
		}
		if(a['O'-65]>0)
		{
			a['N'-65]-=a['O'-65];
			a['E'-65]-=a['O'-65];
			b[1]=a['O'-65];
		}
		if(a['T'-65]>0)
		{
			a['H'-65]-=a['T'-65];
			a['R'-65]-=a['T'-65];
			a['E'-65]-=2*a['T'-65];
			b[3]=a['T'-65];
		}
		if(a['F'-65]>0)
		{
			a['I'-65]-=a['F'-65];
			a['V'-65]-=a['F'-65];
			a['E'-65]-=a['F'-65];
			b[5]=a['F'-65];
		}
		if(a['S'-65]>0)
		{
			a['V'-65]-=a['S'-65];
			a['N'-65]-=a['S'-65];
			a['E'-65]-=2*a['S'-65];
			b[7]=a['S'-65];
		}
		b[9]=a['I'-65];
		for(int i=0;i<10;i++)
		{
			//cout<<b[i]<<" ";
			for(int j=0;j<b[i];j++)
			ans+=i+48;
		}
		
		out<<"Case #"<<m-t<<": "<<ans<<"\n";	}
}

