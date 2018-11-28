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
#define eps 1e-15
 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back	
#define mod 1000000007
#define maxn 100100

using namespace std;

map<string,int> mp;
char aux[12];

int fixo[3030];
int lang[3030];

vector<int> v[22];
int cont;
int ans;
int n;

void brute(int pos){

	if(pos == n){

		int cur = 0;
		for(int i=0;i<cont;i++) if(lang[i] == 3) cur++;

		ans = min(ans,cur);

		return;
	}

	vector<int> last;

	for(int i=0;i<v[pos].size();i++)
		last.pb(lang[v[pos][i]]);

	for(int i=0;i<v[pos].size();i++){
		lang[v[pos][i]] |= 1;
	}

	brute(pos+1);

	for(int i=0;i<v[pos].size();i++){
		lang[v[pos][i]] = last[i];
		lang[v[pos][i]] |= 2;
	}

	brute(pos+1);

	for(int i=0;i<v[pos].size();i++)
		lang[v[pos][i]] = last[i];

	last.clear();

}	

main(){

		int te;
		scanf("%d",&te);
		
		for(int t=1;t<=te;t++){

			scanf("%d",&n);
			for(int i=0;i<n;i++) v[i].clear();

			memset(fixo,0,sizeof(fixo));
			memset(lang,0,sizeof(lang));
			mp.clear();

			cont = 1;

			for(int i=0;i<n;i++)
				while(1){
					scanf(" %s",aux);
					string str = (string) aux;
					for(int j=0;j<str.size();j++) assert(str[j] >= 'a' && str[j] <= 'z' && str.size());
					if(mp[str] == 0) mp[str] = cont++;
					v[i].pb(mp[str]);
					if(getchar() == '\n') break;
				}

			assert(cont < 3000);

			for(int i=0;i<v[0].size();i++)
				lang[v[0][i]] |= 1;
			for(int i=0;i<v[1].size();i++)
				lang[v[1][i]] |= 2;

				assert(v[n-1].size());

			ans = 999999;
			debug("ok\n");
			brute(2);

			printf("Case #%d: %d\n",t,ans);

		}

}
