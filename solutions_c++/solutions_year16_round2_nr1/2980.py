#include<iostream>
#include<stdio.h>
#include<map>
#include<string>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w+",stdout);
    long long int cases,count=1;
    cin>>cases;
    while(cases--)
    {
		string s;
		long long int ans[10]={0};
		cin>>s;
		long long int len=s.size();
		map <char,long long int> m;
		for(long long int i=0;i<len;i++)
			m[s[i]]++;
		if(m['Z']!=0)
		{
			ans[0]+=m['Z'];
			m['E']-=m['Z'];
			m['R']-=m['Z'];
			m['O']-=m['Z'];
			m['Z']=0;
		}
		if(m['W']!=0)
		{
			ans[2]+=m['W'];
			m['T']-=m['W'];
			m['O']-=m['W'];
			m['W']=0;
		}
		if(m['U']!=0)
		{
			ans[4]+=m['U'];
			m['F']-=m['U'];
			m['O']-=m['U'];
			m['R']-=m['U'];
			m['U']=0;
		}
		if(m['X']!=0)
		{
			ans[6]+=m['X'];
			m['S']-=m['X'];
			m['I']-=m['X'];
			m['X']=0;
		}
		if(m['G']!=0)
		{
			ans[8]+=m['G'];
			m['E']-=m['G'];
			m['I']-=m['G'];
			m['H']-=m['G'];
			m['T']-=m['G'];
			m['G']=0;
		}
		if(m['O']!=0)
		{
			ans[1]+=m['O'];
			m['N']-=m['O'];
			m['E']-=m['O'];
			m['O']=0;
		}
		if(m['R']!=0)
		{
			ans[3]+=m['R'];
			m['T']-=m['R'];
			m['H']-=m['R'];
			m['E']-=m['R'];
			m['E']-=m['R'];
			m['R']=0;
		}
		if(m['F']!=0)
		{
			ans[5]+=m['F'];
			m['I']-=m['F'];
			m['V']-=m['F'];
			m['E']-=m['F'];
			m['F']=0;
		}
		if(m['S']!=0)
		{
			ans[7]+=m['S'];
			m['E']-=m['S'];
			m['V']-=m['S'];
			m['E']-=m['S'];
			m['N']-=m['S'];
			m['S']=0;
		}
		if(m['I']!=0)
		{
			ans[9]+=m['I'];
			m['N']-=m['I'];
			m['N']-=m['I'];
			m['E']-=m['I'];
			m['I']=0;
		}
		cout << "Case #" << count++ << ": " ;
		for(long long int i=0;i<10;i++)
		{
			for(long long int j=1;j<=ans[i];j++)
				cout << i ;
		}
		cout << "\n";
    }
    return 0;
}
