#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<map>
#include<vector>
using namespace std;
typedef unsigned long long LL;
int N,J,cnt;
vector<int> fc[555];
map<string,int> S;

bool dv(string &s,int b,int d)
{
	int r=0;
	for(int i=0;i<N;i++)
		r=(r*b+s[i]-'0')%d;
	return r==0;
}

void Add(string s)
{
	if(S.count(s))return;
	vector<int> v;
	for(int b=2;b<=10;b++)
	{
		for(int i=2;i<=1000;i++)
			if(dv(s,b,i)){v.push_back(i);break;}
	}
	if(v.size()==9)
	{
		S[s]=++cnt;
		fc[cnt]=v;
		if(cnt==J)
		{
			int id=0;
			for(map<string,int>::iterator it=S.begin();it!=S.end();it++)
			{
				cout<<it->first;
				for(int i=0;i<9;i++)
					cout<<' '<<fc[it->second][i];
				cout<<endl;
			}
			exit(0);
		}
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	cin>>N;cout<<"Case #1:"<<endl;
	cin>>N>>J;
	while(1)
	{
		string s;
		s="";
		s+='1';
		for(int i=1;i<N-1;i++)
			s+=rand()>>3&1?'1':'0';
		s+='1';
		Add(s);
	}
	return 0;
}

