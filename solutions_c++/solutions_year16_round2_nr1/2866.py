#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	string num[10] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
	int cases=1;
	while(t--)
	{
		string s;
		cin>>s;
		int count[26]={};
		int ans[26]={};
		for(int i=0;i<s.length();i++)
		{
			count[s[i]-'A']++;
		}
		if(count['Z'-'A']>0)
		{
			int diff = count[25];
			count['Z'-'A']-=diff;
			count['E'-'A']-=diff;
			count['R'-'A']-=diff;
			count['O'-'A']-=diff;
			ans[0]=diff;
		}
		if(count['G'-'A']>0)
		{
			int diff = count['G'-'A'];
			count['E'-'A']-=diff;
			count['I'-'A']-=diff;
			count['G'-'A']-=diff;
			count['H'-'A']-=diff;
			count['T'-'A']-=diff;
			ans[8]=diff;
		}
		if(count['W'-'A']>0)
		{
			int diff = count['W'-'A'];
			count['T'-'A']-=diff;
			count['W'-'A']-=diff;
			count['O'-'A']-=diff;
			ans[2]=diff;
		}
		if(count['X'-'A']>0)
		{
			int diff = count['X'-'A'];
			count['S'-'A']-=diff;
			count['I'-'A']-=diff;
			count['X'-'A']-=diff;
			ans[6]=diff;
		}
		if(count['U'-'A']>0)
		{
			int diff = count['U'-'A'];
			count['F'-'A']-=diff;
			count['O'-'A']-=diff;
			count['U'-'A']-=diff;
			count['R'-'A']-=diff;
			ans[4]=diff;
		}
		if(count['O'-'A']>0)
		{
			int diff = count['O'-'A'];
			count['O'-'A']-=diff;
			count['N'-'A']-=diff;
			count['E'-'A']-=diff;
			ans[1]=diff;	
		}
		if(count['R'-'A']>0)
		{
			int diff = count['R'-'A'];
			count['T'-'A']-=diff;
			count['H'-'A']-=diff;
			count['R'-'A']-=diff;
			count['E'-'A']-=diff;
			count['E'-'A']-=diff;
			ans[3]=diff;	
		}
		if(count['F'-'A']>0)
		{
			int diff = count['F'-'A'];
			count['F'-'A']-=diff;
			count['I'-'A']-=diff;
			count['V'-'A']-=diff;
			count['E'-'A']-=diff;
			ans[5]=diff;	
		}
		if(count['S'-'A']>0)
		{
			int diff = count['S'-'A'];
			count['S'-'A']-=diff;
			count['E'-'A']-=diff;
			count['V'-'A']-=diff;
			count['E'-'A']-=diff;
			count['N'-'A']-=diff;
			ans[7]=diff;	
		}
		if(count['I'-'A']>0)
		{
			int diff = count['I'-'A'];
			count['N'-'A']-=diff;
			count['I'-'A']-=diff;
			count['N'-'A']-=diff;
			count['E'-'A']-=diff;
			ans[9]=diff;	
		}
		string res="";
		for(int i=0;i<=9;i++)
		{
			for(int j=0;j<ans[i];j++)
				res+=(i+'0');
		}
		cout<<"Case #"<<cases<<": "<<res<<endl;
		cases++;
	}
	return 0;
}
