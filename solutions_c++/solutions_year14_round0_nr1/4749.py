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

int t;
bool a[20],b[20];

int main(){
	scanf("%d",&t);
	FOE(T,1,t){
		CLR(a); CLR(b);
		int x,y,tmp;
		scanf("%d",&x);
		FOE(i,1,4){
			FOE(j,1,4){
				scanf("%d",&tmp);
				if (i==x) a[tmp]=1;
			}
		}
		scanf("%d",&y);
		FOE(i,1,4){
			FOE(j,1,4){
				scanf("%d",&tmp);
				if (i==y) b[tmp] = 1;
			}
		}

		int num=0,ans;
		FOE(i,1,16){
			if (a[i] && b[i]) ++num,ans=i;
		}
		printf("Case #%d: ",T);
		if (num==0) printf("Volunteer cheated!");
		else if (num==1) printf("%d",ans);
		else printf("Bad magician!");
		printf("\n");
	}
	return 0;
}
