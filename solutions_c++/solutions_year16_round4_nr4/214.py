#include<bits/stdc++.h>
using namespace std;

string a[30],b[30];
map<string,int> mp;
int n,s,v[30];

inline void gao(int x)
{
	int i,j,k,p;
	for(p=i=0;i<n;i++)
		b[i]=a[i];
	for(k=i=0;i<n;i++)
		for(j=0;j<n;j++,k++)
			if(x&1<<k)
			{
				if(b[i][j]=='0')
					b[i][j]='1',p++;
			}
			else
			{
				if(b[i][j]=='1')
					return;
			}
	mp.clear();
	memset(v,0,sizeof(v));
	for(i=0;i<n;i++)
		mp[b[i]]++;
	for(auto c:mp)
	{
		for(k=i=0;i<n;i++)
			if(c.first[i]=='1')
			{
				if(!v[i]) v[i]=1;
				else return;
				k++;
			}
		if(c.second!=k)
			return;
	}
	s=min(s,p);
}

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	int T,_,i,m;
	for(cin>>T,_=1;_<=T;_++)
	{
		for(cin>>n,m=1<<n*n,i=0;i<n;i++)
			cin>>a[i];
		for(s=1<<30,i=0;i<m;i++)
			gao(i);
		printf("Case #%d: %d\n",_,s);
	}
	return 0;
}
