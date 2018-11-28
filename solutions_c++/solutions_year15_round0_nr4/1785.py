#include <iomanip>
#include <map>
#include <queue>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <map>
//#pragma comment(linker,"/STACK:1024000000,1024000000")
inline const int getint() { int r=0, k=1; char c=getchar(); for(; c<'0'||c>'9'; c=getchar()) if(c=='-') k=-1; for(; c>='0'&&c<='9'; c=getchar()) r=r*10+c-'0'; return k*r; }

using namespace std;
#define eps 1e-9
#define LL long long
#define ull unsigned long long
#define Rep(i,l,r) for(i=(l);i<(r);i++)
#define rep(i,l,r) for(i=(l);i<=(r);i++)
#define red(i,l,r) for(i=(l);i>=(r);i--)
#define pb push_back
#define mp make_pair
const int maxn=1e5+10;
int ans[5][5][5];
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	for(int j=1;j<=4;j++){
		for(int k=j;k<=4;k++){
			ans[1][j][k]=2;
		}
	}
	ans[2][1][1]=1,ans[2][1][2]=2,ans[2][1][3]=1,ans[2][1][4]=ans[2][2][2]=ans[2][2][3],ans[2][2][4]=ans[2][3][4]=ans[2][4][4]=2,ans[2][3][3]=1;
	ans[3][1][1]=ans[3][1][2]=ans[3][1][3]=ans[3][1][4]=ans[3][2][2]=1,ans[3][2][3]=2,ans[3][2][4]=1,ans[3][3][3]=ans[3][3][4]=2,ans[3][4][4]=1;
		for(int j=1;j<=4;j++){
			for(int k=j;k<=4;k++){
				ans[4][j][k]=1;
			}
		}
		ans[4][3][4]=ans[4][4][4]=2;
	int x,r,c;
	int T;
	scanf("%d",&T);
	int ka=1;
	while(T--){
		scanf("%d%d%d",&x,&r,&c);
		printf("Case #%d: ",ka++);
		if(r>c)swap(r,c);
		if(ans[x][r][c]==1){
			cout<<"RICHARD"<<endl;
		}
		else cout<<"GABRIEL"<<endl;
	}
	return 0;
}