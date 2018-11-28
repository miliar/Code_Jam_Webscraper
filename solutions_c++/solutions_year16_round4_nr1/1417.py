#include<bits/stdc++.h>
#include<cstdlib>   
#define sf(x) scanf("%d",&x)
#define pf(x) printf("%d ",x)
#define sf2(x,y) scanf("%d %d",&x,&y)
#define pf2(x,y) printf("%d %d ",x,y)
#define sf3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf3(x,y,z) printf("%d %d %d ",x,y,z)
#define sfc(c) scanf(" %c",&c)
#define pfc(c) printf("%c",c)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define INF 2000000000
#define ENDL puts("")


using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef unsigned int uint;
typedef long double ld;



string Sort(string a)
{
	if(a.size()==1) return a;
	string l,r;
	for(int i=0; i<a.size()/2; i++)
	{
		l.pb(a[i]);
	}
	for(int i=a.size()/2; i<a.size(); i++)
	{
		r.pb(a[i]);
	}
	l=Sort(l);
	r=Sort(r);
	if(l<r) 
	{
		return l+r;
	}
	else 
	{
		return r+l;
	}
}




string foo(string s, int n)
{
	for(int i=0; i<n; i++)
	{
		string tmp;
		for(int j=0; j<s.size(); j++)
		{
			if(s[j]=='S')
			{
				tmp+="PS";
			}
			else if(s[j]=='P')
			{
				tmp+="PR";
			}
			else
			{
				tmp+="RS";
			}
		}
		s=tmp;
	}
	return s;
}

bool check(string &s, int *Q)
{
	int cnt[3];
	memset(cnt,0,sizeof(cnt));
	for(int i=0; i<s.size(); i++)
	{
		if(s[i]=='R')
		{
			cnt[0]++;
		}
		else if(s[i]=='P')
		{
			cnt[1]++;
		}
		else
		{
			cnt[2]++;
		}
	}
	return cnt[0]==Q[0]&&cnt[1]==Q[1]&&cnt[2]==Q[2];
}

int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);      
    /**/
    
    
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	int n;
    	sf(n);
    	int N=(1<<n);
    	int Q[5];
    	memset(Q,0,sizeof(Q));
    	sf3(Q[0],Q[1],Q[2]);
    	string a,b,c;
    	a=foo("S",n);
    	b=foo("R",n);
    	c=foo("P",n);
    	string v="Z";
    	bool f=0;
    	if(check(a,Q))
    	{
    		f=1;
    		a=Sort(a);
    		v=min(v,a);
    	}
    	if(check(b,Q))
    	{
    		f=1;
    		b=Sort(b);
    		v=min(v,b);
    	}
    	if(check(c,Q))
    	{
    		f=1;
    		c=Sort(c);
    		v=min(v,c);
    	}
    	if(!f)
    	{
    		printf("Case #%d: IMPOSSIBLE\n",t);
    	}
    	else
    	{
    		printf("Case #%d: %s\n",t,v.c_str());
    	}
    }
    
    
    return 0;
}












