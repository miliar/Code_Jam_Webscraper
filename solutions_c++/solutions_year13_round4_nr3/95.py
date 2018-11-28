//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define N 2010
int		last[N],first[N];
int		a[N],b[N],n,ans[N];
bool	mark[N],used[N];
queue<int> v;

int		ecnt;
struct	Edge{
	int to,w;
	Edge *next;
}*mat[N],edges[N*4];
void	link(int x,int to,int w){
	swap(x,to);
	edges[ecnt].to = to;
	edges[ecnt].w = w;
	edges[ecnt].next = mat[x];
	mat[x] = &edges[ecnt++];
}

bool	in_que[N];
int		dis[N];

bool	check(int &x,int y){
	if ( x < y ) { x = y; return true; }
	return false;
}

void	spfa(int st){
	queue<int> que;
	while ( !que.empty() ) que.pop();
	memset( in_que , 0 , sizeof(in_que) );
	Rep(i,n) dis[i] = -1;
	dis[st] = 0;
	que.push( st );
	while ( !que.empty() ){
		int i = que.front();  que.pop();
		in_que[i] = 0;
		for ( Edge *p = mat[i]; p ; p = p->next ){
			int to = p->to;
			if ( check( dis[to] , dis[i]+1 ) && !in_que[to] ){
				in_que[to] = 1;
				que.push( to );
			}
		}
	}
	int num = 1;
	for(int i = st+1; i<n; i++) 
		if ( dis[i]>0 ) num++;
	for(int g = 1; g<=n; g++){
		if ( used[g] ) continue;
		num--;
		if ( num == 0 ){
			ans[st] = g;
			used[g] = 1;
			return;
		}
	}
}
int		main(){
	int cas , tt = 0;
	scanf("%d", &cas );
	while ( cas -- ){
		scanf("%d", &n );
		Rep(i,n) scanf("%d", &a[i] );
//		Rep(i,n) printf("%d(%d) ", i ,a[i] ); puts("");
		Rep(i,n) scanf("%d", &b[i] );
		memset(last, -1 , sizeof(last) );
		ecnt = 0;
		memset( mat , 0 , sizeof(mat) );
		memset( mark, 0 , sizeof(mark));
		memset( used, 0 , sizeof(used));
		Rep(i,n){
			if ( a[i] > 1 ) 
				link( last[a[i]-1] , i , 1 );
			if ( last[a[i]] != -1 )
				link( i , last[a[i]] , 0 );
			last[a[i]] = i;
		}
		memset(last, -1 , sizeof(last) );
		for(int i = n-1; i>=0; i--){
			if ( b[i] > 1 ) 
				link( last[b[i]-1] , i , 1 );
			if ( last[b[i]] != -1 )
				link( i , last[b[i]] , 0 );
			last[b[i]] = i;
		}
		int gg = 0;
		Rep(i,n) spfa(i);
		printf("Case #%d:", ++tt );
		Rep(i,n) printf(" %d", ans[i] ); puts("");
	}
	return 0;
}
