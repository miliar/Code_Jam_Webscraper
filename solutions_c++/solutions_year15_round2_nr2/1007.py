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
#define MOD 1000003
#define MAXN 500005
typedef unsigned long long int uint64;
typedef long long int int64;

int r,c,n;
int ret;
int mat[17][17];
void cal(){
	int val=0;
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(i>0){
				if(mat[i][j]+mat[i-1][j]==2)
				val++;
			}
			if(j>0){
			if(mat[i][j]+mat[i][j-1]==2)
				val++;	
			}
		}
	}
	ret=min(ret,val);
}
void go(int x,int y,int place){
	if(!place){
		cal();
		return;
	}
	if(x>=r){
		go(0,y+1,place);
		return;
	}
	if(y>=c)
	return;
	mat[x][y]=1;
	go(x+1,y,place-1);
	mat[x][y]=0;
	go(x+1,y,place);
}

int main(){
	int t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>r>>c>>n;
		ret=1e9;
		memset(mat,0,sizeof(mat));
		go(0,0,n);
		cout<<ret<<endl;
	}
	fclose(stdout);
	return 0;
}
