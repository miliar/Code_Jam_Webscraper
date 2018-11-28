#include <bits/stdc++.h>
#define IT(e) typeof((e).begin())
#define FE(i,e) for(IT(e) i=(e).begin(); i!=(e).end(); i++)
#define F(i,b,n) for(typeof(n) i=(b), _n=(n); i<_n; i++)
#define MS(e,v) memset(e,v,sizeof(e))
#define OO ~(1<<31)
#define PB push_back

using namespace std;

bool won(string *grid, char p){
	int di=0, dd=0;
	F(i,0,4){
		int r=0, c=0;
		F(j,0,4){
			if(grid[i][j]==p || grid[i][j]=='T') r++;
			if(grid[j][i]==p || grid[j][i]=='T') c++;
			if(i==j && (grid[i][j]==p || grid[i][j]=='T')) di++;
			if(i==3-j &&  (grid[i][j]==p || grid[i][j]=='T')) dd++;
		}
		if(r==4 || c==4) return true;
	}
	return di==4 || dd==4;
}
bool full(string *grid){
	int cnt=0;
	F(i,0,4) F(j,0,4) if(grid[i][j]=='.') cnt++;
	return cnt==0;
}

int main(){
	freopen("aa.in","r",stdin);
	//freopen("aa.out","w",stdout);
	int t; string grid[4];
	cin>>t;
	for(int cs=1; cs<=t; cs++){
		F(i,0,4) cin>>grid[i];
		cout<<"Case #"<<cs<<": ";
		if(won(grid,'X')) cout<<"X won"<<endl;
		else if(won(grid,'O')) cout<<"O won"<<endl;
		else if(full(grid)) cout<<"Draw"<<endl;
		else cout<<"Game has not completed"<<endl;
	}
	return 0;
}
