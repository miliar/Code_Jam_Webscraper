#include <iostream>
#include <algorithm>
// #include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false);//cin.tie(NULL);cout.tie(NULL);
#define MAXN 20000  
using namespace std;
int main() 
{
	FAST_IO
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		string s;
		cin>>s;
		int a[26] = {};
		for(char c: s)
			a[c-'A']++;
		string b[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
		int num[10] = {};
		while(a['Z'-'A'] >=0)
		{
			bool flag = true;
			for(char c: b[0])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(!flag)
				break;
			num[0]++;
			for(char c: b[0])
				a[c-'A']--;
		}
		while(a['W'-'A'] >= 0)
		{
			bool flag = true;
			for(char c: b[2])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(!flag)
				break;
			num[2]++;
			for(char c: b[2])
				a[c-'A']--;
		}
		while(a['U'-'A'] >= 0)
		{
			bool flag = true;
			for(char c: b[4])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(!flag)
				break;
			num[4]++;
			for(char c: b[4])
				a[c-'A']--;
		}
		while(a['O'-'A'] >= 0)
		{
			bool flag = true;
			for(char c: b[1])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(!flag)
				break;
			num[1]++;
			for(char c: b[1])
				a[c-'A']--;
		}
		while(a['R'-'A'] >= 0)
		{
			bool flag = true;
			for(char c: b[3])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(a['E'-'A']<2)
				flag = false;
			if(!flag)
				break;
			num[3]++;
			for(char c: b[3])
				a[c-'A']--;
		}
		while(a['F'-'A'] >= 0)
		{
			bool flag = true;
			for(char c: b[5])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(!flag)
				break;
			num[5]++;
			for(char c: b[5])
				a[c-'A']--;
		}
		while(a['X'-'A'] >= 0)
		{
			bool flag = true;
			for(char c: b[6])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(!flag)
				break;
			num[6]++;
			for(char c: b[6])
				a[c-'A']--;
		}
		while(a['S'-'A'] >= 0)
		{
			bool flag = true;
			for(char c: b[7])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(a['E'-'A']<2)
				flag = false;
			if(!flag)
				break;
			num[7]++;
			for(char c: b[7])
				a[c-'A']--;
		}
		while(a['G'-'A'] >= 0)
		{
			bool flag = true;
			for(char c: b[8])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(!flag)
				break;
			num[8]++;
			for(char c: b[8])
				a[c-'A']--;
		}
		while(a['N'-'A'] >= 0)
		{
			bool flag = true;
			for(char c: b[9])
			{
				if(a[c-'A']==0)
				{
					flag = false;
					break;
				}					
			}
			if(a['N'-'A']<2)
				flag = false;
			if(!flag)
				break;
			num[9]++;
			for(char c: b[9])
				a[c-'A']--;
		}
		cout<<"Case #"<<t<<": ";
		for(int i=0;i<10;i++)
		{
			for(int j=0;j<num[i];j++)
			{
				cout<<i;
			}
		}
		cout<<"\n";
	}
}
