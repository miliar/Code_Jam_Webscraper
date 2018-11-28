#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#include<algorithm>
#include<memory>
#include<map>
#include<queue>
#include<limits>
#include<iomanip>
#include<fstream>
using namespace std;

int main()
{
	freopen("1l.in","r",stdin);
	freopen("1l_o.out","wt",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		string s;
		cin>>s;
		int n=s.length();
		int a[26]={0},ans[10]={0};
		for(int i=0;i<n;i++)
		{
			a[s[i]-65]++;
		}
		cout<<"Case #"<<tc<<": ";
		if(a[25])
		{
			int m=a[25];
			a[25]-=m;
			a[4]-=m;
			a[17]-=m;
			a[14]-=m;
			for(int i=0;i<m;i++)
				cout<<"0";
		}
		if(a[22])
		{
			int m=a[22];
			a[22]-=m;
			a[19]-=m;
			a[14]-=m;
			ans[2]+=m;
			
		}
		if(a[20])
		{
			int m=a[20];
			a[20]-=m;
			a[5]-=m;
			a[14]-=m;
			a[17]-=m;
			ans[4]+=m;
			
		}
		if(a[6])
		{
			int m=a[6];
			a[6]-=m;
			a[4]-=m;
			a[8]-=m;
			a[7]-=m;
			a[19]-=m;
			ans[8]+=m;
			
		}
		if(a[14])
		{
			int m=a[14];
			a[14]-=m;
			a[13]-=m;
			a[4]-=m;
			ans[1]+=m;
			
		}
		if(a[19])
		{
			int m=a[19];
			a[19]-=m;
			a[7]-=m;
			a[17]-=m;
			a[4]-=m;
			a[4]-=m;
			ans[3]+=m;
			
		}
		if(a[5])
		{
			int m=a[5];
			a[5]-=m;
			a[8]-=m;
			a[20]-=m;
			a[4]-=m;
			ans[5]+=m;
			
		}
		if(a[23])
		{
			int m=a[23];
			a[23]-=m;
			a[18]-=m;
			a[8]-=m;
			ans[6]+=m;
			
		}
		if(a[18])
		{
			int m=a[18];
			a[18]-=m;
			a[4]-=m;
			a[21]-=m;
			a[4]-=m;
			a[13]-=m;
			ans[7]+=m;
			
		}
		if(a[13])
		{
			int m=a[13];
			ans[9]=m/2;
			//cout<<a[9]<<endl;
			
		}
		for(int i=1;i<10;i++)
		{
			if(ans[i])
			{
				for(int j=0;j<ans[i];j++)
					cout<<i;
			}
		}
		cout<<endl;
		
		
		
		//cout<<endl;
	}
	return 0;
}
