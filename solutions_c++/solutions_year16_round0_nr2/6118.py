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

#define inf 1000000007
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define pif pair<int,double>
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back
#define maxn 50500

#define count blergh

typedef long long ll;
using namespace std;

char str[110];

main(){

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){

		scanf(" %s",str);

		int n = strlen(str);

		int ans = 0;
		if(str[n-1] == '-')
			ans = 1;
		for(int i=0;i<n-1;i++)
			if(str[i] != str[i+1])
				ans++;

		printf("Case #%d: %d\n",t,ans);

	}

}
			
