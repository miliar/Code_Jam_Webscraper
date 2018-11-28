#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

#define inf (9999999999999999LL)
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define eps 1e-8
 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) //fprintf(stderr,args)
#endif

#define pb push_back	
#define mod 1000000007
#define maxn 100100

using namespace std;

char M[110][110];

map<char,int> dx;
map<char,int> dy;

char dir[4] = {'^','v','>','<'};

main(){

		dy['>'] = 1;
		dy['<'] = -1;
		dx['^'] = -1;
		dx['v'] = 1;

		int te;
		scanf("%d",&te);
		
		for(int t=1;t<=te;t++){

			int n,m;
			scanf("%d%d",&n,&m);

			for(int i=0;i<n;i++)
				for(int j=0;j<m;j++)
					scanf(" %c",&M[i][j]);

			int ans = 0;
			int imp = 0;

			for(int i=0;i<n;i++)
				for(int j=0;j<m;j++){

					int x = i, y = j;
					char c = M[i][j];

					debug("i %d j %d\n",i,j);

					if(c == '.') continue;

					int ok = 0;
					x += dx[c];
					y += dy[c];
					while(x >= 0 && y >=0 && x < n && y < m){
						if(M[x][y] != '.') ok = 1;
						x += dx[c];
						y += dy[c];
					}

					debug("ve %d\n",ok);
					if(ok) continue;

					ok = 0;

					for(int u=0;u<4;u++){

						x = i, y = j;
						x += dx[dir[u]];
						y += dy[dir[u]];
						while(x >= 0 && y >=0 && x < n && y < m){
							if(M[x][y] != '.') {ok = 1; debug("! %d %d\n",x,y);}
							x += dx[dir[u]];
							y += dy[dir[u]];
							
						}

					}

					debug("qq %d\n",ok);
					if(ok == 0) imp = 1;
					else ans++;

				}

			printf("Case #%d: ",t);
			if(imp) printf("IMPOSSIBLE\n");
			else printf("%d\n",ans);

		}

}
