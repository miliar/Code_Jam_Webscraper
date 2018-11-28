/**
 	My standard template
 	Name: Shivam Mishra
 	handle: shivam217
 **/
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <set>
#include <assert.h>
#include <cstring>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <time.h>
#include <climits>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define FORR(i,a,b) for(int i=a;i>=b;--i)
#define FORC(it,container) for(typeof(container.begin()) it=container.begin();it!=container.end();++it)
#define INT(x) scanf("%d",&x)
#define LLD(x) scanf("%lld",&x)
#define STR(x) scanf("%s",x)
#define CHAR(x) scanf("%c",&x)
#define PINT(x) printf("%d\n",x)
#define PLLD(x) printf("%lld\n",x)
#define CLR(x) memset(x,0,sizeof(x));
#define F first
#define S second
#define PB push_back

const int INF = INT_MAX;
const int MOD = 1e9 + 7;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef map<int,int> MII;
typedef vector<pair<int,int> > VPII;
typedef vector<int> VI;
typedef vector<char> VC;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef vector<VLL> VVL;
typedef set<int> SI;
typedef set<char> SC;


char s[100005];
int main()
{	
	int tc; INT(tc);
	
	FOR(test,1,tc+1) {
		
		int smax; INT(smax);
		STR(s);
		int len = strlen(s);
		int ans=0;
		int stand = s[0]-48;
			

		FOR(i,1,len) {

			//cout<<" 1- i = "<<i<<" ans = "<<ans<<" stand = "<<stand<<endl;			

			if(stand>=i)
				stand += s[i]-48;
			else {
				if(s[i]>'0')
				ans += i-stand , stand += s[i]-48 + i-stand;
			}

			//cout<<" 2 - i = "<<i<<" ans = "<<ans<<" stand = "<<stand<<endl;
			
		}

		printf("Case #%d: %d\n",test,ans);
		
	}

return 0;
}

