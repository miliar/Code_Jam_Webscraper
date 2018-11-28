#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
//#define LOCAL
const int N = 200;
char s[N],t[N];

int main(){
	int T;
	#ifdef LOCAL
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	scanf("%d",&T);
	for(int times=1;times<=T;times++){
		scanf("%s",s+1);
		int n = strlen(s+1);
		int tt=1;
		for(int i=2;i<=n;i++)
			tt += s[i] != s[i-1];
		if (s[n]=='+') tt--;
		printf("Case #%d: %d\n",times,tt);
	}
	return 0;
}