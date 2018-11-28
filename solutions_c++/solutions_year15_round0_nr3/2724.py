#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define rrep(i,x,y) for(i=x;i>=y;i--)
#define trv(y,x) for(typeof(x.begin())y=x.begin();y!=x.end();y++)
#define pb(f) push_back(f)
#define sc(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define pi(c) printf("%d\n",c)
#define pil(c) printf("%lld\n",c)
#define ll long long int
#define pii pair<int,int>
#define vi vector<int>
#define scs(a) scanf("%s",a)
using namespace std;
#define mod 1000000007
char s[10001];
int sign[10001],revsign[10001];
char dp[10001],revdp[10001];
char mult(char a,char b)
{
	if(a=='1')
	{
		if(b=='1')
		return '1';
		if(b=='i')
		return 'i';
		if(b=='j')
		return 'j';
		if(b=='k')
		return 'k';
	}
	if(a=='i')
	{
		if(b=='1')
		return 'i';
		if(b=='i')
		return '1';
		if(b=='j')
		return 'k';
		if(b=='k')
		return 'j';
	}
	if(a=='j')
	{
		if(b=='1')
		return 'j';
		if(b=='i')
		return 'k';
		if(b=='j')
		return '1';
		if(b=='k')
		return 'i';
	}
	if(a=='k')
	{
		if(b=='1')
		return 'k';
		if(b=='i')
		return 'j';
		if(b=='j')
		return 'i';
		if(b=='k')
		return '1';
	}
}
int signmult(char a,char b)
{
	if(a=='1')
	{
		if(b=='1')
		return 1;
		if(b=='i')
		return 1;
		if(b=='j')
		return 1;
		if(b=='k')
		return 1;
	}
	if(a=='i')
	{
		if(b=='1')
		return 1;
		if(b=='i')
		return -1;
		if(b=='j')
		return 1;
		if(b=='k')
		return -1;
	}
	if(a=='j')
	{
		if(b=='1')
		return 1;
		if(b=='i')
		return -1;
		if(b=='j')
		return -1;
		if(b=='k')
		return 1;
	}
	if(a=='k')
	{
		if(b=='1')
		return 1;
		if(b=='i')
		return 1;
		if(b=='j')
		return -1;
		if(b=='k')
		return -1;
	}
}
map<pair<int,int>,int> mp;
int main()
{
	int t,i,j,k;
	sc(t);
	
	int caase=1;
	while(t--)
	{
		int n,l,x;
		sc(l); sc(x);
		n=l*x;
		scs(s+1);
	/*	for(i=1;i<=l;i++)
		{
			if(s[i]=='i')
			a[i]=2;
			else if(s[i]=='j')
			a[i]=3;
			else a[i]=4;
		}*/
		i=l+1;
		for(j=1;j<x;j++)
		{
			for(k=1;k<=l;k++)
			{
				s[i]=s[k];
				i++;
			}
		}
	//	for(i=1;i<=n;i++)
	//	printf("%c",s[i]);
		dp[1]=s[1];sign[1]=1;
		revdp[n]=s[n];revsign[n]=1;
		for(i=2;i<=n;i++)
		{
			dp[i]=mult(dp[i-1],s[i]);
			sign[i]=sign[i-1]*signmult(dp[i-1],s[i]);
		}
		for(i=n-1;i>=1;i--)
		{
			revdp[i]=mult(s[i],revdp[i+1]);
			revsign[i]=revsign[i+1]*signmult(s[i],revdp[i+1]);
		}
	//	for(i=1;i<=n;i++)
	//	cout<<dp[i]<<" "<<"n="<<n<<" "<<sign[i]<<endl;
	//	cout<<endl<<endl;
		
	//	for(i=n;i>=1;i--)
	//	cout<<revdp[i]<<" "<<"n="<<n<<" "<<revsign[i]<<endl;
		bool fa=false,fb=false,fc=false;
		for(i=1;i<=n-2;i++)
		{
			if(dp[i]=='i'&&sign[i]==1)
			{
				fa=true;
				break;
			}
			
		}
		if(fa)
		{
		//	cout<<"yo"<<endl;
			for(j=n;j>i+1&&j>2;j--)
			{
				if(revdp[j]=='k'&&revsign[j]==1)
				{
					fb=true;
					break;
				}
			}
			if(fb)
			{
		//		cout<<"yo"<<endl;
				char aaa='1';
				int signaaa=1;
				for(k=i+1;k<j;k++)
				{
					char prev=aaa;
					int signprev=signaaa;
				//	cout<<s[k]<<endl;
					aaa=mult(aaa,s[k]);
					signaaa=signprev*signmult(prev,s[k]);
				}
				if(aaa=='j'&&signaaa==1)
				{
					fc=true;
				}
				
			}
		}
		if(fa&&fb&&fc)
		{
			printf("Case #%d: YES\n",caase);
		}
		else
		{
			printf("Case #%d: NO\n",caase);
		}
		
		caase++;
	}
}
