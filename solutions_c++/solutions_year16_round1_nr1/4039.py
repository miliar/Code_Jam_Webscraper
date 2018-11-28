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
#define Max 2024

char s[Max],ans[2*Max];

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);

	lli n,t,i,j,k,kase,len,f,e;
	char cur,pas;
	scanf("%lld",&kase);

	for(i=1;i<=kase;i++){
		scanf("%s",s);
		len=strlen(s);
		f=e=2000;
		ans[f]=s[0];
		for(j=1;j<len;j++){
			if(s[j]>=ans[f]){
				ans[f-1]=s[j];
				f--;
			}
			else{
				ans[e+1]=s[j];
				e++;
			}
		}
		printf("Case #%lld: ",i);
		for(j=f;j<=e;j++){
			printf("%c",ans[j]);
		}
		printf("\n");
	}
	return 0;
}