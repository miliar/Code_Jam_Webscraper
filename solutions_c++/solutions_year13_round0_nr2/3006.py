#include <cstdio>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,1,n+1)
using namespace std;
int n,m;
int lawn[100][100];
bool check(){
	int row[100]={0};
	int col[100]={0};
	FOR(i,0,n){
		FOR(j,0,m){
			row[i]=max(row[i],lawn[i][j]);
			col[j]=max(col[j],lawn[i][j]);
		}
	}
	int vlawn[100][100];
	FOR(i,0,n){
		FOR(j,0,m){
			vlawn[i][j]=min(row[i],col[j]);
		}
	}
	FOR(i,0,n){
		FOR(j,0,m){
			if(lawn[i][j]!=vlawn[i][j])return false;
		}
	}
	return true;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    int T;scanf("%d",&T);
	REP(t,T){
		scanf("%d %d",&n,&m);
		FOR(i,0,n){
			FOR(j,0,m){
				scanf("%d",&lawn[i][j]);
			}
		}
		if(check()){
			printf("Case #%d: YES\n",t);
		}
		else{
			printf("Case #%d: NO\n",t);
		}
	}
	
}	