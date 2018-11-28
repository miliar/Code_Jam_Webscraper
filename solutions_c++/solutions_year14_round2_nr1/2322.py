#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;
int main()
{
	int i,j,n,t,tc,arr[101][26],av[26],ans,p[101],len[101],to,end;
	string a[101],an;
	char c[101],pre;
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	cin>>t;
	for (tc=1;tc<=t;tc++)
	{
		an="";
		cin>>n;
		for (j=0;j<n;j++)for (i=0;i<26;i++) arr[j][i]=0;
		for (i=0;i<26;i++) av[i]=0;
		for (i=0;i<n;i++) cin>>a[i];
		ans=0;	
		for (i=0;i<n;i++) p[i]=0;
		for (i=0;i<n;i++) c[i]=a[i][0];
		while (1)
		{
//			cout<<ans<<" ";
			to=0;
			for (i=0;i<n;i++) len[i]=0;
			for (i=0;i<n;i++)
			{
				c[i]=a[i][p[i]];
				while (p[i]<a[i].length()&&a[i][p[i]]==c[i])
				{
					p[i]++;
					len[i]++;
					to++;
				}
			}
			end=0;
			pre=c[0];
			for (i=0;i<n;i++)
			{
				if (p[i]==a[i].length())
				{
					end++;
				}
				if (pre!=c[i])
				{
					an="Fegla Won";
					break;
				}
			}
			if (end!=0&&end!=n)
			{
				an="Fegla Won";
				break;
			}
			if (an!="")
			{
				break;
			}
			else
			{
				to=to/n;
				for (i=0;i<n;i++)
				{
					ans+=abs(to-len[i]);
				}
			}
			if (end==n)
			{
				break;
			}
		}
		if (an!="")
		{
			cout<<"Case #"<<tc<<": "<<an<<endl;
		}
		else
		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}
}
