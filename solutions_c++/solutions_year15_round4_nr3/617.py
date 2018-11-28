#include<bits/stdc++.h>
using namespace std;

map<string,int> mp;
int mpn,b[3000],n;
char a[15];
vector<int> v[205];

inline int s2i(string s)
{
	if(mp.count(s))
		return mp[s];
	return mp[s]=mpn++;
}
inline int gao(int x)
{
	memset(b,0,sizeof(b));
	int i,j;
	for(i=0;i<n;i++,x>>=1)
		for(j=0;j<v[i].size();j++)
			b[v[i][j]]|=(x&1)+1;
	for(j=0,i=0;i<mpn;i++)
		if(b[i]==3)
			j++;
	return j;
}

int main()
{freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	int T,t,s,nn,i;
	char ch;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		mp.clear(),mpn=0;
		for(scanf("%d",&n),nn=1<<n,i=0;i<n;i++)
			for(ch=0,v[i].clear();ch!='\n';)
				scanf("%s%c",a,&ch),v[i].push_back(s2i(a));
		for(s=1<<30,i=2;i<nn;i+=4)
			s=min(s,gao(i));
		printf("Case #%d: %d\n",t,s);
	}
	return 0;
}
