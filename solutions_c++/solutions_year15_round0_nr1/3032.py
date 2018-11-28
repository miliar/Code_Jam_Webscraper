#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;

char str[1005];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int T,tcase=1;
	for(scanf("%d",&T);tcase<=T;tcase++){
		int n;
		scanf("%d%s",&n,str);
		int cnt=0;
		int ans=0;
		for(int i=0;i<=n;i++){
			if(str[i]=='0')continue;
			if(cnt<i){
				ans+=i-cnt;
				cnt=i;
			}
			cnt+=str[i]-'0';
		}
		printf("Case #%d: ",tcase);
		printf("%d\n",ans);
	}
    return 0;
}

