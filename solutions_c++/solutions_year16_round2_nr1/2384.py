#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,p2=0;
	scanf("%d",&t);
	while(t--)
	{
p2++;

	char s[20001];
	scanf("%s",s);
	int a[30];
	for(int i=0;i<30;i++)
	{
		a[i] = 0;
	}
	for(int i=0;s[i]!='\0';i++)
		a[s[i]-'A']++;
	int m=0;
	string s1;
	if(a['Z'-'A'])
	{
		m=min(a['Z'-'A'],min(a['E'-'A'],min(a['R'-'A'],a['O'-'A'])));
		a['Z'-'A']-=m;
		a['E'-'A']-=m;
		a['R'-'A']-=m;
		a['O'-'A']-=m;
		for(int i=0;i<m;i++)s1+='0';
	}
	if(a['U'-'A'])
	{
		m=min(a['U'-'A'],min(a['F'-'A'],min(a['R'-'A'],a['O'-'A'])));
		a['U'-'A']-=m;
		a['F'-'A']-=m;
		a['R'-'A']-=m;
		a['O'-'A']-=m;
		for(int i=0;i<m;i++)s1+='4';
    }
if(a['G'-'A']){
		m=min(a['G'-'A'],min(a['E'-'A'],min(a['I'-'A'],min(a['H'-'A'],a['T'-'A']))));
		a['E'-'A']-=m;
		a['I'-'A']-=m;
		a['G'-'A']-=m;
		a['H'-'A']-=m;
		a['T'-'A']-=m;
		for(int i=0;i<m;i++)s1+='8';
	}
if(a['W'-'A'])
	{
		m=min(a['W'-'A'],min(a['T'-'A'],a['O'-'A']));
		a['W'-'A']-=m;
		a['O'-'A']-=m;
		a['T'-'A']-=m;
		//a['O'-'A']-=m;
		for(int i=0;i<m;i++)s1+='2';
	}
if(a['X'-'A'])
	{
		m=min(a['X'-'A'],min(a['I'-'A'],a['S'-'A']));
		a['S'-'A']-=m;
		a['I'-'A']-=m;
		a['X'-'A']-=m;
		//a['O'-'A']-=m;
		for(int i=0;i<m;i++)s1+='6';
	}
 if(a['R'-'A'])
	{
		m=min(a['R'-'A'],min(2*a['E'-'A'],min(a['T'-'A'],a['H'-'A'])));
		a['E'-'A']-=2*m;
		a['T'-'A']-=m;
		a['R'-'A']-=m;
		a['H'-'A']-=m;
		//a['T'-'A']-=m;
		for(int i=0;i<m;i++)s1+='3';
	}
if(a['F'-'A'])
	{
		m=min(a['F'-'A'],min(a['I'-'A'],min(a['V'-'A'],a['E'-'A'])));
		a['F'-'A']-=m;
		a['I'-'A']-=m;
		a['V'-'A']-=m;
		a['E'-'A']-=m;
		for(int i=0;i<m;i++)s1+='5';
	}
if(a['V'-'A'])
	{
		m=min(a['S'-'A'],min(2*a['E'-'A'],min(a['V'-'A'],a['N'-'A'])));
		a['E'-'A']-=2*m;
		a['S'-'A']-=m;
		a['V'-'A']-=m;
		a['N'-'A']-=m;
		//a['T'-'A']-=m;
		for(int i=0;i<m;i++)s1+='7';
	}
if(a['I'-'A'])
	{
		m=min(2*a['N'-'A'],min(a['I'-'A'],a['E'-'A']));
		a['N'-'A']-=2*m;
		a['I'-'A']-=m;
		//a['V'-'A']-=m;
		a['E'-'A']-=m;
		for(int i=0;i<m;i++)s1+='9';
	}
if(a['O'-'A'])
{
	m=min(a['O'-'A'],min(a['N'-'A'],a['E'-'A']));
	a['O'-'A']-=m;
	a['N'-'A']-=m;
	a['E'-'A']-=m;
	for(int i=0;i<m;i++)s1+='1';
}
sort(s1.begin(),s1.end());
printf("Case #%d: ",p2);
cout<<s1<<"\n";
}
	return 0;
}