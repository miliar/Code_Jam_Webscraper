#include<bits/stdc++.h>
using namespace std;
map<string,int> mp,mp1,mpans1,mp2,mpans2;

void solve1(string s,int l,int j)
{

	if(j==l)
	mpans1[s]=1;
	
	if(mp[s])
	return ;
	mp[s]=1;
	

		for(int k=0;k<s.size();k++)
		{
			if(s[k]=='?')
			{
				for(char i='0';i<='9';i++)
				{
					string s1=s;
					s1[k]=i;
					solve1(s1,l,j+1);	
				}
			}
		}
	
}

void solve2(string s,int l,int j)
{
	if(j==l)
	mpans2[s]=1;
	
	if(mp2[s])
	return ;
	mp2[s]=1;
	
	for(int k=0;k<s.size();k++)
		{
			if(s[k]=='?')
			{
				for(char i='0';i<='9';i++)
				{
					string s1=s;
					s1[k]=i;
					solve2(s1,l,j+1);	
				}
			}
		}
}
map<int,string> mx;
int main()
{
freopen("ins.in","r",stdin);
	freopen("out.out","w",stdout);
int t,cs=0;
	cin>>t;
	while(t--)
	{
		printf("Case #%d: ",++cs);
		string s1,s2;
		int i=0,j=0;
		cin>>s1>>s2;
		for(int k=0;k<s1.size();k++)
		{
			if(s1[k]=='?')
			i++;
		}
		
			for(int k=0;k<s2.size();k++)
		{
			if(s2[k]=='?')
			j++;
		}
		solve1(s1,i,0);
			solve2(s2,j,0);
			
			map<string,int> :: iterator it;
			int a[1000],b[1000];
			int k1=0,k2=0;
			for(it=mpans1.begin();it!=mpans1.end();it++)
			{
			
			string s=it->first;
			int x=0;

stringstream convert(s);
convert>>x;
a[k1++]=x;
mx[x]=s;
		}
			
	for(it=mpans2.begin();it!=mpans2.end();it++)
	{
					string s=it->first;
			int x=0;

stringstream convert(s);
convert>>x;
b[k2++]=x;
mx[x]=s;
	}
	string ss,ss1;
	int maxi=99999999;
	for(i=0;i<k1;i++)
	{
		for(j=0;j<k2;j++)
		{
			int x=abs(a[i]-b[j]);
			if(x<maxi)
			{
				maxi=x;
				ss=mx[a[i]];
				ss1=mx[b[j]];
			}
		}
	}
			cout<<ss<<" "<<ss1<<endl;
			
			mp.clear();
			mp1.clear();
			mp2.clear();
			mpans1.clear();
			mpans2.clear();
			mx.clear();
	}
	return 0;
}
