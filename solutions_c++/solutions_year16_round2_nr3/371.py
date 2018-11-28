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



string s1[1010],s2[1010];
unordered_map<string, int> us;

vector<int> g[2010];

int cc=1,u[2010];
bool u1[2010],u2[2010];
map<int, int> pa;

bool dfs(int v)
{
    u[v]=cc;
    for(int i=0; i<g[v].size(); i++)
    {
        int qwe=pa[g[v][i]];
        if(qwe==0||u[qwe]!=cc&&dfs(qwe))
        {
            pa[g[v][i]]=v;
            return 1;
        }
    }
    return 0;
}

int main()
{
    
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);      
    /**/
	
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	int n;
    	sf(n);
    	int cnt=1;
    	us.clear();
    	for(int i=0; i<2010; i++)
    	{
    		g[i].clear();
    	}
    	memset(u,0,sizeof(u));
    	cc=1;
    	pa.clear();
    	set<int> S;
    	set<int> S2;
    	for(int i=0; i<n; i++)
    	{
    		cin>>s1[i]>>s2[i];
    		int &r1=us[s1[i]];
    		int &r2=us[s2[i]];
    		if(r1==0)
    		{
    			r1=cnt++;
    		}
    		if(r2==0)
    		{
    			r2=cnt++;
    		}
    		g[r1].pb(r2);
    		S.insert(r1);
    		S2.insert(r2);
    	}
    	if(n<=2)
    	{
    		printf("Case #%d: 0\n",t);
    		continue;
    	}
    	
	    for(auto i: S)
	    {
	        if(dfs(i))
	            cc++;
	    }
	    for(auto i: pa)
	    {
	    	S2.erase(i.first);
	    	S.erase(i.second);
	    }
	    int res=pa.size()+S.size()+S2.size();
	    printf("Case #%d: %d\n",t,n-res);
    }
    
    
    
    return 0;
}











