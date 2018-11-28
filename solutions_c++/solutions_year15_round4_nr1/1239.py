#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
typedef double db;
typedef pair<int,int> pii;
#define y1 y1_
#define ran() (rand()<<15|rand())

const int mo=(int)1e9+7,inf=(int)1e9;
const ll linf=(ll)1e18;

int n,m;
char a[105][105];

bool dangerous(int i,int j){
	bool danger=true;
	if(a[i][j]=='^'){
		for(int k=i-1;k>=1;k--) if(a[k][j]!='.'){
			danger=false;
			break;
		}
	}
	else
	if(a[i][j]=='v'){
		for(int k=i+1;k<=n;k++) if(a[k][j]!='.'){
			danger=false;
			break;
		}
	}
	else
	if(a[i][j]=='<'){
		for(int k=j-1;k>=1;k--) if(a[i][k]!='.'){
			danger=false;
			break;
		}
	}
	else
	if(a[i][j]=='>'){
		for(int k=j+1;k<=m;k++) if(a[i][k]!='.'){
			danger=false;
			break;
		}
	}
	else
		danger=false;
	return danger;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T; scanf("%d",&T);
	for(int Case=1;Case<=T;Case++){
		scanf("%d%d",&n,&m);
		int ans=0;
		for(int i=1;i<=n;i++)
			scanf("%s",a[i]+1);
		for(int i=1;i<=n&&ans!=-1;i++)
			for(int j=1;j<=m&&ans!=-1;j++) if(dangerous(i,j)){
				ans++;
				a[i][j]='^';
				if(!dangerous(i,j)) continue;
				a[i][j]='v';
				if(!dangerous(i,j)) continue;
				a[i][j]='<';
				if(!dangerous(i,j)) continue;
				a[i][j]='>';
				if(!dangerous(i,j)) continue;
				ans=-1;
				break;
			}
		printf("Case #%d: ",Case);
		if(ans==-1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans);
	}
	scanf("\n");
}
