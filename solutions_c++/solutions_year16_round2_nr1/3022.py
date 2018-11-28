#include <bits/stdc++.h>
using namespace std;

int main() 
{
	ifstream input;
    ofstream output;
    input.open("A-large.in");
    output.open("output.txt");
	int t,j=1;
	input>>t;
	while(t--)
	{char s[5000];
	int a[30],b[5000],i,x,k=0;
	for(i=0;i<5000;++i)
	b[i]=0;
	for(i=0;i<30;++i)
	a[i]=0;
	input>>s;
	for(i=0;i<strlen(s);++i)
	a[s[i]-64]++;
		if(a[23]>0)
		{
			x=a[23];
			for(i=0;i<x;++i)
			b[k++]=2;
			a[15]-=x;a[20]-=x;a[23]-=x;
		}
		if(a[21]>0)
		{
			x=a[21];
			for(i=0;i<x;++i)
			b[k++]=4;
			a[21]-=x;a[15]-=x;a[6]-=x;a[18]-=x;
		}
		if(a[6]>0)
		{
			x=a[6];
			for(i=0;i<x;++i)
			b[k++]=5;
			a[6]-=x;a[9]-=x;a[22]-=x;a[5]-=x;
		}
		if(a[24]>0)
		{
			x=a[24];
			for(i=0;i<x;++i)
			b[k++]=6;
			a[24]-=x;a[9]-=x;a[19]-=x;
		}
		if(a[22]>0)
		{
			x=a[22];
			for(i=0;i<x;++i)
			b[k++]=7;
			a[22]-=x;a[5]-=2*x;a[19]-=x;a[14]-=x;
		}
		if(a[7]>0)
		{
			x=a[7];
			for(i=0;i<x;++i)
			b[k++]=8;
			a[5]-=x;a[9]-=x;a[7]-=x;a[8]-=x;a[20]-=x;
		}
		if(a[9]>0)
		{
			x=a[9];
			for(i=0;i<x;++i)
			b[k++]=9;
			a[14]-=2*x;a[5]-=x;a[9]-=x;
		}
		if(a[26]>0)
		{
			x=a[26];
			for(i=0;i<x;++i)
			b[k++]=0;
			a[26]-=x;a[5]-=x;a[15]-=x;a[18]-=x;
		}
		if(a[15]>0&&a[14]>0&&a[5]>0)
		{
			x=min(a[15],min(a[14],a[5]));
			for(i=0;i<x;++i)
			b[k++]=1;
			a[15]-=x;a[14]-=x;a[5]-=x;
		}
		if(a[18]>0&&a[8]>0)
		{
			x=min(a[20],min(a[8],min(a[18],a[5]/2)));
			for(i=0;i<x;++i)
			b[k++]=3;
			a[18]-=x;a[20]-=x;a[5]-=2*x;a[8]-=x;
		}
		output<<"Case #"<<j<<": ";j++;
	sort(b,b+k);
	for(i=0;i<k;++i)
	output<<b[i];
	output<<endl;}
	return 0;
}
