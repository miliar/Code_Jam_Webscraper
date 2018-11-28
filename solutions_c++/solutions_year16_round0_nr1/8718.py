#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<list>
#include<sstream>
#include<utility>
#include<climits>
#include<fstream>
#include<bitset>

using namespace std;

#define lli long long int
#define max 1000005

bool f[16];

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);

	lli n,t,i,j,k,ans,kase;

	scanf("%lld",&kase);

	for(i=1;i<=kase;i++){
		scanf("%lld",&n);
		if(n==0){
			printf("Case #%lld: INSOMNIA\n",i);
			continue;
		}
		memset(f,0,sizeof(f));
		for(j=1;j<max;j++){
			t=ans=n*j;
			while(t){
				f[t%10]=1;
				t/=10;
			}
			for(k=0;k<10;k++){
				if(f[k]==0){
					break;
				}
			}
			if(k==10)break;
		}
		printf("Case #%lld: %lld\n",i,ans);
	}
	return 0;
}