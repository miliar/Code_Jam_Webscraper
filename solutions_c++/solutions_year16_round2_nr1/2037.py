#include <bits/stdc++.h>
using namespace std;
vector<string>vv(10);
int main()
{
	vv[0]="ZERO";
	vv[1]="ONE";
	vv[2]="TWO";
	vv[3]="THREE";
	vv[4]="FOUR";
	vv[5]="FIVE";
	vv[6]="SIX";
	vv[7]="SEVEN";
	vv[8]="EIGHT";
	vv[9]="NINE";
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		string s;
		cin>>s;
		vector<int>v(26,0);
		for(int i=0;i<s.size();i++)
		{
			v[s[i]-'A']++;
		}
		vector<int>ans(10,0);
		ans[0] = v['Z'-'A'];
		for(auto ch:vv[0])v[ch-'A']-=ans[0];
		ans[6]=v['X'-'A'];
		for(auto ch:vv[6])v[ch-'A']-=ans[6];
		ans[2]=v['W'-'A'];
		for(auto ch:vv[2])v[ch-'A']-=ans[2];
		ans[8]=v['G'-'A'];
		for(auto ch:vv[8])v[ch-'A']-=ans[8];
		ans[3]=v['H'-'A'];
		for(auto ch:vv[3])v[ch-'A']-=ans[3];
		ans[4]=v['U'-'A'];
		for(auto ch:vv[4])v[ch-'A']-=ans[4];
		ans[5]=v['F'-'A'];
		for(auto ch:vv[5])v[ch-'A']-=ans[5];
		ans[7]=v['V'-'A'];
		for(auto ch:vv[7])v[ch-'A']-=ans[7];
		ans[1]=v['O'-'A'];
		for(auto ch:vv[1])v[ch-'A']-=ans[1];
		ans[9]=v['E'-'A'];
		for(auto ch:vv[9])v[ch-'A']-=ans[9];
		/*map<int,int>m;
		for(int i=0;i<10;i++)m.insert({i,ans[i]});*/
		cout<<"Case #"<<tt<<": ";
		for(int i=0;i<=9;i++)
		{
			int cc=ans[i];
			while(cc--)cout<<i;
		}
		/*for(auto & ii:m)
		{
			int cc = ii.second;
			if(cc)
			while(cc--)cout<<ii.second;
		}*/
		cout<<'\n';
	}
	
}
