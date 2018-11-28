#include <bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define ALL(G) (G).begin(),(G).end()

typedef long long ll;
typedef double D;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int inft = 1000000009;
const int MAXN = 106;//10^6

char s[MAXN][MAXN];
bool forb[MAXN][MAXN][4];
void solve() {
	int r,c;
	scanf("%d%d",&r,&c);
	fru(i,r)scanf("%s",s[i]);
	fru(i,r)fru(j,c)fru(h,4)forb[i][j][h]=0;

	// <
	fru(i,r){
		fru(j,c){
			if(s[i][j]=='.')continue;
			else {forb[i][j][0]=1;break;}
		}
	}
	// >
	fru(i,r){
		fru(j,c){
			if(s[i][c-j-1]=='.')continue;
			else {forb[i][c-j-1][1]=1;break;}
		}
	}
	//^
	fru(j,c){
		fru(i,r){
			if(s[i][j]=='.')continue;
			else {forb[i][j][2]=1;break;}
		}
	}
	//v
	fru(j,c){
		fru(i,r){
			if(s[r-i-1][j]=='.')continue;
			else {forb[r-i-1][j][3]=1;break;}
		}
	}
	bool poss=true;
	int ile=0;
	fru(i,r)fru(j,c)
	{
		int sum=0;
		fru(h,4)sum+=forb[i][j][h];
		if(sum==4 && s[i][j]!='.')poss=false;
	}
	fru(i,r)fru(j,c)
	{
		if(s[i][j]=='<' && forb[i][j][0])ile++;
		if(s[i][j]=='>' && forb[i][j][1])ile++;
		if(s[i][j]=='^' && forb[i][j][2])ile++;
		if(s[i][j]=='v' && forb[i][j][3])ile++;
	}
	if(!poss)printf("IMPOSSIBLE\n");
	else printf("%d\n",ile);
}
int main(){
	int t=1;scanf("%d",&t);
	fru(i,t)
	{
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}

