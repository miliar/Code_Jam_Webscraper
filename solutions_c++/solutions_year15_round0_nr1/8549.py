#include <cstdio>
#include <cstring>
#define f(x,y,z) for(int x = (y),__ = (z);x < __;++x)
#define fd(x,y,z) for(int x = (y),__ = (z);x > __;--x)
#define gd(x,y,z) for(int x = (y),__ = (z);x >= __;--x)
#define g(x,y,z) for(int x = (y),__ = (z);x <= __;++x)
int t;
int smax,ans,now;
char buf[1024];
int main(){
#ifdef LOCAL
freopen("a.in","r",stdin);
#endif
	scanf("%d",&t);
	g(id,1,t){
		scanf("%d%s",&smax,buf);
		ans = 0;now = buf[0] - '0';
		g(i,1,smax){
			if (buf[i] != '0' && i > now){
				ans += i - now;
				now += i - now;
			}
			now += buf[i] - '0';
		}
		printf("Case #%d: %d\n",id,ans);
	}
	return 0;
}
