#include <cstdio>
#include <algorithm>

#define MAX 1003

using namespace std;

char s[MAX];

int main()
{
	int n,t,T,i,ans,standing;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		ans = standing = 0;
		scanf("%d %s",&n,s);
		for(i=0;i<=n;i++) {
			if(standing<i) {
				ans += i-standing;
				standing += i-standing;
			}
			standing += s[i]-'0';
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}