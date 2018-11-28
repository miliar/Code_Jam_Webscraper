#include <cstdio>
#include <map>
#include <vector>
#include <cstring>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;
//#define maxn 50001
#define maxq 50001
#define maxe 100001
#define inf 100000007
#define ll long long
template <class T> T f_max(T x,T y){return x>y?x:y;}
template <class T> T f_min(T x,T y){return x<y?x:y;}
template <class T> void f_swap(T &x,T &y){T t;t=x,x=y,y=t;}
#define maxn 5
int a[maxn][maxn];
int b[maxn][maxn];
int main(){
	int n;
	int t;

	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	scanf("%d",&t);
	int i,j,cas;
	for(cas=1;cas<=t;cas++){
		int n=4;
		int x,y;
		scanf("%d",&x);
		for(i=1;i<=n;i++) for(j=0;j<n;j++) scanf("%d",&a[i][j]);
		sort(a[x],a[x]+n);
		scanf("%d",&y);
		for(i=1;i<=n;i++) for(j=0;j<n;j++) scanf("%d",&b[i][j]);
		sort(b[y],b[y]+n);
		int ans=0;
		j=0;
		for(i=0;i<n;i++){
			while( j <n && b[y][j]<a[x][i]) j++;
			if(j==n) break;
			if(a[x][i]==b[y][j]){
				if(!ans) ans=a[x][i];
				else ans=-1;
			}
		}
		printf("Case #%d: ",cas);
		if(ans==-1) printf("Bad magician!\n");
		else if(ans==0) printf("Volunteer cheated!\n");
		else printf("%d\n",ans);
	}
	return 0;
}