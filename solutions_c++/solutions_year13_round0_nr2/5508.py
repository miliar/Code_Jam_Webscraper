#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
#include<vector>

using namespace std;

#define FOR(i,n,first) for(int i=first;i<n;i++)
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
#define pb push_back
#define N 110
#define M 101000
const int MOD=100000007;
const int INF = 0x3f3f3f3f;
typedef long long int Int64;
//#define SMALL

int vis[N][N];
int maps[N][N];
int n,m;

bool dfs(int cow,int col){
	//printf("%d,%d\n",cow,col);
	for(int i=1;i<=n;i++){
	//	printf("%d,%d---%d-%d\n",i,col,maps[i][col],maps[cow][col]);
		if(maps[i][col]!=maps[cow][col])return true;
	}
	return false;
}

int main()
{
	#ifdef SMALL
    freopen("B-small-attempt2.in","rt",stdin);
   //  freopen("text.in","rt",stdin);
    freopen("text.out","w",stdout);
    #endif
    int cas;
    scanf("%d",&cas);
    for(int ii=1;ii<=cas;ii++){
    	scanf("%d%d",&n,&m);
    	for(int i=1;i<=n;i++){
    		for(int j=1;j<=m;j++){
    			scanf("%d",&maps[i][j]);
    		}
    	}
    	printf("Case #%d: ",ii);
    	if(n==1||m==1){
    		puts("YES");
    		continue;
    	}
    	bool flag=false;
    	set<int>sets;
    	for(int i=1;!flag&&i<=n;i++){
    		int k=-1;
    		for(int j=1;j<=m;j++){
    			k=max(k,maps[i][j]);
    		}
    		for(int j=1;!flag&&j<=m;j++){
    			if(maps[i][j]!=k)
    				flag=dfs(i,j);
    		//	printf("k=%d,%d\n",k,flag);
    		}
    	}

    	(flag==true)?puts("NO"):puts("YES");
    }
    	
    
    return 0;
}