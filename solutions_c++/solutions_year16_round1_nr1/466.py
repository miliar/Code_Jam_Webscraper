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

typedef long long ll;
using namespace std;

char str[1010];


main(){

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){

		scanf(" %s",str);
		int n = strlen(str);

		vector<char> ans;

		ans.pb(str[0]);

		for(int i=1;i<n;i++){
			if(str[i] >= ans[0]){
				ans.pb(str[i]);
				for(int j=ans.size()-1;j>=1;j--){
					swap(ans[j],ans[j-1]);
				}
			}
			else
				ans.pb(str[i]);
		}

		printf("Case #%d: ",t);
		for(int i=0;i<n;i++)
			printf("%c",ans[i]);
		printf("\n");

	}

}
