#include <bits/stdc++.h>

#define REP(i,n) for(i=0;i<n;i++)
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define DEC(i,a,b) for(i=a;i>=b;i--)
#define SKIP(i,a,b,k) for(i=a;i<=b;i+=k)
#define DEBUG printf("ok\n")
#define NL printf("\n")

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define SQR(x) (x)*(x)
#define MOD(a,b) ((a)%(b)+b)%(b)

#define N 100000
#define inf 2000000000

typedef long long ll;
typedef double db;

using namespace std;

int a[20][20];
int r,c,ans;
const int di[2]={1,0},dj[2]={0,1};

void play(int i,int n)
{
	if(n==0){
		int j,k,sum=0;
		FOR(i,1,r){
			FOR(j,1,c){
				//printf("%d",a[i][j]);
				if(a[i][j]) sum+=a[i-1][j]+a[i][j-1];
			}
		}

		ans=MIN(ans,sum);
		return;
	}
	FOR(i,i,r*c-1){
		a[i/c+1][i%c+1]=1;
		play(i+1,n-1);
		a[i/c+1][i%c+1]=0;
		play(i+1,n);
	}
}
void solve(int T)
{
	int n;
	scanf("%d %d %d",&r,&c,&n);
	ans=inf;
	play(0,n);
	printf("Case #%d: %d\n",T,ans);
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin); freopen("1.out","w",stdout);
	int T,i;
	scanf("%d",&T);
	FOR(i,1,T) solve(i);
	return 0;
}