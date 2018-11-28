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



bool check(string &s)
{
	for(int i=0; i<s.size(); i++)
	{
		if(s[i]!='+') return 0;
	}
	return 1;
}


int main()
{
    
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);      
    /**/

    
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	string s;
    	cin>>s;
    	int res=0;
    	char c;
    	while(!check(s))
    	{
    		c=s[0];
    		for(int i=0; i<s.size(); i++)
    		{
    			if(s[i]!=c) break;
    			if(s[i]=='+') s[i]='-';
    			else s[i]='+';
    		}
    		res++;
    	}
    	printf("Case #%d: %d\n",t,res);
    }
    
    
    return 0;
}











