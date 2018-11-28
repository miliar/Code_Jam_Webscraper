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





int main()
{
    
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);      
    /**/

    
	int T;
	sf(T);
	for(int t=1; t<=T; t++)
	{
		int k,c,s;
		sf3(k,c,s);
		printf("Case #%d: ",t);
		for(int i=0; i<k; i++)
		{
			if(i) printf(" ");
			printf("%d",i+1);
		}
		printf("\n");
	}
    
    
    return 0;
}











