#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cin.tie(0);
using namespace std;
#define pb push_back
#define pob pop_back
#define pf push_front
#define pof pop_front
#define mp make_pair
#define all(a) a.begin(),a.end()
#define bitcnt(x) __builtin_popcountll(x)
#define MOD 1000000000
#define MAXN 500005
typedef unsigned long long int uint64;
typedef long long int int64;

int ans[5][5][5];
void pre(){
	ans[2][1][1]=1;
	ans[2][1][3]=1;
	ans[2][3][1]=1;
	ans[2][3][3]=1;

	ans[3][1][1]=1;
	ans[3][1][2]=1;
	ans[3][1][3]=1;
	ans[3][1][4]=1;
	ans[3][2][1]=1;
	ans[3][2][2]=1;
	ans[3][2][4]=1;
	ans[3][3][1]=1;
	ans[3][4][1]=1;
	ans[3][4][2]=1;
	ans[3][4][4]=1;
	
	ans[4][4][1]=1;
	ans[4][4][2]=1;
	ans[4][1][4]=1;
	ans[4][1][3]=1;
	ans[4][1][2]=1;
	ans[4][1][1]=1;
	ans[4][2][1]=1;
	ans[4][2][2]=1;
	ans[4][2][3]=1;
	ans[4][2][4]=1;
	ans[4][3][1]=1;
	ans[4][3][2]=1;
	ans[4][3][3]=1;
	
}
int main(){
	int t,x,r,c;
	pre();
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>x>>r>>c;
		if((x==1)||(!ans[x][r][c])){
			printf("GABRIEL\n");
		}
		else{
			printf("RICHARD\n");
		}
	}
	fclose(stdout);
	return 0;
}
