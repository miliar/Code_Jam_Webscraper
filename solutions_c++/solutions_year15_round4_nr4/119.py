#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
using namespace std;
int T,N,M;
int mapp[10][10],ans;
map<string,int> ck;
bool ismapp(int x,int y){
	if(x < 0 ) return false;
	if(x >= N) return false;
	if(y < 0 ) return false;
	if(y >= M) return false;
	return true;
}
bool check(){
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			int k=0;
			int c = mapp[i][j];
			if(ismapp(i-1,j) && mapp[i-1][j] == c) k++;
			if(ismapp(i+1,j) && mapp[i+1][j] == c) k++;
			if(ismapp(i,(j-1+M)%M) && mapp[i][(j-1+M)%M] == c) k++;
			if(ismapp(i,(j+1)%M) && mapp[i][(j+1)%M] == c) k++;
			if(c!=k) return false;
		}
	}
}
string makestring(int x){
	string res = "";
	for(int i=0;i<N;i++){
		for(int k=x;k<x+M;k++){
			int j=k%M;
			res += mapp[i][j] + '0';
		}
	}
	return res;
}
void dfs(int x,int y){
	if(x==N){
		if(check()){
			string a = makestring(0);
			if(!ck[a]){
				ans++;
				for(int i=0;i<M;i++){
					ck[makestring(i)]=true;
				}
			}
		}
		return;
	}
	for(int i=1;i<=3;i++){
		mapp[x][y] = i;
		if(x>0){
			int k=mapp[x-1][y];
			int c=0;
			if(mapp[x][y] == k) c++;
			if(mapp[x-1][(y+1)%M]==k) c++;
			if(mapp[x-1][(y-1+M)%M]==k) c++;
			if(x>1 && mapp[x-2][y]==k) c++;
			if(c!=k) continue;
		}
		if(y+1==M) dfs(x+1,0);
		else dfs(x,y+1);
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T;
	for(int t=1;t<=T;t++){
		cin >> N >> M;
		ck.clear();
		ans=0;
		memset(mapp,0,sizeof(mapp));
		dfs(0,0);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
