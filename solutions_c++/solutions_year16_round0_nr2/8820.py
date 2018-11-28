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

char S[200];

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);

	lli n,t,i,j,k,l,ans,kase;

	scanf("%lld",&kase);

	for(i=1;i<=kase;i++){
		scanf("%s",S);
		l = strlen(S);
		S[l]='+';
		ans=t=0;
		for(j=1;j<=l;j++){
			if(S[j-1]=='+')
				t=1;
			if(S[j]=='+' && S[j-1]=='-'){
				if(t==0){
					ans++;
				}
				else{
					ans+=2;
				}
			}
		}
		printf("Case #%lld: %lld\n",i,ans);
	}
	return 0;
}