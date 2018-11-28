#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;
#define N 105
#define MOD 1000000007
#define inf 1<<28
#define LL long long
#define abs(a) (a)<0?(-a):(a)
#define CLR(a) memset((a),0,sizeof((a)))
#define FRIN freopen("B-large.in","r",stdin)
#define FROUT freopen("Blarge.txt","w",stdout)
int brd[N][N],n,m;
bool visit[102];
bool check(int r,int c,int h){
	int i,j;
	bool f1=true,f2=true;
	/*printf("pattern %d %d\n",n,m);
	cout<<endl;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++) {
			printf("%d ",pat[i][j]);
			//if(brd[i][j]!=pat[i][j]) return false;
		}
		cout<<endl;
	}*/
	for(i=c;i<m;i++){
		if(brd[r][i]>h) f2=false;
	}
	for(i=c-1;i>=0;i--){
		if(brd[r][i]>h) f2=false;
	}
	for(i=r;i<n;i++){
		if(brd[i][c]>h) f1=false;
	}
	for(i=r-1;i>=0;i--){
		if(brd[i][c]>h) f1=false;
	}
	if(!f1&&!f2) return false;
	else return true;
}
int main(){
	//FRIN;
	//FROUT;
	int test,i,j,k,ii;
	bool f;
	scanf("%d",&test);
	for(k=1;k<=test;k++){
		scanf("%d%d",&n,&m);
		CLR(visit);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				scanf("%d",&brd[i][j]);
				visit[brd[i][j]]=true;
			}
		}
	//	printf("r=%d c=%d",n,m);
		printf("Case #%d: ",k);
		if(n==1&&m==1){
		  printf("YES\n");
		  continue;
		}
		f=true;
		for(i=1;i<101;i++){
			if(visit[i]){
				for(ii=0;ii<n&&f;ii++){
					for(j=0;j<m&&f;j++){
						if(brd[ii][j]==i) f=check(ii,j,i);
					}
				}
			}
		}
		if(f) printf("YES\n");
		else  printf("NO\n");
	}
	return 0;
}
