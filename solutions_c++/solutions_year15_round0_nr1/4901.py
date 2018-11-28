#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#define mx(a,b) ((a>b)? a:b)
#define mn(a,b) ((a<b)? a:b)
#define inf 2000000000
using namespace std;
char str[1010];
void solve(){
	int T,len,cnt,ans;
	scanf("%d",&T);
	for(int k=1;k<=T;k++){
		cnt=ans=0;
		scanf("%d %s",&len,str);
		for(int i=0;i<=len;i++){
			if(cnt<i)
				ans+=i-cnt,cnt=i;
			cnt+=str[i]-'0';
		}
		printf("Case #%d: %d\n",k,ans);
	}
}
int main(){
	solve();
	return 0;
}