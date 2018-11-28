#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int T,N,M;
string map[101];
bool ismap(int x,int y){
	if(x < 0) return false;
	if(x >= N) return false;
	if(y < 0) return false;
	if(y >= M) return false;
	return true;
}
int check(int X,int Y){
	int x,y,f;
	int res = -1;
	// >
	x=X,y=Y;f=0;
	while(true){
		y++;
		if(ismap(x,y)){
			if(map[x][y] !='.'){
				f=1;
				break;
			}
		} else break;
	}
	if( f==1 ){
		if(map[X][Y]=='>') res= max(res,2);
		else res= max(res,1);
	}
	// <
	x=X,y=Y;f=0;
	while(true){
		y--;
		if(ismap(x,y)){
			if(map[x][y] !='.'){
				f=1;
				break;
			}
		} else break;
	}
	if( f==1 ){
		if(map[X][Y]=='<') res= max(res,2);
		else res= max(res,1);
	}
	// v
	x=X,y=Y;f=0;
	while(true){
		x++;
		if(ismap(x,y)){
			if(map[x][y] !='.'){
				f=1;
				break;
			}
		} else break;
	}
	if( f==1 ){
		if(map[X][Y]=='v') res= max(res,2);
		else res= max(res,1);
	}
	// ^
	x=X,y=Y;f=0;
	while(true){
		x--;
		if(ismap(x,y)){
			if(map[x][y] !='.'){
				f=1;
				break;
			}
		} else break;
	}
	if( f==1 ){
		if(map[X][Y]=='^') res= max(res,2);
		else res= max(res,1);
	}
	return res;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N >> M;
		bool F = false;
		int ans =0;
		for(int i=0;i<N;i++){
			cin >> map[i];
		}
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				if(map[i][j] !='.'){
					int k = check(i,j);
					if(k == 1) ans ++ ;
					if(k== -1) F = 1;
				}
			}
		}
		printf("Case #%d: ",t);
		if(F) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}
