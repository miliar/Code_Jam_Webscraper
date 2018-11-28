#include<bits/stdc++.h>
using namespace std;

#define sd(a) scanf("%d",&a)
#define ss(a) scanf("%s",&a)
#define sl(a) scanf("%lld",&a)
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define F first
#define S second
#define MP make_pair
#define PB push_back
string go(int cur,int n)
{
	if(n==0)
	{
		string ret="";
		if(cur==1)
			return ret+'R';
		if(cur==2)
			return ret+'P';
		if(cur==3)
			return ret+'S';
	}
	string s1,s2;
	if(cur==1)
	{
		s1=go(1,n-1);
		s2=go(3,n-1);
	}
	if(cur==2)
	{
		s1=go(1,n-1);
		s2=go(2,n-1);
	}
	if(cur==3)
	{
		s1=go(2,n-1);
		s2=go(3,n-1);
	}
	if(s1>s2)
		swap(s1,s2);
	return (s1+s2);

}
int main()
{
	// freopen("A_1.in","r",stdin);
	// freopen("A_1.out","w",stdout);
	int t,n,i,r,p,s,x,y,z;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		sd(n);sd(r);sd(p);sd(s);
		int r1=r,p1=p,s1=s,n1=n;
		bool f=0;
		while(n)
		{
			--n;
			x=(r+s+p)/2-s;
			y=(r+s+p)/2-p;
			z=(r+s+p)/2-r;
			if(x<0 || y<0 || z<0)
			{
				f=1;
				break;
			}
			p=x;
			r=y;
			s=z;
		}
		printf("Case #%d: ",tt);
		if(f)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		cout<<go(r*1+p*2+s*3,n1)<<'\n';
	}	
}