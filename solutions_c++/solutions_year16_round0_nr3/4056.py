#include<bits/stdc++.h>
using namespace std;
int main()
{	ifstream f1("C-small-attempt5.in");
	ofstream f2("C-small-ans.out");
	int t,x=1;
	f1>>t;
	while(t--)
	{
		f2<<"Case #"<<x++<<":\n";
		int n,j;
		f1>>n>>j;
		string s="1";
		for(int i=1;i<n-1;i++)
		s+="0";
		s+="1";
	while(j--)
	{	long long div[11]={0},u;
		
		while(!div[0])
		{
		long long no;
		for(int k=2;k<=10;k++)
		{	no=0;
		for(int i=s.size()-1,o=0;i>=0;i--,o++)
			if(s[i]=='1')
			{
				no+=pow(k,o);
			}
		for(int u=2;u<=16000;u++)
		if(no%u==0)
		{	div[k]=u;break;
			}
		if(div[k]==0)  
		{	div[1]=1;
			break;}
		
		}
		if(div[1]==1)
		{
			div[1]=0;
			for(int i=n-2;i>0;i--)
				if(s[i]=='0')
				{s[i]='1';break;
				}
				else s[i]='0';			
		}
		else div[0]=1;
		}
		/*for(int i=2;i<=10;i++)
		{
			for(long pl=2;pl<=16000;pl++)
			{	
				if(div[i]%pl==0)
				{	
					div[i]=pl; break;
				}
			}
			
		}*/
		
		f2<<s<<" ";
			for(int i=2;i<=10;i++)
				f2<<div[i]<<" ";
		for(int i=n-2;i>0;i--)
			if(s[i]=='0')
			{s[i]='1';break;
			}
			else s[i]='0';
		f2<<'\n';
		if(j==14||j==13)
			for(int i=n-2;i>0;i--)
			if(s[i]=='0')
			{s[i]='1';break;
			}
			else s[i]='0';
		
	}
	}
	f1.close();
	f2.close();
	return 0;
}
