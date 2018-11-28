#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <string>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>

#define inf (1<<30)
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define pif pair<int,double>
#define pdp pair<double,pii>
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back
#define maxn 1001000
#define mod 1000000007

#define min3(a,b,c) min(min(a,b),c)
#define max3(a,b,c) max(max(a,b),c)

typedef long long ll;
using namespace std;

int pref[maxn];
int suf[maxn];

char st[maxn];
char str[maxn];

main(){

	int nt;
	scanf("%d",&nt);

	for(int t=1;t<=nt;t++){

		int n;
		scanf(" %s",str);
		n = strlen(str);

		int sz = 0;
		int cur = 0;
		for(int i=0;i<n;i++){
			if(sz == 0 || st[sz-1] != str[i])
				st[sz++] = str[i];
			else {
				sz--;
				cur++;
			}
			pref[i] = cur;
		}

		sz = 0;
		cur = 0;
		for(int i=n-1;i>=0;i--){
			if(sz == 0 || st[sz-1] != str[i]){
				st[sz++] = str[i];
			}
			else {
				sz--;
				cur++;
			}
			suf[i] = cur;
		}

		int ans = pref[n-1];

		if(n%2 == 1){
			ans = 0;
			for(int i=1;i<n-1;i++){
				ans = max(ans,pref[i-1]+suf[i+1]);
				//if(ans == 4)
					//debug("i %d : %d %d\n",i,pref[i-1],suf[i+1]);
			}
		}

		int tot = n/2;
		printf("Case #%d: %d\n",t,5*tot+5*ans);

	}

}
