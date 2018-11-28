#include<bits/stdc++.h>
using namespace std;

int n,r,p,s;

inline string gao(int n,string s)
{
	if(n<=0)
		return s;
	string l=gao(n-1,s);
	string r=gao(n-1,s=="S"?"P":s=="R"?"S":"R");
	return l<r?l+r:r+l;
}
inline bool ck(int np,int nr,int ns)
{
	for(int i=0;i<n;i++)
	{
		int ap=ns,ar=np,as=nr;
		np+=ap,nr+=ar,ns+=as;
	}
	return np==p&&nr==r&&ns==s;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,_;
	for(scanf("%d",&T),_=1;_<=T;_++)
	{
		scanf("%d%d%d%d",&n,&r,&p,&s);
		cout<<"Case #"<<_<<": ";
		if(ck(1,0,0)) cout<<gao(n,"P");
		else if(ck(0,1,0)) cout<<gao(n,"R");
		else if(ck(0,0,1)) cout<<gao(n,"S");
		else cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	return 0;
}
