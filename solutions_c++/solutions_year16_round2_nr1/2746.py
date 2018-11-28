#include<bits/stdc++.h>
#define scan(n) scanf("%d",&n)
#define scanll(n) scanf("%lld",&n)
#define For(i,a,b) for(i=a;i<b;i++)
#define fill(a,b) memset(a,b,sizeof(a))
#define swap(a,b) a=a+b;b=a-b;a=a-b;
#define ll long long int
#define pb push_back
#define MAX 1000000007
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std;
int main()
{
//	f_in("A-large.in");
//	f_out("A-large-out.txt");
	int test;
	scan(test);
	for(int t = 1 ;t<=test;t++)
	{
		int hash[26];
		int count[10];
		fill(hash,0);
		fill(count,0);
		string str;
		cin>>str;
		string s[10];
		s[0]="ZERO";
		s[1]="ONE";
		s[2]="TWO";
		s[3]="THREE";
		s[4]="FOUR";
		s[5]="FIVE";
		s[6]="SIX";
		s[7]="SEVEN";
		s[8]="EIGHT";
		s[9]="NINE";
		
		int len = str.length(),i;
		for(i=0;i<len;i++)
		{
			hash[str[i]-'A']++;
		}
		if(hash['Z'-'A'])
		{
			int v = hash['Z'-'A'];
			 count[0]+=v;
			 char c;
			 for(i=0;i<s[0].length();i++)
			 {
			 	c=s[0][i];
			 	hash[c-'A']-=v;
			 }
		}
		if(hash['W'-'A'])
		{
			int v = hash['W'-'A'];
			 count[2]+=v;
			 char c;
			 for(i=0;i<s[2].length();i++)
			 {
			 	c=s[2][i];
			 	hash[c-'A']-=v;
			 }
		}
		if(hash['G'-'A'])
		{
			int v = hash['G'-'A'];
			 count[8]+=v;
			 char c;
			 for(i=0;i<s[8].length();i++)
			 {
			 	c=s[8][i];
			 	hash[c-'A']-=v;
			 }
		}
		if(hash['X'-'A'])
		{
			int v = hash['X'-'A'];
			 count[6]+=v;
			 char c;
			 for(i=0;i<s[6].length();i++)
			 {
			 	c=s[6][i];
			 	hash[c-'A']-=v;
			 }
		}
		if(hash['H'-'A'])
		{
			int v = hash['H'-'A'];
			 count[3]+=v;
			 char c;
			 for(i=0;i<s[3].length();i++)
			 {
			 	c=s[3][i];
			 	hash[c-'A']-=v;
			 }
		}
		if(hash['R'-'A'])
		{
			int v = hash['R'-'A'];
			 count[4]+=v;
			 char c;
			 for(i=0;i<s[4].length();i++)
			 {
			 	c=s[4][i];
			 	hash[c-'A']-=v;
			 }
		}
		if(hash['F'-'A'])
		{
			int v = hash['F'-'A'];
			 count[5]+=v;
			 char c;
			 for(i=0;i<s[5].length();i++)
			 {
			 	c=s[5][i];
			 	hash[c-'A']-=v;
			 }
		}
		if(hash['V'-'A'])
		{
			int v = hash['V'-'A'];
			 count[7]+=v;
			 char c;
			 for(i=0;i<s[7].length();i++)
			 {
			 	c=s[7][i];
			 	hash[c-'A']-=v;
			 }
		}
		if(hash['O'-'A'])
		{
			int v = hash['O'-'A'];
			 count[1]+=v;
			 char c;
			 for(i=0;i<s[1].length();i++)
			 {
			 	c=s[1][i];
			 	hash[c-'A']-=v;
			 }
		}
		if(hash['N'-'A'])
		{
			int v = hash['N'-'A'];
			v=v/2;
			 count[9]+=v;
			 char c;
			 for(i=0;i<s[9].length();i++)
			 {
			 	c=s[9][i];
			 	hash[c-'A']-=v;
			 }
		}
		
		cout<<"Case #"<<t<<": "; 
		for(i=0;i<10;i++)
		{
			for(int j = 0;j<count[i];j++)
			cout<<i;
		}
		cout<<endl;
	}
 	return 0;
}


