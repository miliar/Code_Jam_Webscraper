#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
#define FOR(i,l,r) for(int i=l; i<=r; i++)
#define COR(i,r,l) for(int i=r; i>=l; i--)
#define FILL(a,b) memset(a,b,sizeof(a))
#define INF 1000000000
#define N 120001
int n,m,T,ans,a[10][10],b[10][10],c[20];
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	FOR(t,1,T){
		FILL(c,0);
		scanf("%d",&n);
		FOR(i,1,4) FOR(j,1,4) scanf("%d",&a[i][j]);
		FOR(i,1,4) c[ a[n][i] ] ++;
		scanf("%d",&m);
		FOR(i,1,4) FOR(j,1,4) scanf("%d",&b[i][j]);
		FOR(i,1,4) c[ b[m][i] ] ++;
		ans = 0;
		printf("Case #%d: ",t);
		FOR(i,1,16) if( c[i] == 2 ){
			if( ans != 0 ){
				puts("Bad magician!");
				ans = -1;
				break;
			}
			ans = i;
		}
		if( ans == 0 ) puts("Volunteer cheated!");
		else if( ans > 0 ) printf("%d\n",ans);
	}
	
	return 0;
}

