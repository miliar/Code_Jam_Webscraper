#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
using namespace std;


int dy[]={0,1,0,-1};
int dx[]={1,0,-1,0};

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int testcase;
	cin>>testcase;
	rep(_,testcase){
		int r,c;
		cin>>r>>c;
		vector<string> b(r);
		rep(i,r)cin>>b[i];
		int ans=0;
		bool no=false;
		rep(y,r)rep(x,c){
			int dir=-1;
			if(b[y][x]=='>')dir=0;
			else if(b[y][x]=='v')dir=1;
			else if(b[y][x]=='<')dir=2;
			else if(b[y][x]=='^')dir=3;
			if(dir==-1)continue;
			bool f=false;
			int s=y,t=x;
			while(1){
				s+=dy[dir];
				t+=dx[dir];
				if(s<0||r<=s||t<0||c<=t)break;
				if(b[s][t]!='.'){
					f=true;
					break;
				}
			}
			if(f)continue;
			f=false;
		 	rep(d,4){
				if(d==dir)continue;
				int s=y,t=x;
				while(1){
					s+=dy[d];
					t+=dx[d];
					if(s<0||r<=s||t<0||c<=t)break;
					if(b[s][t]!='.'){
						f=true;
						break;
					}
				}
			}
			if(!f)no=true;
			ans++;
		}
		cout<<"Case #"<<_+1<<": ";
		if(no)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}