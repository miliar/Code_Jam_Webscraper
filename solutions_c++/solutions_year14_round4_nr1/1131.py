#include <map>
#include <set>
#include <queue>
#include <ctime>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define all(a) a.begin(),a.end()
#define clr(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<pair<int,int> > VII;

const double eps = 1e-8;
const double pi = acos(-1.0);

set<pair<int,int> > S;
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int tt, n, x, y, i;
	scanf("%d",&tt);
	for(int cal = 1; cal <= tt; ++cal){
		S.clear();
		scanf("%d%d",&n,&x);
		for(i=1;i<=n;++i){
			scanf("%d",&y);
			S.insert(mp(-y,i));
		}

		int ans = 0;
		while(!S.empty()){
			set<pair<int,int> >::iterator e = S.begin(), p;
			p = S.lower_bound(mp(-x-S.begin()->first,0));
			if(p == S.begin()){
				++p;
			}
			if(p == S.end()){
				S.erase(S.begin());
				ans++;
			}
			else{
				S.erase(S.begin());
				S.erase(p);
				ans++;
			}
		}
		printf("Case #%d: %d\n", cal, ans);
	}
    return 0;
}

