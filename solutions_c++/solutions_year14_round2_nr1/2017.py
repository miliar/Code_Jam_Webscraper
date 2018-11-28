#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,n,i,j;
	cin>>t;
	string a[200];
	int b[200],c[200];
	char curr;
	int flag,sum;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		for(j=0;j<n;j++)
		{
			cin>>a[j];
		}
		sort(a,a+n);
		flag=sum=0;
		for(j=0;j<200;j++)b[j]=0;
		while(a[0][b[0]]!='\0')
		{
			curr=a[0][b[0]];
			for(j=0;j<n;j++)
			{
				c[j]=0;
				while(a[j][b[j]]==curr){b[j]++;c[j]++;}
			}
			sort(c,c+n);
			if(c[0]==0){flag=1; break;}
			for(j=0;j<n;j++)
			{
				sum+=abs(c[j]-c[n/2]);
			}
		}
		for(j=0;j<n;j++)
		{
			if(b[j]!=a[j].length())flag=1;
		}
		if(flag)
		{
			cout<<"Case #"<<i<<": Fegla Won\n";
		}
		else
		{
			cout<<"Case #"<<i<<": "<<sum<<endl;
		}
	}
	return 0;
}
