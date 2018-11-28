#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstring>
using namespace std;
const int MAXN = 1005;
int T,n,sum,add;
char buf[MAXN];

int main(){
	freopen("input","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int cas = 0;cas < T;++ cas){
		printf("Case #%d: ",cas + 1);
		scanf("%d%s",&n,buf);
		sum = 0; add = 0;
		for(int i = 0;i <= n;++ i){
			if(sum < i){
				add += i - sum; sum = i;
			}
			sum += buf[i] - '0';
		}
		printf("%d\n",add);
	}
	return 0;
}
