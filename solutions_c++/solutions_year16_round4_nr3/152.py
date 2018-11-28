#include<stdio.h>
#include<utility>
using namespace std;
int R,C,a[99],b[99];
bool f[99][99];
pair<int,int> get_pos(int x){
	--x;
	if(x<C)return make_pair(0,2*x+1);
	x-=C;
	if(x<R)return make_pair(2*x+1, 2*C);
	x-=R;
	if(x<C)return make_pair(2*R, 2*C-(2*x+1));
	x-=C;
	return make_pair(2*R-(2*x+1),0);
}
pair<int,int> get_dir(int x){
	--x;
	if(x<C)return make_pair(1,0);
	x-=C;
	if(x<R)return make_pair(0,-1);
	x-=R;
	if(x<C)return make_pair(-1,0);
	return make_pair(0,1);
}
pair<int,int> reflect(pair<int,int> pos,pair<int,int> dir){
	pos.first += dir.first;
	pos.second += dir.second;
	if(f[pos.first/2][pos.second/2]){
		if(dir == make_pair(1,0)) dir = make_pair(0,-1);else
		if(dir == make_pair(0,-1)) dir = make_pair(1,0);else
		if(dir == make_pair(-1,0)) dir = make_pair(0,1);else
		if(dir == make_pair(0,1)) dir = make_pair(-1,0);
	}else{
		if(dir == make_pair(1,0)) dir = make_pair(0,1);else
		if(dir == make_pair(0,-1)) dir = make_pair(-1,0);else
		if(dir == make_pair(-1,0)) dir = make_pair(0,-1);else
		if(dir == make_pair(0,1)) dir = make_pair(1,0);
	}
	pos.first += dir.first;
	pos.second += dir.second;
	if(pos.first == 0 || pos.second == 0 || pos.first == 2*R || pos.second == 2*C)
		return pos;
	return reflect(pos,dir);
}
bool chk(){
	for(int i=0; i<R+C; i++)
		if(reflect(get_pos(a[i]),get_dir(a[i])) != get_pos(b[i]))
			return false;
	return true;
}
bool dfs(int x,int y){
	if(x==R){
		if(chk()){
			for(int i=0; i<R; i++,puts(""))
				for(int j=0; j<C; j++)
					putchar(f[i][j]?'/':'\\');
			return true;
		}
		return false;
	}
	if(y==C)
		return dfs(x+1,0);
	f[x][y] = true;
	if(dfs(x,y+1))return true;
	f[x][y] = false;
	if(dfs(x,y+1))return true;
	return false;
}
int main(){
	int _;
	scanf("%d",&_);
	for(int T=1; T<=_; T++){
		scanf("%d%d",&R,&C);
		for(int i=0; i<R+C; i++)
			scanf("%d%d",&a[i],&b[i]);
		printf("Case #%d:\n",T);
		if(!dfs(0,0))
			puts("IMPOSSIBLE");
	}
	return 0;
}