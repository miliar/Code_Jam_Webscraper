#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define CLR(i) memset(i,0,sizeof(i))
#define ll long long

int T,n,p;

int main(){
	scanf("%d",&T);
	FOE(t,1,T){
		scanf("%d%d",&n,&p);

		int num = (1<<n);
		int a,b;
		FOR(x,0,num){
			//printf("%d!\n",x);
			//BEST
			int before = x, after = num-x-1;
			int b_pos,w_pos;
			FOR(i,0,n){
				if (before && after){
					if (before % 2){
						before = (before + 1)/2;
						after = (after - 2)/2;
					}
					else{
						before /= 2;
						after = (after - 1)/2;
					}
				}
				else{
					b_pos = before + 1;;
					break;
				}
			}
			//WORST
			before = x, after = num-x-1;
			FOR(i,0,n){
				//printf("%d: %d %d\n",i,before,after);
				if (before && after){
					if (after % 2){
						before = (before - 2)/2;
						after = (after + 1)/2;
					}
					else{
						before = (before - 1)/2;
						after /= 2;
					}
				}
				else{
					w_pos = num - after;
					break;
				}
			}
			if (b_pos <= p) b = x;
			if (w_pos <= p) a = x;
		}
		printf("Case #%d: %d %d\n",t,a,b);
	}
	return 0;
}
